<!-- sudoku-solution-validator -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function valid_solution(array $m): bool {
  $matrix = array_fill(0, 27, 1); 
  foreach ($m as $y => $row) {
    foreach ($row as $x => $value) {
      $matrix[$y] *= $value; //row
      $matrix[$x + 9] *= $value; //column
      $t = intdiv($y, 3) * 3 + intdiv($x, 3);
      $matrix[$t + 18] *= $value; //3x3
    }
  }
  return array_sum($matrix) === 362880 * 27; // 9! * 27
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class ValidSolutionTest extends TestCase {
  public function testDescriptionExamples() {
    $this->assertTrue(valid_solution([
      [5, 3, 4, 6, 7, 8, 9, 1, 2], 
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]));
    $this->assertFalse(valid_solution([
      [5, 3, 4, 6, 7, 8, 9, 1, 2], 
      [6, 7, 2, 1, 9, 0, 3, 4, 8],
      [1, 0, 0, 3, 4, 2, 5, 6, 0],
      [8, 5, 9, 7, 6, 1, 0, 2, 0],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 0, 1, 5, 3, 7, 2, 1, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 0, 0, 4, 8, 1, 1, 7, 9]
    ]));
  }
}