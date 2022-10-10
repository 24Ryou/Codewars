// opposites-attract
/* ------------------------------- MY SOLUTION ------------------------------ */
function lovefunc(flower1, flower2){
  return flower1 % 2 !== flower2 % 2 ? true : false
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function lovefunc(flower1, flower2){
  return flower1 % 2 !== flower2 % 2;
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
    assert.strictEqual(lovefunc(1,4), true)
    assert.strictEqual(lovefunc(2,2), false)
    assert.strictEqual(lovefunc(0,1), true)
    assert.strictEqual(lovefunc(0,0), false)
  });
});