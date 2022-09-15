<!-- reverse-words -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function reverseWords($str) {
  $arr = explode(" " , $str);
  foreach ($arr as $key => $word){
    $arr[$key] = strrev($word);
  }
  return implode(" " , $arr);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function reverseWords($str) {
  return implode(' ', array_map('strrev', explode(' ', $str)));
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testBasicTests() {
      $this->assertEquals('ehT kciuq nworb xof spmuj revo eht yzal .god', reverseWords('The quick brown fox jumps over the lazy dog.'));
      $this->assertEquals('elppa', reverseWords('apple'));
      $this->assertEquals('a b c d', reverseWords('a b c d'));
      $this->assertEquals('elbuod  decaps  sdrow', reverseWords('double  spaced  words'));
      $this->assertEquals('desserts stressed', reverseWords('stressed desserts'));
      $this->assertEquals('olleh olleh', reverseWords('hello hello'));
    }
}