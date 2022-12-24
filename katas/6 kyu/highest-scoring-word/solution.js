// highest-scoring-word
/* ------------------------------- MY SOLUTION ------------------------------ */
function high(s){
  alphabet = "abcdefghijklmnopqrstuvwxyz".split("")

  rule = {}

  for (let i = 0; i < 26; i++) {
    rule[alphabet[i]] = i+1
  }

  words = s.split(" ")

  wall = words.map(word => word.split("").map(letter => rule[letter]).reduce((a , b) => a+b , 0))
  return words[wall.indexOf(Math.max(...wall))]
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Basic tests", () => {
  it("Testing for fixed tests", () => {
    assert.strictEqual(high('man i need a taxi up to ubud'), 'taxi');
    assert.strictEqual(high('what time are we climbing up the volcano'), 'volcano'); 
    assert.strictEqual(high('take me to semynak'), 'semynak');   
    assert.strictEqual(high('aa b'), 'aa');
    assert.strictEqual(high('b aa'), 'b');
    assert.strictEqual(high('bb d'), 'bb');
    assert.strictEqual(high('d bb'), 'd');
    assert.strictEqual(high('aaa b'), 'aaa');
  })
});