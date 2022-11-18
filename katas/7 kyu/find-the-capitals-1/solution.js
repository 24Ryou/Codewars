// find-the-capitals-1
/* ------------------------------- MY SOLUTION ------------------------------ */
var capitals = function (word) {
  arr = []
	for (const [index, element] of word.split("").entries()) {
    if (element === element.toUpperCase()) arr.push(index);
  }
  return arr
};
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
var capitals = function (word) {
  var caps = [];
  for(var i = 0; i < word.length; i++) {
    if(word[i].toUpperCase() == word[i]) caps.push(i);
  }
  return caps;
};
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {
    assert.deepEqual(capitals('CodEWaRs'), [0,3,4,6] );
  });
});