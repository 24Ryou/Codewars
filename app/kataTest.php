<!-- reversed-strings -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function solution($str) {
  return strrev($str);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class ReversedStringsTest extends TestCase {
  public function testExamples() {
    $this->assertSame("dlrow", solution("world"));
    $this->assertSame("olleh", solution("hello"));
    $this->assertSame("", solution(""));
    $this->assertSame('h', solution("h"));
  }
}