<!-- next-bigger-number-with-the-same-digits -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function nextBigger($n)
{
  $o = biggerNumber($n);
  for($i = $n+1; $i <= $o; $i++) {
    if(biggerNumber($i) === $o) {
      return $i;
    }
  }
  
  return -1;
}

function biggerNumber($n) {
  $n = str_split(''.$n);
  rsort($n);
  
  return (int) join($n);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */

class KataTest extends TestCase {
  public function testBasicTests() {
    $this->assertSame(21, nextBigger(12));
    $this->assertSame(531, nextBigger(513));
    $this->assertSame(2071, nextBigger(2017));
    $this->assertSame(441, nextBigger(414));
    $this->assertSame(414, nextBigger(144));
    $this->assertSame(123456798, nextBigger(123456789));
    $this->assertSame(1234567908, nextBigger(1234567890));
    $this->assertSame(-1, nextBigger(9876543210));
    $this->assertSame(-1, nextBigger(9999999999));
    $this->assertSame(59884848483559, nextBigger(59884848459853));
  }
}