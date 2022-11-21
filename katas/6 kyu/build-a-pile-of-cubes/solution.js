// build-a-pile-of-cubes
/* ------------------------------- MY SOLUTION ------------------------------ */
function findNb(m) {
  total = 0
  n = 0

  while (total < m ){
    n = n+1
    total = total + n ** 3
  }
  return total == m ? n : -1;
}

/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const { assert } = require('chai');

it("Basic tests",function() {
  assert.strictEqual(findNb(4183059834009), 2022)
  assert.strictEqual(findNb(24723578342962), -1)
  assert.strictEqual(findNb(135440716410000), 4824)
  assert.strictEqual(findNb(40539911473216), 3568)
})
