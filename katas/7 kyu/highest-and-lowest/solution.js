// highest-and-lowest
/* ------------------------------- MY SOLUTION ------------------------------ */
function highAndLow(numbers){
  numbers = numbers.split(" ")
  low = high = parseInt(numbers[0])
  numbers.forEach(element => {
    if (parseInt(element) > high) high = element
    if (parseInt(element) < low ) low  = element
  });
  return high + " " + low
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function highAndLow(numbers){
  numbers = numbers.split(' ').map(Number);
  return `${Math.max(...numbers)} ${Math.min(...numbers)}`;
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Example tests", () => {
  it("Test 1", () => {
    assert.strictEqual(highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9");
  });
  it("Test 2", () => {
    assert.strictEqual(highAndLow("1 2 3"), "3 1");
  });
});