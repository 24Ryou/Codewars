// vowel-count
/* ------------------------------- MY SOLUTION ------------------------------ */
function getCount(str) {
  return str.split("").filter(x => "aeiou".includes(x)).length;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function getCount(str) {
  return (str.match(/[aeiou]/ig)||[]).length;
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const {assert} = require("chai");

describe("Vowels Count Tests",function(){
  it("should return 5 for 'abracadabra'",function(){
    assert.strictEqual(getCount("abracadabra"), 5) ;
  });
});