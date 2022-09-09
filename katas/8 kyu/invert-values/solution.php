<!-- invert-values -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function invert(array $a): array {
  $b = array();
  foreach ($a as $value) {
    array_push($b , -$value);
  };
  return $b;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function invert(array $a): array {
  return array_map(function ($n) {return -$n;}, $a);
}
/* ---------------------------------- TEST ---------------------------------- */
class InvertTest extends TestCase {
  public function testFixed() {
    $this->assertEquals([-1, -2, -3, -4, -5], invert([1, 2, 3, 4, 5]));
    $this->assertEquals([-1, 2, -3, 4, -5], invert([1, -2, 3, -4, 5]));
    $this->assertEquals([], invert([]));
    $this->assertEquals([0], invert([0]));
  }
}