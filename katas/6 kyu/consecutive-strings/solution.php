<!-- consecutive-strings -->
<?php
use PHPUnit\Framework\TestCase;


/* ------------------------------- MY SOLUTION ------------------------------ */
function longestConsec($strarr, $k) {
  $longest = '';
  if ($k > 0) {
    for ($i = 0; $i < count($strarr) - $k + 1; $i++) {
      $consecutive = implode('', array_slice($strarr, $i, $k));
      $longest = strlen($consecutive) > strlen($longest) ? $consecutive : $longest;
    }
  }
  return $longest;
}
/* ---------------------------------- TEST ---------------------------------- */
class ConsecutiveTestCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertEquals($expected, $actual);
    }
    public function testBasics() {
        $this->revTest(longestConsec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta");
        $this->revTest(longestConsec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh");
        $this->revTest(longestConsec([], 3), "");
    }
}