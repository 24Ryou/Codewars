// data-reverse
/* ------------------------------- MY SOLUTION ------------------------------ */
function dataReverse(data) {
  out = []
  for (let i = 0; i < data.length; i = i+8) {
    const x = data.slice(i , i+8);
    out.push(x)
  }
  out.reverse()
  return out.reduce((p , n) => p.concat(n) , [])
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("Data Reverse", function(){
  it("Example Tests", function(){
    const data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
    const data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    assert.deepEqual(dataReverse(data1),data2)
    const data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
    const data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
    assert.deepEqual(dataReverse(data3),data4)
  });
});