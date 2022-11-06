// sort-array-by-string-length
/* ------------------------------- MY SOLUTION ------------------------------ */
function sortByLength (array) {
  return array.sort((a , b) => a.length - b.length)
};
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

// this test is not update base on chai method use the online tester!
// // const Test = require('@codewars/test-compat');

// describe("Example tests",function(){
//   it("Test 1",function(){
//     Test(sortByLength(["Beg", "Life", "I", "To"]),["I", "To", "Beg", "Life"]);
//   });
//   it("Test 2",function(){
//     Test(sortByLength(["", "Moderately", "Brains", "Pizza"]),["", "Pizza", "Brains", "Moderately"]);
//   });
//   it("Test 3",function(){
//     Test(sortByLength(["Longer", "Longest", "Short"]),["Short", "Longer", "Longest"]);
//   });
// });