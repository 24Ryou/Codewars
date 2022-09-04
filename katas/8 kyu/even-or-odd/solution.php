<!-- even-or-odd -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function even_or_odd(int $n): string {
  if ($n % 2 == 0) {
    return 'Even';
  }
  else {
    return 'Odd';
  }
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class EvenOrOddTest extends TestCase {
  public function testExamples() {
    $this->assertEquals("Even", even_or_odd(2));
    $this->assertEquals("Even", even_or_odd(0));
    $this->assertEquals("Odd", even_or_odd(7));
    $this->assertEquals("Odd", even_or_odd(1));
    $this->assertEquals("Odd", even_or_odd(-1));
  }
}