<!-- highest-and-lowest -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function highAndLow($numbers)
{
  $arr = array_map('intval' , explode(" " , $numbers));
  return strval(max($arr) . " " . min($arr));
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function highAndLow($numbers) {
  $a = explode(' ', $numbers);
  return max($a) . " " . min($a);
}
/* ---------------------------------- TEST ---------------------------------- */
class ExampleTests extends TestCase
{
    public function test1() {
      $this->assertEquals("42 -9", highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4"));
    }
    public function test2() {
      $this->assertEquals("3 1", highAndLow("1 2 3"));
    }
}