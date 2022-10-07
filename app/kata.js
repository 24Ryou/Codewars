// grasshopper-personalized-message
/* ------------------------------- MY SOLUTION ------------------------------ */
function greet (name, owner) {
  return name == owner ? 'Hello boss' : 'Hello guest'
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
Test(greet('Daniel', 'Daniel'), 'Hello boss')
Test(greet('Greg', 'Daniel'), 'Hello guest')
  });
});
