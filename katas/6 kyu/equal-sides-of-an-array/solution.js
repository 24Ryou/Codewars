// equal-sides-of-an-array
/* ------------------------------- MY SOLUTION ------------------------------ */
function findEvenIndex(arr)
{
  for (let x = 0; x < arr.length; x++) {
    sum = function (arr) {return arr.reduce((a , b) => a+b , 0)}
    left = sum(arr.slice(0 , x))
    right = sum(arr.slice(x+1))
    if (left == right) return x
  }
  return -1
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;
describe("FindEvenIndex", function() {
  it("Tests", function() {
    Test(findEvenIndex([1,2,3,4,3,2,1]),3, "The array was: [1,2,3,4,3,2,1] \n");
    Test(findEvenIndex([1,100,50,-51,1,1]),1, "The array was: [1,100,50,-51,1,1] \n");
    Test(findEvenIndex([1,2,3,4,5,6]),-1, "The array was: [1,2,3,4,5,6] \n");
    Test(findEvenIndex([20,10,30,10,10,15,35]),3, "The array was: [20,10,30,10,10,15,35] \n");
  });
});