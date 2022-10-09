// invert-values
/* ------------------------------- MY SOLUTION ------------------------------ */
function invert(array) {
  return array.map(x => -x)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Invert array values",() => {
  it("Basic Tests", () => {
    assert.deepEqual(invert([1,2,3,4,5]), [-1,-2,-3,-4,-5]);
    assert.deepEqual(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5]);
    assert.deepEqual(invert([]), []);
    assert.deepEqual(invert([0]), [-0]);
  });
});