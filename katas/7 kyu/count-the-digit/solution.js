// count-the-digit
/* ------------------------------- MY SOLUTION ------------------------------ */
function nbDig(n, d) {
  regex = new RegExp(`[${d}]` , 'g')
  return [...Array(n+1).keys()].map(x => x**2).join("").match(regex).length
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function nbDig(n, d) {
  var o = '';
    for(var i = 0; i <= n; i++){
      o += Math.pow(i, 2);
    }
  return o.split(d).length-1
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const assert = require('chai').assert;
describe("nbDig", () => {
  it("Basic tests", () => { 
    assert.strictEqual(nbDig( 5750, 0),  4700, "n = 5750, d = 0");
    assert.strictEqual(nbDig(11011, 2),  9481, "n = 11011, d = 2");
    assert.strictEqual(nbDig(12224, 8),  7733, "n = 12224, d = 8");
    assert.strictEqual(nbDig(11549, 1), 11905, "n = 11549, d = 1");
  });
});