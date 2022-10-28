// regex-validate-pin-code
/* ------------------------------- MY SOLUTION ------------------------------ */
function validatePIN (pin) {
  return /^(\d{4}|\d{6})$/.test(pin)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;


describe("validatePIN", function() {
  it("should return False for pins with length other than 4 or 6", function() {
    Test(validatePIN("1"),false, "Wrong output for '1'")
    Test(validatePIN("12"),false, "Wrong output for '12'")
    Test(validatePIN("123"),false, "Wrong output for '123'")
    Test(validatePIN("12345"),false, "Wrong output for '12345'")
    Test(validatePIN("1234567"),false, "Wrong output for '1234567'")
    Test(validatePIN("-1234"),false, "Wrong output for '-1234'")
    Test(validatePIN("1.234"),false, "Wrong output for '1.234'")
    Test(validatePIN("-1.234"),false, "Wrong output for '-1.234'")
    Test(validatePIN("00000000"),false, "Wrong output for '00000000'")
  });
  
  it("should return False for pins which contain characters other than digits", function() {
    Test(validatePIN("a234"),false, "Wrong output for 'a234'")
    Test(validatePIN(".234"),false, "Wrong output for '.234'")
  });
  
  it("should return True for valid pins", function() {
    Test(validatePIN("1234"),true, "Wrong output for '1234'");
    Test(validatePIN("0000"),true, "Wrong output for '0000'");
    Test(validatePIN("1111"),true, "Wrong output for '1111'");
    Test(validatePIN("123456"),true, "Wrong output for '123456'");
    Test(validatePIN("098765"),true, "Wrong output for '098765'");
    Test(validatePIN("000000"),true, "Wrong output for '000000'");
    Test(validatePIN("123456"),true, "Wrong output for '123456'");
    Test(validatePIN("090909"),true, "Wrong output for '090909'");
  });
});
