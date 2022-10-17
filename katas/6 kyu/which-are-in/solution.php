<!-- which-are-in -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function inArray($array1, $array2) {
  $arr = array();
  foreach ($array2 as $x){
    foreach ($array1 as $y){
      if (strpos($x , $y) !== false && in_array($y , $arr) == false){
        array_push($arr , $y);
      }
    }
  }
  sort($arr);
  return $arr;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function inArray($a1, $a2) {
  $r = array_filter($a1, function($v) use ($a2) {
    foreach ($a2 as $v2) {
      if (strpos($v2, $v) !== false) return true;
    }
    return false;
  });
  sort($r);
  return $r;
}
/* ---------------------------------- TEST ---------------------------------- */
class WhichAreInTestCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertSame($expected, $actual);
    }
    public function testBasics() {
        $a2 = ["lively", "alive", "harp", "sharp", "armstrong"];
        $a1 = ["arp", "live", "strong"];
        $this->revTest(inArray($a1, $a2), ["arp", "live", "strong"]);
        $a1 = ["xyz", "live", "strong"];
        $this->revTest(inArray($a1, $a2), ["live", "strong"]);
        $a1 = ["live", "strong", "arp"];
        $this->revTest(inArray($a1, $a2), ["arp", "live", "strong"]);
    }

}