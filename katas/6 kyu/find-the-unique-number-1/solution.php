<!-- find-the-unique-number-1 -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function find_uniq($a) {
  sort($a);
  
  return ($a[0] === $a[1]) ? end($a) : current($a);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class FindUniqTest extends TestCase {
  public function testExamples() {
    $this->assertEquals(2, find_uniq([1, 1, 1, 2, 1, 1]));
    $this->assertEquals(0.55, find_uniq([0, 0, 0.55, 0, 0]));
    $this->assertEquals(1, find_uniq([0, 1, 0]));
  }
}