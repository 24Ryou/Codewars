// reversed-sequence
/* ------------------------------- MY SOLUTION ------------------------------ */
const reverseSeq = n => {
  return [...Array(n).keys()].map(i => i+1).reverse();
};
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
const reverseSeq = n => {
  return Array(n).fill(0).map((e, i) => n - i );
};

const reverseSeq = n => {
  let arr = [];
    for (let i=n; i>0; i--) {
    arr.push(i);
    } return arr;
};
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("reverseSeq", function() {
  it("Sample Test", function() {
    assert.deepEqual(reverseSeq(5), [5, 4, 3, 2, 1]);
  });
});