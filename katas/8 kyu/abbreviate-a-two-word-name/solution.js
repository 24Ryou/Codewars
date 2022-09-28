// abbreviate-a-two-word-name
/* ------------------------------- MY SOLUTION ------------------------------ */
function abbrevName(name){
  arr = name.split(" ")
  r = []
  for (word of arr) {
    lower = word.toLowerCase()
    r.push(word.charAt(0).toUpperCase())
  }
  return r.join('.')
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function abbrevName(name){
  return name.split(' ').map(i => i[0].toUpperCase()).join('.')
}
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {
    assert.strictEqual(abbrevName("Sam Harris"), "S.H");
    assert.strictEqual(abbrevName("Patrick Feenan"), "P.F");
    assert.strictEqual(abbrevName("Evan Cole"), "E.C");
    assert.strictEqual(abbrevName("P Favuzzi"), "P.F");
    assert.strictEqual(abbrevName("David Mendieta"), "D.M");
  });
});