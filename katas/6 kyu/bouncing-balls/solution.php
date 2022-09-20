<!-- bouncing-balls -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function bouncingBall($h, $bounce, $window){
  if ($h <= 0 or $bounce <= 0 or $bounce >= 1 or $window >= $h){
    return -1;
  }
  return 2 + bouncingBall($h * $bounce, $bounce, $window);
}
/* ---------------------------------- TEST ---------------------------------- */
class BouncingBallCases extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertEquals($expected, $actual);
    }
    public function testBasics() {
        $this->revTest(bouncingBall(3.0, 0.66, 1.5) , 3);
        $this->revTest(bouncingBall(30.0, 0.66, 1.5), 15);
        $this->revTest(bouncingBall(10, 0.6, 10), -1);
    }
}