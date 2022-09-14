<!-- growth-of-a-population -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function nbYear($p0, $percent, $aug, $p) {
  $percent = $percent / 100;
  $year = 0;
  while($p0 < $p){
    $p0 += floor($p0 * $percent) + $aug;
    $year++;
  }
  return $year;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function nbYear($p0, $percent, $aug, $p) {
  return $p0 >= $p ? 0 : 1 + nbYear((int)$p0 * (1+$percent/100) + $aug, $percent, $aug, $p);   
}
/* ---------------------------------- TEST ---------------------------------- */
class PopulationGrowthCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertEquals($expected, $actual);
    }
    public function testBasics() {
        $this->revTest(nbYear(1500, 5, 100, 5000), 15);
        $this->revTest(nbYear(1500000, 2.5, 10000, 2000000), 10);
    }
}