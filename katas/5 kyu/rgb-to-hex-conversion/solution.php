<!-- rgb-to-hex-conversion -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function rgb($r,$g,$b){
  var_dump("Debugging:", ['r'=>$r, 'g'=>$g, 'b'=>$b]);
  return sprintf("%02X%02X%02X", chk($r), chk($g), chk($b));
}
function chk ($n) { return $n > 255 ? 255 : ($n < 0 ?  0 : $n);}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testBaseTests() {
    // assertEquals(mixed $expected, mixed $actual[, string $message = ''])
      $this->assertSame("FFFFFF", rgb(255, 255, 255));
      $this->assertSame("FFFFFF", rgb(255, 255, 300));
      $this->assertSame("000000", rgb(0,0,0));
      $this->assertSame("000000", rgb(-500,0,0));
      $this->assertSame("9400D3", rgb(148, 0, 211));
    }
}