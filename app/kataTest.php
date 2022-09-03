<!-- slug -->
<!-- 
<?php 
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function even_or_odd(int $n): string {
  $result = '';
  if ($n % 2 == 0){
    $result = 'Even';
  }
  else {
    $result = 'Odd';
  }
  return $result;
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