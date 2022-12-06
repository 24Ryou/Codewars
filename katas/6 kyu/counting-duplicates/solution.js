// counting-duplicates
/* ------------------------------- MY SOLUTION ------------------------------ */
function duplicateCount(text){
  counts = {}
  for (const x of text.toLowerCase().split("")) {
    counts[x] = counts[x] ? counts[x] + 1 : 1
  }
  arr = Object.entries(counts)
  return arr.filter(([key , value]) => value > 1).length
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function duplicateCount(text){
  return (text.toLowerCase().split('').sort().join('').match(/([^])\1+/g) || []).length;
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const { assert } = require('chai');

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual(duplicateCount(""), 0);
    assert.strictEqual(duplicateCount("abcde"), 0);
    assert.strictEqual(duplicateCount("aabbcde"), 2);
    assert.strictEqual(duplicateCount("aabBcde"), 2,"should ignore case");
    assert.strictEqual(duplicateCount("Indivisibility"), 1)
    assert.strictEqual(duplicateCount("Indivisibilities"), 2, "characters may not be adjacent")
  });
});
