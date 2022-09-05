<!-- remove-first-and-last-character -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function remove_char(string $s): string {
  return substr($s, 1, -1);
}
/* ---------------------------------- TEST ---------------------------------- */
class RemoveCharTest extends TestCase {
  public function testFixed() {
    $this->assertEquals('loquen', remove_char('eloquent'));
    $this->assertEquals('ountr', remove_char('country'));
    $this->assertEquals('erso', remove_char('person'));
    $this->assertEquals('lac', remove_char('place'));
  }
}