<!-- snail -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function snail(array $array): array
{
  $result = [];
  while (!empty($array)) {
    $result = array_merge($result, array_shift($array));
    $array = rotate($array);
  }
  return $result;
}
function rotate(array $array): array
{
  if (!isset($array[0])) {
    return [];
  }
  $rotated = [];
  for ($i=0; $i < count($array[0]); $i++) {
    $rotated[] = array_column($array, $i);
  }
  return array_reverse($rotated);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class SnailTest extends TestCase {
  public function testDescriptionExamples() {
    $this->assertSame([1, 2, 3, 6, 9, 8, 7, 4, 5], snail([
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]));
    $this->assertSame([1, 2, 3, 4, 5, 6, 7, 8, 9], snail([
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]
    ]));
    $this->assertSame([1, 2, 3, 1, 4, 7, 7, 9, 8, 7, 7, 4, 5, 6, 9, 8], snail([
      [1, 2, 3, 1],
      [4, 5, 6, 4],
      [7, 8, 9, 7],
      [7, 8, 9, 7]
    ]));
    $this->assertSame([], snail([[]]), 'Your solution should also work properly for an empty matrix');
  }
}