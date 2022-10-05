// even-or-odd
/* ------------------------------- MY SOLUTION ------------------------------ */
function even_or_odd(number) {
  return number%2 == 0 ? 'Even' : 'Odd'
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require('chai');
const assert = chai.assert;

describe("Sample tests",() => {
  
  it("2 is even", () => {
    assert.strictEqual(even_or_odd(2), "Even");
  });
  it("7 is odd", () => {
    assert.strictEqual(even_or_odd(7), "Odd");
  });
  it("-42 is even", () => {
    assert.strictEqual(even_or_odd(-42), "Even");
  });
  it("-7 is odd", () => {
    assert.strictEqual(even_or_odd(-7), "Odd");
  });
  it("0 is even", () => {
    assert.strictEqual(even_or_odd(0), "Even");
  });
});