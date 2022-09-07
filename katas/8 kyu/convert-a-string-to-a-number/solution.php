<!-- convert-a-string-to-a-number -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function stringToNumber($str) {
  return intval($str);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function stringToNumber($str) { return +$str; }
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testFixedTests() {
      $this->assertEquals(1234, stringToNumber("1234"));
      $this->assertEquals(605, stringToNumber("605"));
      $this->assertEquals(1405, stringToNumber("1405"));
      $this->assertEquals(-7, stringToNumber("-7"));
    }
}