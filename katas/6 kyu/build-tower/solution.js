// build-tower
/* ------------------------------- MY SOLUTION ------------------------------ */
function towerBuilder(n) {
  return Array.from({length: n}, function(v, k) {
    const spaces = ' '.repeat(n - k - 1);
    return spaces + '*'.repeat(k + k + 1) + spaces;
  });
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
Test(towerBuilder(1), ["*"]);
Test(towerBuilder(2), [" * ","***"]);
Test(towerBuilder(3), ["  *  "," *** ","*****"]);
  });
});
