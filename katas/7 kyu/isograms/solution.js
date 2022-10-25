// isograms
/* ------------------------------- MY SOLUTION ------------------------------ */
function isIsogram(str){
  arr = str.toLowerCase().split("")
  const occurrences = arr.reduce(function (key, value) {
    return key[value] ? ++key[value] : key[value] = 1, key
  }, {});
  return Object.values(occurrences).reduce((a , b) => a + b , 0) == Object.values(occurrences).length
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function isIsogram(str){ 
  return !/(\w).*\1/i.test(str)
}

function isIsogram(str){
  return new Set(str.toUpperCase()).size == str.length;
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
    assert.strictEqual( isIsogram("Dermatoglyphics"), true );
    assert.strictEqual( isIsogram("isogram"), true );
    assert.strictEqual( isIsogram("aba"), false, "same chars may not be adjacent" );
    assert.strictEqual( isIsogram("moOse"), false, "same chars may not be same case" );
    assert.strictEqual( isIsogram("isIsogram"), false );
    assert.strictEqual( isIsogram(""), true, "an empty string is a valid isogram" );
  });
});
