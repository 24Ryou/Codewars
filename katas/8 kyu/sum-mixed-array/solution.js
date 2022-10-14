// sum-mixed-array
/* ------------------------------- MY SOLUTION ------------------------------ */
function sumMix(x){
  return x.reduce((a, b) => Number(a) + Number(b), 0)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function sumMix(x){
  return x.map(a => +a).reduce((a, b) => a + b);
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
    assert.strictEqual(sumMix([9, 3, '7', '3']), 22);
    assert.strictEqual(sumMix(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 42); 
    assert.strictEqual(sumMix(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 41); 
  })
});