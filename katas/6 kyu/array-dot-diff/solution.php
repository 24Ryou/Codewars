<!-- array-dot-diff -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function arrayDiff($a, $b) {
  $t = array();
  foreach ($a as $x){
    if (in_array($x , $b) == false){
      array_push($t , $x);
    }
  }
  return $t;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function arrayDiff($a, $b) {
  return array_values(array_diff($a, $b));
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCasesTest extends TestCase
{
    public function testSampleTests() {
      $this->assertEquals([2], arrayDiff([1,2], [1]), "a was [1,2], b was [1], expected [2]");
      $this->assertEquals([2,2], arrayDiff([1,2,2], [1]), "a was [1,2,2], b was [1], expected [2,2]");
      $this->assertEquals([1], arrayDiff([1,2,2], [2]), "a was [1,2,2], b was [2], expected [1]");
      $this->assertEquals([1,2,2], arrayDiff([1,2,2], []), "a was [1,2,2], b was [], expected [1,2,2]");
      $this->assertEquals([], arrayDiff([], [1,2]), "a was [], b was [1,2], expected []");
      $this->assertEquals([3], arrayDiff([1, 2, 3], [1,2]), "a was [1, 2, 3], b was [1,2], expected [3]");
    }
}