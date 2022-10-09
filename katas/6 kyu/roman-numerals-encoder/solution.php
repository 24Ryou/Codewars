<!-- roman-numerals-encoder -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function solution($number)
{
  $dic = ['M'=>1000,'CM'=>900,'D'=>500,'CD'=>400,'C'=>100,'XC'=>90,'L'=>50,'XL'=>40,'X'=>10,'IX'=>9,'V'=>5,'IV'=>4,'I'=>1];
  $out = '';
  foreach($dic as $key=>$value){
    while ($number >= $value){
      $out .= $key;
      $number -= $value;
    }
  }
  return $out;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function test_static_operations()
    {
      $this->assertEquals("M", solution(1000));
      $this->assertEquals("IV", solution(4));
      $this->assertEquals("I", solution(1));
      $this->assertEquals("MCMXC", solution(1990));
      $this->assertEquals("MMVIII", solution(2008));
    }
}