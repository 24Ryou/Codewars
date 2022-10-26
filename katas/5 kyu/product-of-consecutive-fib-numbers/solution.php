<!-- product-of-consecutive-fib-numbers -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function productFib($prod) {
  $test = function ($i) { return fib($i) * fib($i+1); };
  $i = 0;
  while ($test($i) < $prod) {
    $i++;
  }
  return $test($i) == $prod ? [fib($i) , fib($i+1) , true] : [fib($i) , fib($i+1) , false];
}

function fib($n) { return (int)round(pow((sqrt(5)+1)/2, $n) / sqrt(5));}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class FibProductTestCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertSame($expected, $actual);
    }
    public function testBasics() {        
      $this->revTest(productFib(4895), [55, 89, true]);
      $this->revTest(productFib(5895), [89, 144, false]);
      $this->revTest(productFib(74049690), [6765, 10946, true]);
    }
}