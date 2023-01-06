// playing-with-digits
/* ------------------------------- MY SOLUTION ------------------------------ */
function digPow(n, p){
  arr = n.toString().split("").map((v , k) => v ** (p + k))
  sumArr = arr.reduce((a , b) => a + b , 0) 
  k = sumArr / n
  if (!Number.isInteger(k)) return -1
  return k
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;
describe("Tests", () => {
  it("test", () => {
Test(digPow(89, 1), 1)
Test(digPow(92, 1), -1)
Test(digPow(46288, 3), 51)

  });
});