<!-- printer-errors -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function printerError($s) {
  $sample = 'abcdefghijklm';
  $arr = str_split($s);
  $error = 0;
  foreach ($arr as $chr){
    if (strpos($sample , $chr) === false){
      $error ++ ;
    }
  }
  return $error . "/" . strlen($s);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function printerError($s) {
  return strlen(preg_replace('/[a-m]/i', '', $s)) . '/' . strlen($s);
}

function printerError($s) {
  return preg_match_all('/[^a-m]/', $s).'/'.strlen($s);
}
/* ---------------------------------- TEST ---------------------------------- */
class PrinterErrorTestCases extends TestCase {
  private function revTest($actual, $expected) {
      $this->assertEquals($expected, $actual);
  }
  public function testBasics() {        
      $s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
      $this->revTest(printerError($s), "3/56");
      $s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
      $this->revTest(printerError($s), "6/60");
      $s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu";
      $this->revTest(printerError($s) , "11/65");
  }
}
