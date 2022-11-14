<!-- strings-mix -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function mix($s1, $s2) {
  $c1 = count_chars($s1);
  $c2 = count_chars($s2);
      
  $out = [];
  for ($byte = ord("a"); $byte <= ord("z"); $byte++) {
    $num = max($c1[$byte], $c2[$byte]);
    if ($num > 1) {
      $out[] = [-1 => 2, "=", 1][$c1[$byte] <=> $c2[$byte]] . ":" . str_repeat(chr($byte), $num);
    }
  }
  usort($out, function($a, $b) {
    return strlen($b) <=> strlen($a) ?: $a <=> $b;
  });
  
  return implode("/", $out);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MixTest extends TestCase {
  private function revTest($actual, $expected) {
      $this->assertSame($expected, $actual);
  }
  public function testCountOnesBasics() {
      $this->revTest(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr");
      $this->revTest(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg");
      $this->revTest(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt");
  }
}