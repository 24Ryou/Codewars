// printer-errors
/* ------------------------------- MY SOLUTION ------------------------------ */
function printerError(s) {
  codes = "abcdefghijklm".split("")
  cnt = s.split("").filter(x => !codes.includes(x))
  return `${cnt.length}/${s.length}`
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function printerError(s) {
  var count = 0;
  for(var i = 0; i < s.length; i++) {
    if (s[i] > "m") {
      count++;
    }
  }
  return count+"/"+s.length;
}
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("printerError",function() {
it("Basic tests",function() {   
    var s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    Test(printerError(s), "3/56")
    var x="kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    Test(printerError(x), "6/60")
})})