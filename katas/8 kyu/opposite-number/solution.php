<!-- opposite-number -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function opposite($n) {
  return -$n;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class OppositeTest extends TestCase {
  public function testThatOppositeWorksForExamplesProvidedInDescription() {
    $this->assertSame(opposite(1), -1);
    $this->assertSame(opposite(14), -14);
    $this->assertSame(opposite(-34), 34);
  }
}