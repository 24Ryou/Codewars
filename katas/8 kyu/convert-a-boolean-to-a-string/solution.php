<!-- convert-a-boolean-to-a-string -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function booleanToString($b) {
  return $b ? 'true' : 'false';
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTest extends TestCase {
  public function testFixedTests() {
    $this->assertEquals("true", booleanToString(true));
    $this->assertEquals("false", booleanToString(false));
  }
}