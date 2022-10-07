<!-- playing-with-digits -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function digPow($n, $p) {
  $arr = str_split($n);
  // $result = array_sum(array_map(fn($v , $k) => $v ** ($p + $k) , $arr , array_keys($arr))); //php 8+
  $result = array_sum(array_map(function($v , $k) use (&$p) {return $v ** ($p + $k);} , $arr , array_keys($arr)));
  return $result%$n == 0 ? $result/$n : -1;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class PlayDigitTestCases extends TestCase
{
  private function revTest($actual, $expected) {
    $this->assertSame($expected, $actual);
  }
  public function testBasics() {        
    $this->revTest(digPow(89, 1), 1);
    $this->revTest(digPow(92, 1), -1);
    $this->revTest(digPow(46288, 3), 51);
  }
}
