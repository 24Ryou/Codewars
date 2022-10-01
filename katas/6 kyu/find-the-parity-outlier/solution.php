<!-- find-the-parity-outlier -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function find($integers) {
  $odd = array_filter($integers , function ($x) { return $x%2 !== 0;});
  $even = array_filter($integers , function ($x) { return $x%2 === 0;});
  return count($odd) > count($even) ? end($even) : end($odd);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function find($i) {
  foreach ($i as $x)
    $x % 2 == 0 ? $even[] = $x : $odd[] = $x;
  return $odd < $even ? $odd[0] : $even[0];
}
/* ---------------------------------- TEST ---------------------------------- */
class Tests extends TestCase
{
  public function testBasic() {
    $this->assertEquals(101, find([100, 101, 102]));
    $this->assertEquals(100, find([1, 9, 27, 81, 100]));
    $this->assertEquals(11, find([2, 4, 0, 100, 4, 11, 2602, 36]));
    $this->assertEquals(160, find([160, 3, 1719, 19, 11, 13, -21]));
  }
}