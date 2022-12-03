// convert-string-to-camel-case
/* ------------------------------- MY SOLUTION ------------------------------ */
function toCamelCase(str){
  arr = str.split("")
  result = []
  var i = 0
  while (i < arr.length) {
    var element = arr[i];
    if (element === "_" || element === "-") {
      element = arr[i+1].toUpperCase()
      i++
    }
    result.push(element)
    i++
  }
  return result.join("")
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function toCamelCase(str){
  var regExp=/[-_]\w/ig;
  return str.replace(regExp,function(match){
    return match.charAt(1).toUpperCase();
  });
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const { assert } = require('chai');

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual(toCamelCase(''), '', "An empty string was provided but not returned")
    assert.strictEqual(toCamelCase("the_stealth_warrior"), "theStealthWarrior", "toCamelCase('the_stealth_warrior') did not return correct value")
    assert.strictEqual(toCamelCase("The-Stealth-Warrior"), "TheStealthWarrior", "toCamelCase('The-Stealth-Warrior') did not return correct value")
    assert.strictEqual(toCamelCase("A-B-C"), "ABC", "toCamelCase('A-B-C') did not return correct value")
  });
});
