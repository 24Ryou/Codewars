// count-characters-in-your-string
/* ------------------------------- MY SOLUTION ------------------------------ */
function count (string) {  
  res = {}
  for (const item of string.split("")) {
    if (item != " ") {
      res[item] = res[item] ? res[item] + 1 : 1
    }
  }
  return res
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("should pass sample tests", () => {
    assert.deepEqual(count("aba"), { a: 2, b: 1 }); 
    assert.deepEqual(count(""), {});    
  });
});