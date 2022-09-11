<!-- rock-paper-scissors -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function rpc ($p1, $p2) {
  $rules = array(
    "rock" => "paper",
    "paper" => "scissors",
    "scissors" => "rock"
  );
  if ($rules[$p1] == $rules[$p2]){
    return "Draw!";
  }
  return $rules[$p1] == $p2 ? 'Player 2 won!' : "Player 1 won!";
}
/* ---------------------------------- TEST ---------------------------------- */
class rpcTestCases extends TestCase {
  private function dotest($p1, $p2, $exp) {
        $actual = rpc ($p1, $p2);
        //echo $exp == $actual;
        $this->assertEquals($exp, $actual);
    }
    
    public function testrpcBasics() {
        $this->dotest("rock", "scissors", "Player 1 won!");
        $this->dotest("scissors", "rock", "Player 2 won!");
        $this->dotest("scissors", "scissors", "Draw!");
    }
}