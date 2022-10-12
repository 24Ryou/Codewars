// rock-paper-scissors
/* ------------------------------- MY SOLUTION ------------------------------ */
const rules = {
  "rock" : "paper",
  "paper" : "scissors",
  "scissors" : "rock"
}
const rps = (p1, p2) => {
  if (rules[p1] === rules[p2]) return "Draw!" 
  return `Player ${rules[p1] === p2 ? 2:1} won!`
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
const chai = require("chai");
const Test = chai.assert.strictEqual; // replace Test.assertEqual with Test
chai.config.truncateThreshold=0;

describe('rock paper scissors', function() {
  const getMsg = (n) => `Player ${n} won!`;

  it('player 1 win', function() {
    Test(rps('rock', 'scissors'), getMsg(1));
    Test(rps('scissors', 'paper'), getMsg(1));
    Test(rps('paper', 'rock'), getMsg(1));
  });

  it('player 2 win', function() {
    Test(rps('scissors', 'rock'), getMsg(2));
    Test(rps('paper', 'scissors'), getMsg(2));
    Test(rps('rock', 'paper'), getMsg(2));
  });

  it('draw', function() {
    Test(rps('rock', 'rock'), 'Draw!');
    Test(rps('scissors', 'scissors'), 'Draw!');
    Test(rps('paper', 'paper'), 'Draw!');
  });
});