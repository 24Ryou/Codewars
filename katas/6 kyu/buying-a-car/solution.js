// buying-a-car
/* ------------------------------- MY SOLUTION ------------------------------ */
function nbMonths(oldCarPrice, newCarPrice, savingMonth, percentLoss){
  saving = 0
  month = 0

  while ((saving + oldCarPrice) < newCarPrice ){
    month += 1
    saving += savingMonth

    if (month % 2 == 0) {
      percentLoss += 0.5
    }
    oldCarPrice *= ((100 - percentLoss) / 100)
    newCarPrice *= ((100 - percentLoss) / 100)
  }
  return [month , Math.round(saving + oldCarPrice - newCarPrice)]
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
// ! test is having issue use online!!
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

// describe("Tests", () => {
//   it("test", () => {
// Test(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
// Test(nbMonths(12000, 8000, 1000, 1.5) ,[0, 4000])
//   });
// });
