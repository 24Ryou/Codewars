// grasshopper-terminal-game-combat-function-1
/* ------------------------------- MY SOLUTION ------------------------------ */
function combat(health, damage) {
  return damage > health ? 0 : health - damage
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("The combat() function", function () {
  it("should work for some example tests", function () {
    Test(combat(100, 5), 95);
    Test(combat(92, 8), 84);
    Test(combat(20, 30), 0, "Health cannot go below 0");
  });
});