// beginner-series-number-1-school-paperwork
/* ------------------------------- MY SOLUTION ------------------------------ */
function paperwork(n, m) {
  if (n > 0 && m > 0) {
    return n*m
  }
  else return 0
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function paperwork(n, m) {
  return n > 0 && m > 0 ? n * m : 0
}
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Simple Tests", function(){
  it("Testing for fixed tests", () => {
    assert.strictEqual(paperwork(5,5), 25, 'Failed at paperwork(5, 5)');
    assert.strictEqual(paperwork(5,-5), 0, 'Failed at paperwork(5, -5)');
    assert.strictEqual(paperwork(-5,-5), 0, 'Failed at paperwork(-5, -5)');
    assert.strictEqual(paperwork(-5,5), 0, 'Failed at paperwork(-5, 5)');
    assert.strictEqual(paperwork(5,0), 0, 'Failed at paperwork(5, 0)');
  });
});
