// keep-hydrated-1
/* ------------------------------- MY SOLUTION ------------------------------ */
function litres(time) {
  return parseInt(time / 2);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function litres(time) {
  return Math.floor(time/2);
}

litres = t => ~~(t / 2);
/* ---------------------------------- TEST ---------------------------------- */
// const chai = require("chai");
// const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
// chai.config.truncateThreshold=0;

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe('Fixed tests', () => {
  it('Tests', () => {
    assert.strictEqual(litres(2), 1, 'should return 1 litre');
    assert.strictEqual(litres(1.4), 0, 'should return 0 litres');
    assert.strictEqual(litres(12.3), 6, 'should return 6 litres');
    assert.strictEqual(litres(0.82), 0, 'should return 0 litres');
    assert.strictEqual(litres(11.8), 5, 'should return 5 litres');
    assert.strictEqual(litres(1787), 893, 'should return 893 litres');
    assert.strictEqual(litres(0), 0, 'should return 0 litres');
  });
});