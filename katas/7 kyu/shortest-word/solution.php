<!-- shortest-word -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function findShort($str){
  $arr = array_map('strlen' , explode(" " , $str));
  return min($arr);
}
/* ---------------------------------- TEST ---------------------------------- */
// PHPUnit Test Examples:
// TODO: Replace examples and use TDD development by writing your own tests
class MyTestCases extends TestCase
{
    // test function names should start with "test"
    public function testBasics() {
      $this->assertEquals(3, findShort("bitcoin take over the world maybe who knows perhaps"));
      $this->assertEquals(3, findShort("turns out random test cases are easier than writing out basic ones"));
      $this->assertEquals(2, findShort("Let's travel abroad shall we"));
    }
}