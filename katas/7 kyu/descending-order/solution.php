<!-- descending-order -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function descendingOrder(int $n): int {
  $arr = array_map('intval' , str_split($n));
  rsort($arr , SORT_NUMERIC);
  $string = implode("" , $arr);
  return intval($string);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function descendingOrder(int $n): int {
  $arrayNumber = str_split($n);
  arsort($arrayNumber);
  return (int)  implode($arrayNumber);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testDigits() {
        $this->assertSame(0, descendingOrder(0));
        $this->assertSame(1, descendingOrder(1));
    }

    public function testSmallNumbers() {
        $this->assertSame(51, descendingOrder(15));
        $this->assertSame(2110, descendingOrder(1021));
    }

    public function testBigNumbers() {
        $this->assertSame(987654321, descendingOrder(123456789));
    }
}