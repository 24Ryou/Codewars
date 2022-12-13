// detect-pangram
/* ------------------------------- MY SOLUTION ------------------------------ */
function isPangram(string){
  inp = string.toLowerCase()

  alphabet = "abcdefghijklmnopqrstuvwxyz".split("")

  cnt = 0

  for (const letter of alphabet) {
    if (inp.includes(letter)) cnt++  
  }

  return cnt === alphabet.length ? true : false
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function isPangram(string){
  string = string.toLowerCase();
  return "abcdefghijklmnopqrstuvwxyz".split("").every(function(x){
    return string.indexOf(x) !== -1;
  });
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test1", () => {
    var string = "The quick brown fox jumps over the lazy dog."
    assert.strictEqual(isPangram(string), true)
  })
  it("test2", () => {
    var string = "This is not a pangram."
    assert.strictEqual(isPangram(string), false)
  });
});