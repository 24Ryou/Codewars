<!-- two-to-one -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function longest($a, $b) {
  $arr = array_unique(str_split($a ."". $b));
  asort($arr);
  return implode($arr);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function longest($a, $b) {
  return count_chars($a.$b, 3);
}
/* ---------------------------------- TEST ---------------------------------- */
class LongestTestCases extends TestCase {
  private function revTest($actual, $expected) {
      $this->assertEquals($expected, $actual);
  }
  public function testBasics() {        
      $this->revTest(longest("aretheyhere", "yestheyarehere"), "aehrsty");
      $this->revTest(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu");
      $this->revTest(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy");
      $this->revTest(longest("lordsofthefallen", "gamekult"), "adefghklmnorstu");
  }
}