// count-the-smiley-faces
/* ------------------------------- MY SOLUTION ------------------------------ */
function countSmileys(arr) {
  cnt = 0
  for (const x of arr) {
    if ( x.match(/[:;][-~]?[)D]/g) != null) cnt++ 
  }
  return cnt
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function countSmileys(arr) {
  return arr.filter(x => /^[:;][-~]?[)D]$/.test(x)).length;
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const { assert } = require('chai');

describe("Basic testing", function() {
  it("Example tests", () => {
    assert.strictEqual(countSmileys([]                             ), 0);
    assert.strictEqual(countSmileys([':D',':~)',';~D',':)']        ), 4);
    assert.strictEqual(countSmileys([':)',':(',':D',':O',':;']     ), 2);
    assert.strictEqual(countSmileys([';]', ':[', ';*', ':$', ';-D']), 1);
  });
});