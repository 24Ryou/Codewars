// exclusive-or-xor-logical-operator
/* ------------------------------- MY SOLUTION ------------------------------ */
function xor(a, b) {
  return a != b
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;
describe("Your 'xor' function/operator", () => {
  it("should work for the four basic cases described above", () => {
    Test(xor(false, false), false, "false xor false === false");
    Test(xor(true, false), true, "true xor false === true");
    Test(xor(false, true), true, "false xor true === true");
    Test(xor(true, true), false, "true xor true === false");
    Test(xor(true, true), false, "'xor' is NOT identical to 'or'");
  });
});