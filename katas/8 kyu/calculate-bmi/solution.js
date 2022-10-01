// calculate-bmi
/* ------------------------------- MY SOLUTION ------------------------------ */
function bmi(weight, height) {
  b = weight / height ** 2
  return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
}
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const assert = chai.assert; // assert.strictEqual
chai.config.truncateThreshold=0;

describe("Tests", () => {
  it("test", () => {
assert.strictEqual(bmi(80, 1.80), "Normal");
  });
});

describe("Tests", () => {
  it("test", () => {
assert.strictEqual(bmi(50, 1.80), "Underweight");
assert.strictEqual(bmi(80, 1.80), "Normal");
assert.strictEqual(bmi(90, 1.80), "Overweight");
assert.strictEqual(bmi(110, 1.80), "Obese");

console.log('Random tests')

function sol(weight, height) {
  let v = weight / (height * height);
  
  if(v <= 18.5)
    return "Underweight";
  else if (v <= 25.0)
    return "Normal";
  else if (v <= 30.0)
    return "Overweight";
  else
    return "Obese";
}

for(let i=0; i<25; i++) {
  let target = Math.random()*20+15;
  let height = Math.random()*0.5+1.5;
  let weight = target*height*height;
  assert.strictEqual(bmi(weight, height), sol(weight, height));
}
  });
});