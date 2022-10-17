// beginner-series-number-3-sum-of-numbers
/* ------------------------------- MY SOLUTION ------------------------------ */
function getSum( a,b )
{
  if (a == b) return a
  if (b < a) arr = [...Array(a-b+1).keys()].map(x => a-x)
  else arr = [...Array(b-a+1).keys()].map(x => a+x)
  return arr.reduce((a, b) => a+b , 0)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
const GetSum = (a, b) => {
  let min = Math.min(a, b),
      max = Math.max(a, b);
  return (max - min + 1) * (min + max) / 2;
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {         
    assert.strictEqual(getSum(0,-1),-1);
    assert.strictEqual(getSum(0,1),1);
  })
});