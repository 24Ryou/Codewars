// find-the-unique-number-1
/* ------------------------------- MY SOLUTION ------------------------------ */
function findUniq(arr) {
  arr.sort((a , b) => b -a)
  if (arr[2] != arr[0]) return arr[0]
  return arr[arr.length-1]
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function findUniq(arr) {
  arr.sort((a,b)=>a-b);
  return arr[0]==arr[1]?arr.pop():arr[0]
}

function findUniq(arr) {
  return arr.find(n => arr.indexOf(n) === arr.lastIndexOf(n));
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold = 0;

describe("Example Tests", () => {
  it("Tests", () => {
    assert.strictEqual(findUniq([ 1, 0, 0 ]), 1);
    assert.strictEqual(findUniq([ 0, 1, 0 ]), 1);
    assert.strictEqual(findUniq([ 0, 0, 1 ]), 1);
    assert.strictEqual(findUniq([ 1, 1, 1, 2, 1, 1 ]), 2);
    assert.strictEqual(findUniq([ 1, 1, 2, 1, 1 ]), 2);
    assert.strictEqual(findUniq([ 3, 10, 3, 3, 3 ]), 10);
  });
});
