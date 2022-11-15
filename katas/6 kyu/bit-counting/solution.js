// bit-counting
/* ------------------------------- MY SOLUTION ------------------------------ */
var countBits = function(n) {
  return n.toString(2).split("").filter(x => x === '1').length
};
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
var countBits = function(n)
{
  return (n.toString(2).match(/1/g) || []).length;
};
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const { assert } = require("chai")

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {
    assert.strictEqual(countBits(0), 0);
    assert.strictEqual(countBits(4), 1);
    assert.strictEqual(countBits(7), 3);
    assert.strictEqual(countBits(9), 2);
    assert.strictEqual(countBits(10), 2);
    })
  })