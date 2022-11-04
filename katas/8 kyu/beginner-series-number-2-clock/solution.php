<!-- beginner-series-number-2-clock -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function past($h, $m, $s) {
  return array_sum([$s , $m*60 , $h*3600]) * 1000;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function past($h, $m, $s) {
  return strtotime("$h:$m:$s", 0) * 1000;
}
/* ---------------------------------- TEST ---------------------------------- */

class KataTest extends TestCase {
  public function testBasicTests() {
    $this->assertSame(61000, past(0, 1, 1));
    $this->assertSame(3661000, past(1, 1, 1));
    $this->assertSame(0, past(0, 0, 0));
    $this->assertSame(3601000, past(1, 0, 1));
    $this->assertSame(3600000, past(1, 0, 0));
  }
}