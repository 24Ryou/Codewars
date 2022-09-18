<!-- build-a-pile-of-cubes -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function findNb($m){
  $total = 0;
  $n = 0;
  
  while ($total < $m){
    $n = $n + 1;
    $total = $total + $n ** 3;
  }
  return $total == $m ? $n : -1;
}
/* ---------------------------------- TEST ---------------------------------- */
class PileOfCubesCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertEquals($expected, $actual);
    }
    public function testBasics() {
        $this->revTest(findNb(4183059834009), 2022);
        $this->revTest(findNb(24723578342962), -1);
        $this->revTest(findNb(135440716410000), 4824);
    }
}
