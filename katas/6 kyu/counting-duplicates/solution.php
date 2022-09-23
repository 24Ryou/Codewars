<!-- counting-duplicates -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function duplicateCount($text) {
  if ($text != "") {
    $chars = array_unique(str_split(strtolower($text)));
    $times = array();
    foreach ($chars as $chr){
      array_push($times , substr_count(strtolower($text) , $chr));
    }
    return count(array_filter($times , function ($x) {return $x >= 2;}));
  }
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function duplicateCount($text) : int {
  $stats = array_count_values(str_split(strtolower($text)));
  return count(array_filter($stats, function($value) {return $value > 1;} ));
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    // test function names should start with "test"
    public function testFixedTests() {
      $this->assertEquals(0, duplicateCount(""));
      $this->assertEquals(0, duplicateCount("abcde"));
      $this->assertEquals(2, duplicateCount("aabbcde"));
      $this->assertEquals(2, duplicateCount("aabBcde"), "should ignore case");
      $this->assertEquals(1, duplicateCount("Indivisibility"));
      $this->assertEquals(2, duplicateCount("Indivisibilities"), "characters may not be adjacent");
    }
}