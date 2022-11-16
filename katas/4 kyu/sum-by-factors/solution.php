<!-- sum-by-factors -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function sumOfDivided($lst) {
  if (!is_array($lst) || empty($lst)) return array();

  $max = max(max($lst), abs(min($lst)));
  
  //get primes
  $sqrtmax = (int)sqrt($max);
  $primes[2] = true;
  for ($i = 3; $i <= $max; $i+=2) {
    $primes[$i] = true;
  }
  
  for($i = 3; $i <= $sqrtmax; $i+=2) {
    $z = 2;
    while($z*$i <=$max) {
      unset($primes[$i*$z]);
      $z++;
    }
  }


  foreach($primes as $prime => $true) {
    $isdivided = 0;
    $result = 0;
    foreach($lst as $num) {
      if ($num%$prime == 0) {
        $isdivided = 1;
        $result+=$num;
      }
    }
    if ($isdivided) {
      $return[]=[$prime, $result];
    }
  }

return $return;

}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class SumOfDividedTest extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertSame($expected, $actual);
    }
    public function testBasics() {        
        $this->revTest(sumOfDivided([12, 15]), [ [2, 12], [3, 27], [5, 15] ]);
        $this->revTest(sumOfDivided([15,21,24,30,45]), [ [2, 54], [3, 135], [5, 90], [7, 21] ]);
        $this->revTest(sumOfDivided([15,21,24,30,-45]), [ [2, 54], [3, 45], [5, 0], [7, 21] ]);
    }
}
