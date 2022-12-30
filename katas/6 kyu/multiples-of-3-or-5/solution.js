// multiples-of-3-or-5
/* ------------------------------- MY SOLUTION ------------------------------ */
function solution(number){
  if (number <= 0) return 0
  arr = []
  for (const x of [...Array(number).keys()]) {
    if (x % 3 == 0 || x % 5 == 0)
    arr.push(x)
  }
  return arr.reduce((a,b) => a+b , 0)
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const { assert } = require("chai")

function test(n, expected) {
  it(`n=${n}`, () => {  
    let actual = solution(n)
    assert.strictEqual(actual, expected)
  })
}

describe("basic tests", function(){
  test(10,23)
})