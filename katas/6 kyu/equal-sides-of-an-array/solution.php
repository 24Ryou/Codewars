<!-- equal-sides-of-an-array -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function find_even_index($arr){
  foreach($arr as $key => $item) {
    $left = array_slice($arr , 0 , $key);
    $right = array_slice($arr , $key+1);
    if (array_sum($left) == array_sum($right)){
      return $key;
    }
  }
  return -1;
}
/* ---------------------------------- TEST ---------------------------------- */
class FindEvenIndexTest extends TestCase
{
    public function testIt() {
      $this->assertSame(3,find_even_index(array(1,2,3,4,3,2,1)));
      $this->assertSame(1,find_even_index([1,100,50,-51,1,1]));
      $this->assertSame(-1,find_even_index([1,2,3,4,5,6]));
      $this->assertSame(3,find_even_index([20,10,30,10,10,15,35]));
      $this->assertSame(0,find_even_index([20,10,-80,10,10,15,35]));
      $this->assertSame(6,find_even_index([10,-80,10,10,15,35,20]));
      $this->assertSame(-1,find_even_index(range(1,100)));
      $this->assertSame(0,find_even_index([0,0,0,0,0]),"Should pick the first index if more cases are valid");
      $this->assertSame(3,find_even_index([-1,-2,-3,-4,-3,-2,-1]));
      $this->assertSame(-1,find_even_index(range(-100,-1)));

    }
}