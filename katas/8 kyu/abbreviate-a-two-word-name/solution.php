<!-- abbreviate-a-two-word-name -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function abbrevName($name)
{
  $nms = explode(" " , strtoupper($name));
  return "{$nms[0][0]}.{$nms[1][0]}";
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function abbrevName(string $name): string
{
    $divide = explode(' ', $name);
    return strtoupper("{$divide[0][0]}.{$divide[1][0]}");
}
/* ---------------------------------- TEST ---------------------------------- */
class SolutionTest extends TestCase
{
    public function testSampleTests() {
      $this->assertEquals("S.H", abbrevName("Sam Harris"));
      $this->assertEquals("P.F", abbrevName("Patrick Feenan"));
      $this->assertEquals("E.C", abbrevName("Evan Cole"));
      $this->assertEquals("P.F", abbrevName("P Favuzzi"));
      $this->assertEquals("D.M", abbrevName("David Mendieta"));
    }
}