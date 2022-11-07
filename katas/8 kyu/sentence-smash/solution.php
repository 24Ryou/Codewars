<!-- sentence-smash -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function smash(array $words): string {
  return implode(" " , $words);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class SmashTest extends TestCase {
  public function testExamples() {
    $this->assertSame('', smash([]));
    $this->assertSame('hello', smash(["hello"]));
    $this->assertSame('hello world', smash(["hello", "world"]));
  }
}