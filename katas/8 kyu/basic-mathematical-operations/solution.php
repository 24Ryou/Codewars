<!-- basic-mathematical-operations -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function basicOp($op, $val1, $val2)
{
  switch ($op) {
    case '+':
      return $val1 + $val2;
    case '-':
      return $val1 - $val2;
    case '*':
      return $val1 * $val2;
    case '/':
      return $val1 / $val2;
  }
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function basicOp($op, $val1, $val2)
{
  // this makes me feel dirty, but it gets the job done
  return eval("return {$val1}{$op}{$val2};");
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function test()
    {
      echo "<h1>Static Test Cases: </h1><br>";
      $this->check(basicOp('+', 4, 7), 11);
      $this->check(basicOp('-', 15, 18), -3);
      $this->check(basicOp('*', 5, 5), 25);
      $this->check(basicOp('/', 49, 7), 7);
    }
    private function check($a, $b)
    {
      echo "<span style='font-size: 20px'><span style='color:" . ($a == $b ? "green'>True:" : "red'>False:") . "</span></span><br>" . "Expected: " . $b . " <br> Got: " . $a . "<br>";
      $this->assertSame($a, $b);
    }
}