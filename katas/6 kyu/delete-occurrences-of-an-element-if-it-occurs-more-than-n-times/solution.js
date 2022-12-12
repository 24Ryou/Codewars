// delete-occurrences-of-an-element-if-it-occurs-more-than-n-times
/* ------------------------------- MY SOLUTION ------------------------------ */
function deleteNth(arr,n){
  out = []
  for (const x of arr) {
  cnt = out.filter(y => y === x).length
    if (cnt < n) out.push(x)
  }
  return out
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function deleteNth(arr,x) {
  var cache = {};
  return arr.filter(function(n) {
    cache[n] = (cache[n]||0) + 1;
    return cache[n] <= x;
  });
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const { assert } = require('chai');

describe("Tests", () => {
  it("test", () => {
    assert.sameOrderedMembers(deleteNth([20,37,20,21], 1), [20,37,21])
    assert.sameOrderedMembers(deleteNth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
  });
});
