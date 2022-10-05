// counting-sheep-dot-dot-dot
/* ------------------------------- MY SOLUTION ------------------------------ */
function countSheeps(arrayOfSheep) {
  return arrayOfSheep.filter(Boolean).length
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
var array1 = [true,  true,  true,  false,
              true,  true,  true,  true ,
              true,  false, true,  false,
              true,  false, false, true ,
              true,  true,  true,  true ,
              false, false, true,  true ];
              
Test(countSheeps(array1), 17, "There are 17 sheeps in total")
  });
});
