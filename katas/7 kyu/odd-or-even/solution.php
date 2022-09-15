<!-- odd-or-even -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function odd_or_even(array $a): string {
  return array_sum($a) % 2 == 0 ? 'even' : 'odd';
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function odd_or_even(array $a): string {
  return array_sum($a) % 2 ? 'odd' : 'even';
}
/* ---------------------------------- TEST ---------------------------------- */
class OddOrEvenTest extends TestCase {
  public function testDescriptionExamples() {
    $this->assertEquals('even', odd_or_even([0]));
    $this->assertEquals('odd', odd_or_even([2, 5, 34, 6]));
    $this->assertEquals('even', odd_or_even([0, -1, -5]));
  }
}