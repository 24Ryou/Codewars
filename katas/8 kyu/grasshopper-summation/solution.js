// grasshopper-summation
/* ------------------------------- MY SOLUTION ------------------------------ */
var summation = function (num) {
  return [...Array(num).keys()].map(x => ++x).reduce((a, b) => a+b , 0)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
const summation = n => n * (n + 1) / 2;
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe('summation', function () {
  it('should return the correct total', function () {
    Test(summation(1), 1)
    Test(summation(8), 36)
  })
})
