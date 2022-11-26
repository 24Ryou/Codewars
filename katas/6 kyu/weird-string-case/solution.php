<!-- weird-string-case -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function toWeirdCase($string) {
  $arr = [];
  foreach (explode(" ", $string) as $word) {
    $temp = "";
    foreach (str_split($word) as $i => $val){
      $i % 2 === 0 ? $temp = $temp . strtoupper($val) : $temp = $temp . strtolower($val); 
    }
    $arr[] = $temp;
  } 
  return implode(" " , $arr);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function toWeirdCase($string) {
  $str = str_split(strtolower($string));
  for ($n=0; $n<=count($str); $n++) {
    if ($str[$n]!=" ") {
      $str[$n] = strtoupper($str[$n]);
      $n = $n + 1; 
    }
  }
  return implode("", $str);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTest extends TestCase
{
    // test function names should start with "test"
    public function testWeirdCaseConverter() {
      $this->assertSame('HeLlO WoRlD FoO BaR BaZ', toWeirdCase('Hello world foo bar baz'));
      $this->assertSame('WeLl I GuEsS YoU PaSsEd', toWeirdCase('wEll i GuesS you passed'));
    }
}