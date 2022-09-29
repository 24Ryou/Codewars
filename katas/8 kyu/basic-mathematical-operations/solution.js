// basic-mathematical-operations
/* ------------------------------- MY SOLUTION ------------------------------ */
function basicOp(operation, value1, value2)
{
  return eval(`${value1} ${operation} ${value2}`)
}
/* ---------------------------------- TEST ---------------------------------- */
// node v10.x not working with mocha and chai
describe("Tests", () => {
  it("test", () => {
console.log("Basic tests\n");
Test.assertSimilar(basicOp('+', 4, 7), 11);
Test.assertSimilar(basicOp('-', 15, 18), -3);
Test.assertSimilar(basicOp('*', 5, 5), 25);
Test.assertSimilar(basicOp('/', 49, 7), 7);
  });
});
