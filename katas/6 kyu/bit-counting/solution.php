<!-- bit-counting -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function countBits($n) 
{
  return substr_count(decbin($n) , "1");
}
/* ---------------------------------- TEST ---------------------------------- */
class CountBitsTestCases extends TestCase
{
    public function testResultCountBits() {
      $this->assertEquals(countBits(0), 0);
      $this->assertEquals(countBits(4), 1);
      $this->assertEquals(countBits(7), 3);
      $this->assertEquals(countBits(9), 2);
      $this->assertEquals(countBits(10), 2);
    }
}