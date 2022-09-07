<!-- keep-hydrated-1 -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function litres($t) {
  return floor($t / 2);
}
/* ---------------------------------- TEST ---------------------------------- */
class KeepHydratedTest extends TestCase {
  public function testFixed() {
    $this->assertEquals(1, litres(2));
    $this->assertEquals(0, litres(1.4));
    $this->assertEquals(6, litres(12.3));
    $this->assertEquals(0, litres(0.82));
    $this->assertEquals(5, litres(11.8));
    $this->assertEquals(893, litres(1787));
    $this->assertEquals(0, litres(0));
  }
}