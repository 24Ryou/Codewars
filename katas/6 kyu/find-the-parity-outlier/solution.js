// find-the-parity-outlier
/* ------------------------------- MY SOLUTION ------------------------------ */
function findOutlier(integers){
  let oddArr =[];
  let evenArr = [];

  for(let i = 0; i< integers.length; i++){
    if(integers[i] % 2 === 0){
      evenArr.push(integers[i]);
    }else{
      oddArr.push(integers[i]);
    }
  }

  if(evenArr.length == 1){
    return evenArr[0];
  }else{
    return oddArr[0];
  }
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;


describe("Tests", () => {
  it("test", () => {
    Test(findOutlier([0, 1, 2]), 1)
    Test(findOutlier([1, 2, 3]), 2)
    Test(findOutlier([2,6,8,10,3]), 3)
    Test(findOutlier([0,0,3,0,0]), 3)
    Test(findOutlier([1,1,0,1,1]), 0)
  });
});
