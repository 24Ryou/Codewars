// fake-binary
/* ------------------------------- MY SOLUTION ------------------------------ */
function fakeBin(x){
  return x.split("").map(i => i < 5 ? '0' : '1').join("")
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function fakeBin(x) {
  return x.replace(/\d/g, d => d < 5 ? 0 : 1);
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests",() =>{
  it("Testing for fixed tests", () => {
    assert.strictEqual(fakeBin('45385593107843568'), '01011110001100111');
    assert.strictEqual(fakeBin('509321967506747'), '101000111101101'); 
    assert.strictEqual(fakeBin('366058562030849490134388085'), '011011110000101010000011011');
  })
});