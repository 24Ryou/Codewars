<!-- isograms -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function isIsogram($string) {
  $string = strtolower($string);
  return $string == "" ? true : count(array_unique(str_split($string , 1)))  == strlen($string) ;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testSampleTests() {
      $this->assertEquals(true, isIsogram("Dermatoglyphics"));
      $this->assertEquals(true, isIsogram("isogram"));
      $this->assertEquals(false, isIsogram("aba"), "same chars may not be adjacent");
      $this->assertEquals(false, isIsogram("moOse"), "same chars may not be same case");
      $this->assertEquals(false, isIsogram("isIsogram"));
      $this->assertEquals(true, isIsogram(""), "an empty string is a valid isogram");
    }
}