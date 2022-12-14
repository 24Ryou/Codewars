// does-my-number-look-big-in-this
/* ------------------------------- MY SOLUTION ------------------------------ */
function narcissistic(value) {
  a = value.toString().split("")
  k = a.length
  out = 0
  for (const x of a) {
    out += x ** k
  }
  return out == value
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;
describe( "Narcissistic Function", function() {
  it( "should find small numbers are all narcissistic", function() {
    Test(narcissistic( 7 ), true, "7 is narcissistic" );
  });
  
  it( "should find these numbers are narcissistic", function() {
    Test(narcissistic( 371 ), true, "371 is narcissistic" );
  });
});
