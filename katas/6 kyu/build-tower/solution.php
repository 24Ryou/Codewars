<!-- build-tower -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function tower_builder(int $n): array {
  return $n === 1 ? ['*'] : array_merge(array_map(function (string $f): string {return " $f ";}, tower_builder($n - 1)), [implode(array_fill(0, 2 * $n - 1, '*'))]);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function tower_builder(int $n): array {
  $pad = $n * 2 - 1;
  $x = 1;
  
  $arr = [];
  while ($n --> 0) {
      $arr[] = str_pad(str_repeat('*', $x), $pad, ' ', STR_PAD_BOTH);
      $x += 2;
  }

  return $arr;
}
/* ---------------------------------- TEST ---------------------------------- */
class TowerBuilderTest extends TestCase {
  public function testBaseCase() {
    $this->assertEquals(['*'], tower_builder(1));
  }
  public function testDescriptionExamples() {
    $this->assertEquals([
      '  *  ',
      ' *** ',
      '*****'
    ], tower_builder(3));
    $this->assertEquals([
      '     *     ', 
      '    ***    ', 
      '   *****   ', 
      '  *******  ', 
      ' ********* ', 
      '***********'
    ], tower_builder(6));
  }
}