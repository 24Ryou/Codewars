// decode-the-morse-code
/* ------------------------------- MY SOLUTION ------------------------------ */
decodeMorse = function(inp){
  MORSE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
      '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
      '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
      '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
      '-.--': 'Y', '--..': 'Z',
      '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
      '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
      '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
      '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
      '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
      '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
  }
  
  inp = inp.trim()
  words = inp.split("   ")
  
  decodeWord =  function(word) {
    chars = word.split(" ")
    decodedWord = chars.map(x => MORSE[x]).join("")
    return decodedWord
  }
  
  return words.map(x => decodeWord(x)).join(" ")
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const { assert } = require('chai');

describe("Sample tests", function(){
  
  it("Example from description", () => {  
    assert.strictEqual(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE');
  });
  
  it("Leading and trailing spaces", () => {  
    assert.strictEqual(decodeMorse('   .... . -.--   '), 'HEY');
  });
  
});
