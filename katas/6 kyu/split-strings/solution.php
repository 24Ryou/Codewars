<!-- split-strings -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function solution($str) {
  if ($str == "") return [];
  $arr = str_split($str , 2);
  $temp = array_pop($arr);
  if (strlen($temp) < 2){
    $temp .= "_";
  }
  array_push($arr , $temp);
  return $arr;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function solution($str) {
  if (empty($str))
    return [];
  if (strlen($str) % 2 != 0)
    $str .= "_";
  return str_split($str, 2);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testBasicTests() {
        $this->assertEquals(["ab", "cd", "ef"], solution("abcdef"));
        $this->assertEquals(["ab", "cd", "ef", "g_"], solution("abcdefg"));
        $this->assertEquals([], solution(""));
    }
}