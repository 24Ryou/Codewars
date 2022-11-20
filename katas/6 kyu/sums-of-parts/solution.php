<!-- sums-of-parts -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function partsSums($ls) {
  $sums = [array_sum($ls)];
  foreach ($ls as $i) {
    array_push($sums, end($sums)-$i);
  }
  return $sums;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class partsSumsTest extends TestCase {
  private function dotest($ls, $expected) {
      $actual = partsSums($ls);
      $this->assertSame($expected, $actual);
  }
  public function testPartsSumsBasics() {      
      $this->dotest([], [0]);
      $this->dotest([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0]); 
      $this->dotest([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0]);         
      $this->dotest([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358], 
              [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]);                     
  }   
}