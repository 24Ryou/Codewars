<!-- integers-recreation-one -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function listSquared($m, $n) {

  $answer = [];
  
  for($i = $m; $i < $n; $i++)
  {
  
    $sum = sumOfDivisorsSquares($i);
    if(isSquare($sum))
    $answer[] = [$i, $sum];

  }
  
  return $answer;
}

function isSquare($num) {
$y = sqrt($num);
return $y == (int)$y;
}


function sumOfDivisorsSquares($num){
$sum = 0;

for ($Divisor = 1; $Divisor <= round(sqrt($num)); $Divisor++)
{
  if ($num % $Divisor == 0)
  {
    $sum += $Divisor * $Divisor;
    $secondDivisor = $num/$Divisor;
    if ($Divisor !== $secondDivisor) {
      $sum += $secondDivisor * $secondDivisor;
    }
  }
}

return $sum;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class IntegerRecreationTestCases extends TestCase {
  private function revTest($actual, $expected) {
      $this->assertSame($expected, $actual);
  }
  public function testBasics() {
      $this->revTest(listSquared(1, 250), [[1, 1], [42, 2500], [246, 84100]]);
      $this->revTest(listSquared(42, 250), [[42, 2500], [246, 84100]]);
      $this->revTest(listSquared(250, 500), [[287, 84100]]);
      $this->revTest(listSquared(300, 600), []);
  }
}
