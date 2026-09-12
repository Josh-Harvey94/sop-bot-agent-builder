(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.SopGuideCore = factory();
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';
  function calculate(input) {
    const limits = {minutes:[0,Infinity],cases:[0,Infinity],staff:[1,Infinity],weeks:[1,52],realisation:[0,100],build:[0,Infinity],maintenance:[0,Infinity]};
    const value = {};
    for (const [key, [min, max]] of Object.entries(limits)) {
      const raw = input[key];
      if (raw === null || raw === undefined || String(raw).trim() === '') return {valid:false,error:'Complete every calculator field.'};
      value[key] = Number(raw);
      if (!Number.isFinite(value[key]) || value[key] < min || value[key] > max) return {valid:false,error:'Use non-negative values, staff multiplier at least 1, 1–52 active weeks and 0–100% realisation.'};
    }
    const weekly = value.minutes * value.cases * value.staff / 60 * value.realisation / 100;
    const annual = weekly * value.weeks - value.maintenance;
    const monthly = annual / 12;
    const payback = monthly > 0 ? value.build / monthly : null;
    if (![weekly, annual, monthly].every(Number.isFinite) || (payback !== null && !Number.isFinite(payback))) return {valid:false,error:'Values are too large to calculate. Use realistic planning inputs.'};
    return {valid:true,weekly,annual,monthly,payback};
  }
  function readiness(tasks, tests, controls) {
    return tasks.length > 0 && tests.length > 0 && controls.length > 0 &&
      tasks.every(value => value === true) && tests.every(value => value === 'pass') && controls.every(value => value === true);
  }
  return {calculate, readiness};
});
