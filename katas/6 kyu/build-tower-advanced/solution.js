// build-tower-advanced
/* ------------------------------- MY SOLUTION ------------------------------ */
function towerBuilder(nFloors, nBlockSz) {
  const w = nBlockSz[0], h = nBlockSz[1];
  const tower = [];
  
  for (let floor = 1; floor <= nFloors; floor++) {
    let stars = '*'.repeat(w * (floor * 2 - 1));
    let space = ' '.repeat(w * (nFloors - floor));
    for (let i = 0; i < h; i++) {
      tower.push(space + stars + space);
    }
  }
  
  return tower;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
Test(JSON.stringify(towerBuilder(1, [1, 1])), JSON.stringify(["*"]));
Test(JSON.stringify(towerBuilder(3, [4, 2])), JSON.stringify(['        ****        ', '        ****        ', '    ************    ', '    ************    ', '********************', '********************']));
  });
});