// persistent-bugger
/* ------------------------------- MY SOLUTION ------------------------------ */
function persistence(x) {
  str = (a) => {
    return a.toString().split("")
  } 
  
  c = 0
  
  while (str(x).length > 1) {
    c++
    x = str(x).reduce((a,b) => a * b , 1)
  }
  return c  
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Persistent Bugger.", () => {
  it("Fixed tests", () => {
    assert.strictEqual(persistence(39),3);
    assert.strictEqual(persistence(4),0);
    assert.strictEqual(persistence(25),2);
    assert.strictEqual(persistence(999),4);
  });
});