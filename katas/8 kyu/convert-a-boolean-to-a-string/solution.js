// convert-a-boolean-to-a-string
/* ------------------------------- MY SOLUTION ------------------------------ */
function booleanToString(b){
  return String(b)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function booleanToString(b){
  return b.toString();
}
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual;
chai.config.truncateThreshold=0;


describe("Tests", () => {
  it("test", () => {
Test(booleanToString(true), "true", 'When we pass in true, we want the string "true" as output');
Test(booleanToString(false), "false", 'When we pass in false, we want the string "false" as output');
  });
});
