// help-the-bookseller
/* ------------------------------- MY SOLUTION ------------------------------ */
function stockList(listOfArt, listOfCat){
  let totalAmountOfBooks = 0 
  const cats = listOfCat.map(c => {
    const stockListsWithCat = listOfArt.filter(sl => sl.indexOf(c) === 0)
    const booksInStockList = stockListsWithCat.map(sl => parseInt(sl.split(' ')[1]))
    const amountOfBooks = booksInStockList.reduce( (acc, curr) => {
      return acc + curr
    }, 0)
    totalAmountOfBooks += amountOfBooks
    return `(${c} : ${amountOfBooks})`
  })
  if (totalAmountOfBooks === 0) return ''
  return cats.join(' - ')
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function stockList(listOfArt, listOfCat) {
  var qs = {};
  if (!listOfArt.length) return '';

  listOfArt.forEach(function(art) {
    var cat = art[0];
    qs[cat] = (qs[cat] | 0) + +art.split(' ')[1];
  });

  return listOfCat.map(function(c) {
    return '(' + c + ' : ' + (qs[c] | 0) + ')';  
  }).join(' - ');  
}
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;
const assert = require('chai').assert
describe("Tests", () => {
  it("test", () => {
    let b,c,res
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B", "C", "D"]
    res = "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"
    assert.strictEqual(stockList(b, c), res)

    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B"]
    res = "(A : 200) - (B : 1140)"
    assert.strictEqual(stockList(b, c), res)
  });
});
