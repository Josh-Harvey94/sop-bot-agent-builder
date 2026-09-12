const test = require('node:test');
const assert = require('node:assert/strict');
const {calculate, readiness} = require('../scripts/guide-core.js');
const baseline = {minutes:5,cases:40,staff:1,weeks:46,realisation:70,build:16,maintenance:12};
const near = (value,expected) => assert.ok(Math.abs(value-expected)<1e-9, `${value} != ${expected}`);

test('capacity matches the independent worked example and deducts annual maintenance once', () => {
  const value=calculate(baseline);
  assert.equal(value.valid,true);
  near(value.weekly,7/3); near(value.annual,286/3); near(value.monthly,143/18); near(value.payback,288/143);
});
test('source-guide inputs remain compatible when maintenance is zero', () => {
  const value=calculate({...baseline,maintenance:0});
  near(value.annual,322/3); near(value.monthly,161/18);
});
test('zero and negative net benefit never produce a numeric payback', () => {
  const zero=calculate({...baseline,minutes:0,maintenance:0});
  assert.equal(zero.annual,0); assert.equal(zero.payback,null);
  const negative=calculate({minutes:1,cases:1,staff:1,weeks:10,realisation:100,build:8,maintenance:1});
  near(negative.annual,-5/6); assert.equal(negative.payback,null);
});
test('zero build effort with positive benefit has immediate payback', () => assert.equal(calculate({...baseline,build:0}).payback,0));
test('blank, invalid, infinite, negative and out-of-range entries are rejected', () => {
  for (const change of [{minutes:''},{minutes:'not a number'},{minutes:-1},{weeks:53},{weeks:0},{realisation:101},{realisation:-1},{staff:0},{maintenance:-1},{build:Infinity},{minutes:null},{minutes:1e308,cases:1e308}]) {
    assert.equal(calculate({...baseline,...change}).valid,false,JSON.stringify(change));
  }
});
test('all controls ticked is insufficient while any test is unrun or failed', () => {
  assert.equal(readiness([true,true],['pass','not'],[true,true]),false);
  assert.equal(readiness([true,true],['pass','fix'],[true,true]),false);
});
test('readiness requires every build task and every control', () => {
  assert.equal(readiness([true,false],['pass','pass'],[true,true]),false);
  assert.equal(readiness([true,true],['pass','pass'],[true,false]),false);
  assert.equal(readiness([true,true],['pass','pass'],[true,true]),true);
});
test('empty or malformed collections cannot claim readiness', () => {
  assert.equal(readiness([],[],[]),false);
  assert.equal(readiness([true],[],[true]),false);
  assert.equal(readiness([true],['pass'],[]),false);
  assert.equal(readiness(['true'],['pass'],[true]),false);
});
