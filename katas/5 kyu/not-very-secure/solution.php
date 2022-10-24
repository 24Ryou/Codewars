<!-- not-very-secure -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function alphanumeric(string $s): bool {
  $regex = '/^(?=[^\s_])[a-zA-Z0-9]+$/';
  return preg_match_all($regex , $s , $matches);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function alphanumeric(string $s): bool {
  return ctype_alnum($s);
}
/* ---------------------------------- TEST ---------------------------------- */
class AlphanumericTest extends TestCase {
  public function testExamples() {
    $this->assertTrue(alphanumeric('Mazinkaiser'));
    $this->assertFalse(alphanumeric('hello world_'));
    $this->assertTrue(alphanumeric('PassW0rd'));
    $this->assertFalse(alphanumeric('     '));
  }
}