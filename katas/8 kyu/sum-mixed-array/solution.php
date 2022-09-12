<!-- sum-mixed-array -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function sum_mix($a) {
  $b = array();
  foreach ($a as $item){
    array_push($b , intval($item));
  }
  return array_sum($b);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function sum_mix($a) {
  return array_sum($a);
}
/* ---------------------------------- TEST ---------------------------------- */
class SumMixTest extends TestCase {
  public function testExamples() {
    $this->assertEquals(22, sum_mix([9, 3, '7', '3']));
    $this->assertEquals(42, sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]));
    $this->assertEquals(41, sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']));
  }
}