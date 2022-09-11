<!-- reversed-sequence -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function reverseSeq ($n) {
  $arr = array();
  for ($i = $n; $i>0;$i--){
    array_push($arr , $i);
  }
  return $arr;
};
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function reverseSeq ($n) {
  return range($n, 1);
};
/* ------------------------------ BEST PRACTICE ----------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    // test function names should start with "test"
    public function testBasic() {
      $this->assertEquals([5,4,3,2,1],reverseSeq(5));
      $this->assertEquals([1],reverseSeq(1));      
    }
}