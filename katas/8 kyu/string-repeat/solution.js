// string-repeat
/* ------------------------------- MY SOLUTION ------------------------------ */
function repeatStr (n, s) {
  return s.repeat(n)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("Tests", function() {
  it ("Basic tests", function() {
    Test(repeatStr(3, "*"), "***");
    Test(repeatStr(5, "#"), "#####");
    Test(repeatStr(2, "ha "), "ha ha ");
  });
});