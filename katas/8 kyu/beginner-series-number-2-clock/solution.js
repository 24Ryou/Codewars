// beginner-series-number-2-clock
/* ------------------------------- MY SOLUTION ------------------------------ */
function past(h, m, s){
  return (h*3600 + m*60 + s) * 1000
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const { assert } = require('chai');

describe("Fixed Tests", () => {
  it("Tests", () => {
    assert.strictEqual(past(0,1,1),61000)
    assert.strictEqual(past(1,1,1),3661000)
    assert.strictEqual(past(0,0,0),0)
    assert.strictEqual(past(1,0,1),3601000)
    assert.strictEqual(past(1,0,0),3600000)
  });
});