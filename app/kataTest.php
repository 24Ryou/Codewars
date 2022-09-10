<!-- fake-binary -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function fake_bin(string $s): string {
  $r = '';
  foreach (str_split($s) as $digit) {
    if (+$digit >= 5){
      $r.="1";
    }
    else {
      $r.= "0";
    }
  }
  return $r;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function fake_bin(string $s): string {
  return strtr($s, '0123456789', '0000011111');
}
/* ------------------------------ BEST PRACTICE ----------------------------- */
function fake_bin(string $s): string {
  return preg_replace(array('/[0-4]/', '/[5-9]/'), array('0', '1'), $s);
}
/* ---------------------------------- TEST ---------------------------------- */
class FakeBinTest extends TestCase {
  public function testExamples() {
    $this->assertEquals('01011110001100111', fake_bin('45385593107843568'));
    $this->assertEquals('101000111101101', fake_bin('509321967506747'));
    $this->assertEquals('011011110000101010000011011', fake_bin('366058562030849490134388085'));
  }
}