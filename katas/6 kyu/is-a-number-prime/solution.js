// is-a-number-prime
/* ------------------------------- MY SOLUTION ------------------------------ */
function isPrime(num) {
  if (num < 2) {
    return false;
  }
  if (num === 2) {
    return true;
  }
  
  const maximumDividor = Math.sqrt(num) + 1;
  for (let i = 2; i < maximumDividor; i++) {
    if (num % i === 0) {
      return false;
    }
  }
return true;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe("Basic", ()=>{
	
	it("Basic tests", () => {
		
		Test(isPrime(0),  false, "0 is not prime");
		Test(isPrime(1),  false, "1 is not prime");
		Test(isPrime(2),  true, "2 is prime");
		Test(isPrime(73), true, "73 is prime");
		Test(isPrime(75), false, "75 is not prime");
		Test(isPrime(-1), false, "-1 is not prime");
		
	});
	
	it("Test prime", () => {
		
		Test(isPrime(3),  true, "3 is prime");
		Test(isPrime(5),  true, "5 is prime");
		Test(isPrime(7),  true, "7 is prime");
		Test(isPrime(41), true, "41 is prime");
		Test(isPrime(5099), true, "5099 is prime");
		
	});
	
	it("Test not prime", () => {
		
		Test(isPrime(4),  false, "4 is not prime");
		Test(isPrime(6),  false, "6 is not prime");
		Test(isPrime(8),  false, "8 is not prime");
		Test(isPrime(9), false, "9 is not prime");
		Test(isPrime(45), false, "45 is not prime");
		Test(isPrime(-5), false, "-5 is not prime");
		Test(isPrime(-8), false, "-8 is not prime");
		Test(isPrime(-41), false, "-41 is not prime");
		
	});
});