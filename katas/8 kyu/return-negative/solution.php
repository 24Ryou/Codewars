<!-- return-negative -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function makeNegative(float $num) : float {
  return $num < 0 ? $num : -$num;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function makeNegative(float $num) : float {
  return -abs($num);
}
/* ---------------------------------- TEST ---------------------------------- */
class MakeNegativeTestCases extends TestCase
{
    // test makeNegative()
    public function testMakeNegative() {
      $this->assertEquals(makeNegative(7), -7);
      $this->assertEquals(makeNegative(-20), -20);
      $this->assertEquals(makeNegative(0), 0);
      $this->assertEquals(makeNegative(0.12), -0.12);
    }
}