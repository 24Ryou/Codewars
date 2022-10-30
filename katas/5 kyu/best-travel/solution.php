<!-- best-travel -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function chooseBestSum($t, $k, $ls) {
  // the $arr part fills $arr with all possible combinations
  $arr = array(array( ));

  foreach ($ls as $element)
    foreach ($arr as $combination)
      array_push($arr, array_merge(array($element), $combination));

  $longest = [];

  foreach($arr as $subar) {
    if (count($subar) != $k)
      continue;
    
    if (array_sum($subar) > array_sum($longest) and array_sum($subar) <= $t)
      $longest = $subar;
  }

  return count($longest) > 0 ? array_sum($longest) : null;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class BestTravelTestCases extends TestCase {
  private function revTest($actual, $expected) {
      $this->assertSame($expected, $actual);
  }
  public function testCountOnesBasics() {
      $ts = [50, 55, 56, 57, 58];
      $this->revTest(chooseBestSum(163, 3, $ts), 163);
      $ts = [50];
      $this->revTest(chooseBestSum(163, 3, $ts), null);
      $ts = [91, 74, 73, 85, 73, 81, 87];
      $this->revTest(chooseBestSum(230, 3, $ts), 228);
  }
}