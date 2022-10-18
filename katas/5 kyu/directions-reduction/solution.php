<!-- directions-reduction -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function dirReduc($arr) {
  $d = ['WEST' => 'EAST', 'EAST' => 'WEST', 'NORTH' => 'SOUTH', 'SOUTH' => 'NORTH'];
  $r = array();
  foreach ($arr as $i) {
    if ($d[$i] == end($r)) {
      array_pop($r);
    }
    else array_push($r , $i);
  }
  return $r;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class DirectionReductionTestCases extends TestCase
{
  private function revTest($actual, $expected) {
    $this->assertSame($expected, $actual);
  }
  public function testBasics() {
    $a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"];
    $this->revTest(dirReduc($a), ["WEST"]);
    $b=["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"];
    $this->revTest(dirReduc($b), []);
    $c = ["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"];
    $this->revTest(dirReduc($c), ["NORTH"]);
  }
}