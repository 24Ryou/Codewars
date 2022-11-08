// two-to-one
/* ------------------------------- MY SOLUTION ------------------------------ */
function longest(s1, s2) {
  s = (s1 + s2).split("")
  return s.filter((v, i, a) => a.indexOf(v) === i).sort().join("")
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
const longest = (s1, s2) => [...new Set(s1+s2)].sort().join('')
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("longest",function() {
  it("Basic tests",function() {
      Test(longest("aretheyhere", "yestheyarehere"), "aehrsty")
      Test(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
      Test(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
  })})