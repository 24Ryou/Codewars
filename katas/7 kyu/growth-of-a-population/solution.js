// growth-of-a-population
/* ------------------------------- MY SOLUTION ------------------------------ */
function nbYear(p0, percent, aug, p) {
  years = 0
  while (p0 < p) {
    years += 1
    p0 += parseInt(p0 * percent/100) + aug // parseInt or Math.floor
  }
  return years
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("nbYear",function() {
  it("Basic tests",function() {    
      Test(nbYear(1500, 5, 100, 5000), 15);
      Test(nbYear(1500000, 2.5, 10000, 2000000), 10);
      Test(nbYear(1500000, 0.25, 1000, 2000000), 94);
  })})