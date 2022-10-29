<!-- buying-a-car -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function nbMonths($startPriceOld, $startPriceNew, $savingPerMonth, $percentLossByMonth) {
  $savings = 0;
  $months = 0;

  while (($savings + $startPriceOld) < $startPriceNew) {
    $months++;
    $savings += $savingPerMonth;

    if ($months % 2 == 0) $percentLossByMonth += 0.5;

    $startPriceOld *= ((100 - $percentLossByMonth) / 100);
    $startPriceNew *= ((100 - $percentLossByMonth) / 100);
  }

  return [$months , (int)round($savings + $startPriceOld - $startPriceNew)];
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class BuyingCarCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertEquals($expected, $actual);
    }
    public function testBasics() {
        $this->revTest(nbMonths(2000, 8000, 1000, 1.5), [6, 766]);
        $this->revTest(nbMonths(12000, 8000, 1000, 1.5) ,[0, 4000]);
        $this->revTest(nbMonths(8000, 12000, 500, 1), [8, 597]);
    }
}
