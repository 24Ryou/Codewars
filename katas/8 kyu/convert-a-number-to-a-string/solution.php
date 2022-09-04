<!-- convert-a-number-to-a-string -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function numberToString($num)
{
  return "$num";
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function numberToString(int $num): string {
  return $num;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testSampleTests() {
      $this->assertSame('67', numberToString(67));
    }
}