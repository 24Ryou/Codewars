// binary-addition
/* ------------------------------- MY SOLUTION ------------------------------ */
function addBinary(a,b) {
  return (a+b).toString(2)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

// const Test = require('@codewars/test-compat');

describe("addBinary(1,2)", function() {
  var results1 = addBinary(1,2);
  it("Should return \"11\"", function() {
    Test(results1, "11");
  });
});