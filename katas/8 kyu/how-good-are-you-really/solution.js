// how-good-are-you-really
/* ------------------------------- MY SOLUTION ------------------------------ */
function betterThanAverage(cp, yp) {
  avg_cp = cp.reduce((a,b)=>a+b)/cp.length
  return avg_cp >= yp ? false : true 
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function betterThanAverage(classPoints, yourPoints) {
  return yourPoints > classPoints.reduce((a, b) => a + b, 0) / classPoints.length; 
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require('chai');
const assert = chai.assert;

describe("Example Tests", function() {
  it("betterThanAverage([2, 3], 5) should return True", function() {
    assert.strictEqual(betterThanAverage([2, 3], 5), true);
  });
  
  it("betterThanAverage([100, 40, 34, 57, 29, 72, 57, 88], 75) should return True", function() {
    assert.strictEqual(betterThanAverage([100, 40, 34, 57, 29, 72, 57, 88], 75), true);
  });
  
  it("betterThanAverage([12, 23, 34, 45, 56, 67, 78, 89, 90], 9) should return False", function() {
    assert.strictEqual(betterThanAverage([12, 23, 34, 45, 56, 67, 78, 89, 90], 9), false);
  });
  
  it("betterThanAverage([41, 75, 72, 56, 80, 82, 81, 33], 50) should return False", function() {
    assert.strictEqual(betterThanAverage([41, 75, 72, 56, 80, 82, 81, 33], 50), false);
  });
  
  it("betterThanAverage([29, 55, 74, 60, 11, 90, 67, 28], 21) should return False", function() {
    assert.strictEqual(betterThanAverage([29, 55, 74, 60, 11, 90, 67, 28], 21), false);
  });
});