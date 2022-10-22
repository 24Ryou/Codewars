// convert-number-to-reversed-array-of-digits
/* ------------------------------- MY SOLUTION ------------------------------ */
function digitize(n) {
  return (""+n).split("").reverse().map(x => parseInt(x))
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function digitize(n) {
  return String(n).split('').map(Number).reverse()
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
    assert.deepEqual(digitize(35231),[1,3,2,5,3]);
    assert.deepEqual(digitize(0),[0]);
  });
});
