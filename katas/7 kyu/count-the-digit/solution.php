<!-- count-the-digit -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function nbDig($n, $d) {
  $arr = array();
  for ($i=0; $i <= $n; $i++) { 
    array_push($arr , $i*$i);
  }
  return substr_count(implode('',$arr) , "$d");
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function nbDig($n, $d) {
  $string = "";
  for ($x=0; $x <= $n; $string .= ($x++)**2);
  return substr_count($string,$d);
}
/* ---------------------------------- TEST ---------------------------------- */
class CountDigitTestCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertEquals($expected, $actual);
    }
    public function testBasics() {        
        $this->revTest(nbDig(5750, 0), 4700);
        $this->revTest(nbDig(11011, 2), 9481);
        $this->revTest(nbDig(12224, 8), 7733);
    }
}
