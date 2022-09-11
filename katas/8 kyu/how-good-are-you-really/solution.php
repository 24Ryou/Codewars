<!-- how-good-are-you-really -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function betterThanAverage($classPoints, $yourPoints) {
  $classPoints = array_sum(($classPoints))/count($classPoints);
  return $classPoints < $yourPoints ? true : false;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function betterThanAverage($classPoints, $yourPoints) {
  return array_sum($classPoints) / count($classPoints) < $yourPoints;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase {
  public function testFixedTests() {
    $this->assertEquals(true, betterThanAverage([2, 3], 5));
    $this->assertEquals(true, betterThanAverage([100, 40, 34, 57, 29, 72, 57, 88], 75));
    $this->assertEquals(true, betterThanAverage([12, 23, 34, 45, 56, 67, 78, 89, 90], 69));
    $this->assertEquals(false, betterThanAverage([41, 75, 72, 56, 80, 82, 81, 33], 50));
    $this->assertEquals(false, betterThanAverage([29, 55, 74, 60, 11, 90, 67, 28], 21));
  }
}