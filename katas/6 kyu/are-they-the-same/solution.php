<!-- are-they-the-same -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function comp($a1, $a2) {
  
  if ( is_null($a1) || is_null($a2) )
    return false;
    
  $t = array_map(function($v) {
    return $v * $v;
  }, $a1);
  
  sort($a2);
  sort($t);
  return $a2 == $t;
}
/* ---------------------------------- TEST ---------------------------------- */
class AreTheyTheSameTest extends TestCase
{
    private function revTest($actual, $expected) {
        $this->assertEquals($expected, $actual);
    }
    public function testBasics() {        
        $a1 = [121, 144, 19, 161, 19, 144, 19, 11];
        $a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19];
        $this->revTest(comp($a1, $a2), true);
        $a1 = [121, 144, 19, 161, 19, 144, 19, 11];
        $a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19];
        $this->revTest(comp($a1, $a2), false);
    }
}