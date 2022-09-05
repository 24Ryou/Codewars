<!-- string-repeat -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function repeatStr($n, $str)
{
  $r = '';
  while($n > 0){
    $r .= $str;
    $n -= 1;
  }
  return $r;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function repeatStr($n, $str)
{
  return str_repeat($str, $n);
}
/* ---------------------------------- TEST ---------------------------------- */

class RepeatStrTest extends TestCase
{
    public function testThatSomethingShouldHappen()
    {
      $this->assertEquals("***", repeatStr(3, "*"));
      $this->assertEquals("@@", repeatStr(2, "@"));
      $this->assertEquals("!", repeatStr(1, "!"));
    }
}