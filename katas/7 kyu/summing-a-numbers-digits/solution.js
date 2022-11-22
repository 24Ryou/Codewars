// summing-a-numbers-digits
/* ------------------------------- MY SOLUTION ------------------------------ */
function sumDigits(number) {
  return ("" + Math.abs(number)).split("").reduce((a , b) => Number(a) + Number(b) , 0)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const { assert } = require("chai")

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {
    assert.strictEqual(sumDigits(10), 1);
    assert.strictEqual(sumDigits(99), 18);
    assert.strictEqual(sumDigits(-32), 5);
    })
  })