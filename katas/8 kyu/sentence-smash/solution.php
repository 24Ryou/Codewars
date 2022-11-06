<!-- matrix-determinant -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function minor(array $matrix, int $x): array
{
  array_shift($matrix);
  foreach ($matrix as $key => $row) {
    $matrix[$key] = array_merge(
      array_slice($row, 0, $x),
      array_slice($row, $x + 1)
    );
  }
  return $matrix;
}

function determinant(array $matrix): int
{
  $size = count($matrix);
  if ($size === 1) {
      return $matrix[0][0];
  }
  
  $result = 0;
  for ($i = 0, $k = 1; $i < $size; $i++, $k = -$k) {
      $result += $k * $matrix[0][$i] * determinant(minor($matrix, $i));
  }
  return $result;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MatrixDeterminantTest extends TestCase {
  public function testExamples() {
    $this->assertSame(1, determinant([[1]]), 'Determinant of a 1 x 1 matrix should equal the value of its one and only element');
    $this->assertSame(-1, determinant([
      [1, 3],
      [2, 5]
    ]), "Should return 1 * 5 - 3 * 2, i.e., -1");
    $this->assertSame(-20, determinant([
      [2, 5, 3],
      [1, -2, -1],
      [1, 3, 4]
    ]), 'Should work for a 3 x 3 matrix');
  }
}