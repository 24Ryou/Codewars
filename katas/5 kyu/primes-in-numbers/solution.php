<!-- primes-in-numbers -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function primeFactors($n) {
  if ($n < 2) return "(".strval($n).")";
  $factors = "";
  for ($i = 2; $i <= $n; $i++) {
    $cnt = 0;
    while ($n % $i == 0) {
      $cnt++;
      $n /= $i;
    }
    if ($cnt) {
      $factors .= "(".strval($i);
      if ($cnt > 1) {
        $factors .= "**".strval($cnt);
      }
      $factors .= ")";
    }
  }
  return $factors;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
class PrimeFactorsTestCases extends TestCase
{
  private function revTest($actual, $expected) {
    $this->assertSame($expected, $actual);
  }
  public function testBasics() {
    $this->revTest(primeFactors(7775460),"(2**2)(3**3)(5)(7)(11**2)(17)");
    $this->revTest(primeFactors(7919),"(7919)");
    $this->revTest(primeFactors(17*17*93*677),"(3)(17**2)(31)(677)");
  }
}
/* ---------------------------------- TEST ---------------------------------- */