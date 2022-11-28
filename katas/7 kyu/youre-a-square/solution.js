// youre-a-square
/* ------------------------------- MY SOLUTION ------------------------------ */
var isSquare = function(n){
  return Math.floor(n ** 0.5) ** 2 == n;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("isSquare", function(){
  it("should work for some examples", function(){
    Test(isSquare(-1), false, "-1: Negative numbers cannot be square numbers");
    Test(isSquare( 0), true, "0 is a square number (0 * 0)");
    Test(isSquare( 3), false, "3 is not a square number");
    Test(isSquare( 4), true, "4 is a square number (2 * 2)");
    Test(isSquare(25), true, "25 is a square number (5 * 5)");
    Test(isSquare(21), false, "26 is not a square number");
  });
});