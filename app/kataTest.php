<!-- sum-of-positive -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function positive_sum($arr) {
  $p = array();
  foreach ($arr as $item){
    if ($item > 0) {
      array_push($p , $item);
    }
  }
  return array_sum(($p));

}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class PositiveSumTest extends TestCase {
  public function testExamples() {
    $this->assertEquals(15, positive_sum([1, 2, 3, 4, 5]));
    $this->assertEquals(13, positive_sum([1, -2, 3, 4, 5]));
    $this->assertEquals(0, positive_sum([]));
    $this->assertEquals(0, positive_sum([-1, -2, -3, -4, -5]));
    $this->assertEquals(9, positive_sum([-1, 2, 3, 4, -5]));
  }
}