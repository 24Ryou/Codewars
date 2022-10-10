// return-negative
/* ------------------------------- MY SOLUTION ------------------------------ */
function makeNegative(num) {
  return -Math.abs(num)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;
describe("Tests", () => {
  it("test", () => {
Test(makeNegative(42), -42);
  });
});
