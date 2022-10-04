// convert-a-string-to-a-number
/* ------------------------------- MY SOLUTION ------------------------------ */
const stringToNumber = function(str){
  return Number(str);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe( "stringToNumber", function(){
  it( "should work for the examples" , function(){
    Test(stringToNumber("1234"),1234)
    Test(stringToNumber("605"), 605)
    Test(stringToNumber("1405"),1405)
    Test(stringToNumber("-7"),  -7)
  });
});