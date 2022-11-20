// break-camelcase
/* ------------------------------- MY SOLUTION ------------------------------ */
function solution(string) {
  return string.split("").map(x => x === x.toUpperCase() ? ` ${x}` : x ).join("")
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function solution(string) {
  return(string.replace(/([A-Z])/g, ' $1'));
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const chai = require("chai");
const assert = chai.assert;

describe("Sample Tests", () => {
  it("Should pass sample tests", () => {
    assert.strictEqual(solution('camelCasing'), 'camel Casing', 'Unexpected result')
    assert.strictEqual(solution('camelCasingTest'), 'camel Casing Test', 'Unexpected result')
  });
});