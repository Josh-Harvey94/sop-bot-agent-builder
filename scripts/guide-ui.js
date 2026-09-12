'use strict';
const prefix = 'sopbot-' + guideData.fingerprint + '-';
const el = id => document.getElementById(id);
const escapeText = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const memory = new Map();
function storageWarning() { el('storageNotice').hidden = false; }
function getState(key) { try { return localStorage.getItem(prefix + key); } catch { storageWarning(); return memory.get(key) ?? null; } }
function setState(key, value) { memory.set(key,value); try { localStorage.setItem(prefix + key,value); } catch { storageWarning(); } }

el('promptDisplay').innerHTML = guideData.prompts.map((p,i) => `<div class="prompt-panel" data-panel="${i}"><p><strong>Title</strong></p><div class="paste">${escapeText(p.title)}<button class="copy">Copy</button></div><p><strong>Prompt</strong></p><div class="paste">${escapeText(p.prompt)}<button class="copy">Copy</button></div></div>`).join('');
function showPrompt(index) {
  document.querySelectorAll('.tab').forEach((button,i) => { button.classList.toggle('active', i===index); button.setAttribute('aria-pressed', String(i===index)); });
  document.querySelectorAll('.prompt-panel').forEach((panel,i) => panel.classList.toggle('inactive', i!==index));
}
document.querySelectorAll('.tab').forEach(button => button.addEventListener('click', () => showPrompt(Number(button.dataset.prompt))));
showPrompt(0);

document.querySelectorAll('.copy').forEach(button => button.addEventListener('click', async event => {
  event.stopPropagation();
  const clone = button.parentElement.cloneNode(true);
  clone.querySelectorAll('button').forEach(node => node.remove());
  const text = clone.textContent.trim();
  try {
    if (!navigator.clipboard) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(text);
    const old = button.textContent;
    button.textContent = 'Copied ✓';
    el('copyNotice').textContent = 'Text copied.';
    setTimeout(() => button.textContent = old, 1600);
  } catch {
    el('manualCopy').value = text;
    el('copyDialog').showModal();
    el('manualCopy').focus();
    el('manualCopy').select();
  }
}));

el('tests').innerHTML = guideData.tests.map(test => `<div class="test"><div><strong>${escapeText(test.id)}. ${escapeText(test.name)}</strong>${test.file ? `<p class="mini">Input: <a href="../${escapeText(test.file)}" download>Download synthetic SOP</a> (or copy its full text)</p>` : '<p class="mini">No attachment for this test.</p>'}<p class="mini"><b>Try:</b> ${escapeText(test.prompt)}</p><p class="mini"><b>Expect:</b> ${escapeText(test.expected)}</p></div><div class="status" data-test="${test.id}" role="group" aria-label="${escapeText(test.name)} result"><button data-v="not">Not run</button><button data-v="pass">Pass</button><button data-v="fix">Fix</button></div></div>`).join('');
document.querySelectorAll('.status').forEach(group => {
  const saved = getState('test-' + group.dataset.test);
  const initial = ['not','pass','fix'].includes(saved) ? saved : 'not';
  function setButtons(value) { group.querySelectorAll('button').forEach(button => { button.classList.toggle('active',button.dataset.v===value); button.setAttribute('aria-pressed',String(button.dataset.v===value)); }); }
  setButtons(initial);
  group.querySelectorAll('button').forEach(button => button.addEventListener('click', () => { setButtons(button.dataset.v); setState('test-' + group.dataset.test,button.dataset.v); gate(); }));
});
el('checks').innerHTML = guideData.groups.map((group,gi) => `<div class="card"><h3>${escapeText(group[0])}</h3>${group[1].map((text,i) => `<label class="control-label"><input type="checkbox" data-gate="${gi}-${i}"> ${escapeText(text)}</label>`).join('')}</div>`).join('');
document.querySelectorAll('[data-gate]').forEach(box => {
  box.checked = getState('control-' + box.dataset.gate)==='1';
  box.addEventListener('change', () => { setState('control-' + box.dataset.gate,box.checked ? '1' : '0'); gate(); });
});
const taskBoxes = [...document.querySelectorAll('[data-task]')];
taskBoxes.forEach((box,i) => {
  box.checked = getState('task-' + i)==='1';
  box.setAttribute('aria-label', 'Complete task: ' + box.closest('summary').textContent.trim());
  box.addEventListener('click',event => event.stopPropagation());
  box.addEventListener('change',() => { setState('task-' + i,box.checked ? '1' : '0'); progress(); gate(); });
});
function progress() {
  const done = taskBoxes.filter(box => box.checked).length;
  document.querySelectorAll('.progress-fill').forEach(node => node.style.width = 100 * done / taskBoxes.length + '%');
  document.querySelectorAll('.progress-label').forEach(node => node.textContent = `${done} of ${taskBoxes.length} build tasks complete`);
}
function testStates() { return [...document.querySelectorAll('.status')].map(group => group.querySelector('button.active')?.dataset.v || 'not'); }
function gate() {
  const tasks = taskBoxes.map(box => box.checked);
  const tests = testStates();
  const controls = [...document.querySelectorAll('[data-gate]')].map(box => box.checked);
  const ready = SopGuideCore.readiness(tasks, tests, controls);
  const remaining = `${tasks.filter(Boolean).length}/${tasks.length} build tasks · ${tests.filter(value => value==='pass').length}/${tests.length} tests passed · ${controls.filter(Boolean).length}/${controls.length} controls confirmed`;
  el('gate').classList.toggle('ready',ready);
  el('gate').innerHTML = ready ? `<h3>Checklist complete — request owner validation</h3><p>${remaining}</p><p>These are your recorded checks, not independent approval. Confirm the evidence and local pilot decision before sharing.</p>` : `<h3>Release checklist incomplete</h3><p>${remaining}</p><p>Complete all tasks, pass every test and confirm every control. Unrun or failed tests prevent completion.</p>`;
}

const calculatorIds = ['minutes','cases','staff','weeks','realisation','build','maintenance'];
function calculatorInput() { return Object.fromEntries(calculatorIds.map(id => [id,el(id).value])); }
function calc() {
  const result = SopGuideCore.calculate(calculatorInput());
  el('calcError').textContent = result.valid ? '' : result.error;
  if (!result.valid) { ['weekly','monthly','annual','payback'].forEach(id => el(id).textContent='—'); return; }
  el('weekly').textContent = result.weekly.toFixed(2);
  el('monthly').textContent = result.monthly.toFixed(2);
  el('annual').textContent = result.annual.toFixed(2);
  el('payback').textContent = result.payback === null ? 'No positive payback' : result.payback.toFixed(2);
}
calculatorIds.forEach(id => {
  const saved = getState('calc-' + id);
  if (saved !== null) el(id).value=saved;
  el(id).addEventListener('input',() => { setState('calc-' + id,el(id).value); calc(); });
});
function resetGuide() {
  el('resetDialog').showModal();
}
el('confirmReset').addEventListener('click', () => {
  try { Object.keys(localStorage).filter(key => key.startsWith(prefix)).forEach(key => localStorage.removeItem(key)); } catch { storageWarning(); }
  memory.clear();
  location.reload();
});
function exportProgress() {
  const record = {guideVersion:guideData.version,configurationFingerprint:guideData.fingerprint,exportedAt:new Date().toISOString(),note:'Self-recorded checklist; not Copilot execution evidence or approval.',tasks:taskBoxes.map(box=>({task:box.closest('summary').textContent.trim(),complete:box.checked})),tests:guideData.tests.map((test,i)=>({id:test.id,name:test.name,result:testStates()[i]})),controls:[...document.querySelectorAll('[data-gate]')].map(box=>({control:box.parentElement.textContent.trim(),confirmed:box.checked})),calculator:calculatorInput()};
  const url = URL.createObjectURL(new Blob([JSON.stringify(record,null,2)],{type:'application/json'}));
  const link = document.createElement('a'); link.href=url; link.download='sop-bot-progress.json'; link.click();
  setTimeout(()=>URL.revokeObjectURL(url),1000);
}
let closedDetails = [];
window.addEventListener('beforeprint',() => { closedDetails=[...document.querySelectorAll('details:not([open])')]; closedDetails.forEach(node => node.open=true); });
window.addEventListener('afterprint',() => { closedDetails.forEach(node => node.open=false); closedDetails=[]; });
progress(); gate(); calc();
