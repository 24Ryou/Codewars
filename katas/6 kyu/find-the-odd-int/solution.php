<!-- find-the-odd-int -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function findIt(array $seq) : int
{
  $arr = array_count_values($seq);
  $result = array_filter($arr , function ($x) { return $x%2 != 0 ? true : false;});
  return key($result);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function findIt(array $seq) : int
{
  return array_reduce($seq, function($carry, $value) {
    return $carry ^ $value;
  });
}
/* ---------------------------------- TEST ---------------------------------- */
class BasicTestCases extends TestCase
{
    public function testFindItReturnsValueAppearingOddNumberOfTimes() 
    {
        $this->assertEquals(5, findIt([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]));
        $this->assertEquals(-1, findIt([1,1,2,-2,5,2,4,4,-1,-2,5]));
        $this->assertEquals(5, findIt([20,1,1,2,2,3,3,5,5,4,20,4,5]));
        $this->assertEquals(10, findIt([10]));
        $this->assertEquals(10, findIt([1,1,1,1,1,1,10,1,1,1,1]));
    }
}