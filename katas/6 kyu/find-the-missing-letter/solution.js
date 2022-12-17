// find-the-missing-letter
/* ------------------------------- MY SOLUTION ------------------------------ */
function findMissingLetter(arr)
{
  code = arr[0].charCodeAt(0) - 1

for (const c of arr) {
  code++
  if (c.charCodeAt(0) != code) return String.fromCharCode(code)
}

}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;
describe("KataTests", function(){
  it("exampleTests", function(){
    Test(findMissingLetter(['a','b','c','d','f']), 'e');
    Test(findMissingLetter(['O','Q','R','S']), 'P');
  });
});