<!-- grasshopper-summation -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function summation($n) {
  $sum = 0;
  while($n > 0){
    $sum = $sum + $n;
    $n -= 1;
  }
  return $sum;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function summation($n) {
  return array_sum(range(1, $n));
}
/* ---------------------------------- TEST ---------------------------------- */
class SummationTest extends TestCase {
  public function testThatSummationWorksForExampleTests() {
    $this->assertEquals(summation(1), 1);
    $this->assertEquals(summation(2), 3);
    $this->assertEquals(summation(3), 6);
    $this->assertEquals(summation(4), 10);
    $this->assertEquals(summation(5), 15);
  }
}