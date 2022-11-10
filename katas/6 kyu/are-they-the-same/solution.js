// are-they-the-same
/* ------------------------------- MY SOLUTION ------------------------------ */
function comp(array1, array2){
  return array1 && array2 !== null ? array1.map(x => x*x).sort().toString() === array2.sort().toString() : false
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function comp(array1, array2) {
  if(array1 == null || array2 == null) return false;
  array1.sort((a, b) => a - b); array2.sort((a, b) => a - b);
  return array1.map(v => v * v).every((v, i) => v == array2[i]);
}

function comp(a, b) {
  return !!a && !!b && a.map(x => x*x).sort().join() == b.sort().join();
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const { assert } = require('chai');

describe("Tests", () => {
  it("test", () => {
    let a1 = [121, 144, 19, 161, 19, 144, 19, 11];
    let a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19];
    assert.isTrue(comp(a1, a2));
  });
});