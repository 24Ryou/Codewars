<!-- calculate-average -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function find_average($array) {
  return array_sum($array)/count($array);
}
/* ---------------------------------- TEST ---------------------------------- */
class CalculateAverageTest extends TestCase {
  public function testExamples() {
    $this->assertEquals(1, find_average([1, 1, 1]));
    $this->assertEquals(2, find_average([1, 2, 3]));
    $this->assertEquals(2.5, find_average([1, 2, 3, 4]));
  }
}