<!-- help-the-bookseller -->
<!-- regex explain https://regexr.com/72t0h -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function stockList($listOfArt, $listOfCat){
  if (empty($listOfArt) || empty($listOfCat)) return "";
  foreach ($listOfCat as $chr) {
    $arr[$chr] = 0;
    foreach ($listOfArt as $str) {
      preg_match('/^\w/' , $str , $match);
      if ($match[0] === $chr){
        $arr[$chr] += (int)(explode(" " , $str))[1];
      }
    }
  }
  array_walk($arr, function(&$value, $key) { $value = "($key : $value)"; });
  return implode(" - " , $arr);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class BookSellerTest extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertSame($expected, $actual);
    }
    public function testBasics() {                
        $b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"];
        $c = ["A", "B", "C", "D"];
        $res = "(A : 0) - (B : 1290) - (C : 515) - (D : 600)";
        $this->revTest(stockList($b, $c), $res);

        $b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"];
        $c = ["A", "B"];
        $res = "(A : 200) - (B : 1140)";
        $this->revTest(stockList($b, $c), $res);
    }
}