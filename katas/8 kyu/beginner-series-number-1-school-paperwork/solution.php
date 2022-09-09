<!-- beginner-series-number-1-school-paperwork -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function paperwork(int $n, int $m): int
{
  if ($n > 0 and $m > 0){
    return $n*$m;
  }
  else {
    return 0;
  }
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function paperwork(int $n, int $m): int
{
  return max(0, $n) * max(0, $m);
}
/* ------------------------------ BEST PRACTICE ----------------------------- */
function paperwork(int $n, int $m): int {
  return $n < 0 || $m < 0 ? 0 : $n * $m;
}
/* ---------------------------------- TEST ---------------------------------- */
class PaperworkTest extends TestCase
{
    public function testExample()
    {
      $this->assertEquals(25, paperwork(5, 5), 'Failed at paperwork(5, 5)');
      $this->assertEquals(0, paperwork(-5, 5), 'Failed at paperwork(-5, 5)');
      $this->assertEquals(0, paperwork(5, -5), 'Failed at paperwork(5, -5)');
      $this->assertEquals(0, paperwork(-5, -5), 'Failed at paperwork(-5, -5)');
      $this->assertEquals(0, paperwork(5, 0), 'Failed at paperwork(5, 0)');
    }
}