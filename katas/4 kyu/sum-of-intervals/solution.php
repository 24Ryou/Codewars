<!-- sum-of-intervals -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function sum_intervals(array $m): int {
  sort($m);
  $s = 0;
  $r = $m[0][0];
  foreach ($m as $x) {
    $s += max($r, $x[1]) - max($r, $x[0]);
    $r = max($r, $x[1]);
  }
  return $s;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class SumIntervalsTest extends TestCase {
  public function testExamples() {
    // Non-overlapping intervals
    $this->assertEquals(4, sum_intervals([[1, 5]]));
    $this->assertEquals(8, sum_intervals([
      [1, 5],
      [6, 10]
    ]));
    // Overlapping intervals
    $this->assertEquals(4, sum_intervals([
      [1, 5],
      [1, 5]
    ]));
    $this->assertEquals(7, sum_intervals([
      [1, 4],
      [7, 10],
      [3, 5]
    ]));
  }
  
  public function testLargeIntervals() {
    $this->assertEquals(2e9, sum_intervals([[-1e9, 1e9]]));
    $this->assertEquals(1e8 + 30, sum_intervals([
      [0, 20],
      [-1e8, 10],
      [30, 40]
    ]));
  }
}