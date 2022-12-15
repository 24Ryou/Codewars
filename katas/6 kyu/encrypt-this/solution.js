// encrypt-this
/* ------------------------------- MY SOLUTION ------------------------------ */
const encryptThis = text => {
  return text
    .split(' ')
    .map(e => {
      if (e.length === 1) return e.charCodeAt(0);
      if (e.length === 2) return `${e[0].charCodeAt(0)}${e[1]}`;
      if (e.length === 3) return `${e[0].charCodeAt(0)}${e.slice(-1)}${e[1]}`;
      if (e.length > 3) return `${e[0].charCodeAt(0)}${e.slice(-1)}${e.slice(2, -1)}${e[1]}`;
    })
    .join(' ');
};
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const assert = require("chai").assert;

describe("Fixed Tests", function() {
  it("should work with fixed tests", function() {
    assert.strictEqual(encryptThis("A"), "65");
    assert.strictEqual(encryptThis("A wise old owl lived in an oak"), "65 119esi 111dl 111lw 108dvei 105n 97n 111ka");
    assert.strictEqual(encryptThis("The more he saw the less he spoke"), "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp");
    assert.strictEqual(encryptThis("The less he spoke the more he heard"), "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare");
    assert.strictEqual(encryptThis("Why can we not all be like that wise old bird"), "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri");
    assert.strictEqual(encryptThis("Thank you Piotr for all your help"), "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple");    
  });
});