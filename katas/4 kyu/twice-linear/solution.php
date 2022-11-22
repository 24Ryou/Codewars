<!-- twice-linear -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function dblLinear($n) {
  $u = [1];
  $i = 0;
  $j = 0;

  while (count($u) <= $n) {
    $y = 2 * $u[$i] + 1;
    $z = 3 * $u[$j] + 1;

    if ($y > $z) {
      array_push($u , $z);
      $j++;
    }

    elseif ($y < $z) {
      array_push($u , $y);
      $i++;
    }

    else {
      array_push($u , $y);
      $i++;
      $j++;
    }
  }
  return $u[$n];
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class DoubleLinearTest extends TestCase {
  private function revTest($actual, $expected) {
      $this->assertSame($expected, $actual);
  }
  public function testBasics() {        
      $this->revTest(dblLinear(10), 22);
      // $this->revTest(dblLinear(20), 57);
      $this->revTest(dblLinear(30), 91);
      $this->revTest(dblLinear(50), 175);
      $this->revTest(dblLinear(100), 447);
  }
}