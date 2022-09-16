<!-- sum-of-odd-numbers -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function rowSumOddNumbers($n) {
  return $n * $n * $n;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase {
  public function testFixedTests() {
    $this->assertEquals(1, rowSumOddNumbers(1));
    $this->assertEquals(8, rowSumOddNumbers(2));
    $this->assertEquals(2197, rowSumOddNumbers(13));
    $this->assertEquals(6859, rowSumOddNumbers(19));
    $this->assertEquals(68921, rowSumOddNumbers(41));
    $this->assertEquals(74088, rowSumOddNumbers(42));
    $this->assertEquals(405224, rowSumOddNumbers(74));
    $this->assertEquals(636056, rowSumOddNumbers(86));
    $this->assertEquals(804357, rowSumOddNumbers(93));
    $this->assertEquals(1030301, rowSumOddNumbers(101));
  }
}