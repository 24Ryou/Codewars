<!-- square-every-digit -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function square_digits($num){
  $num = str_split(strval($num) , 1);
  $r = '';
  foreach ($num as $digit) {
    $r .= strval(intval($digit**2));
  }
  return intval($r);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    // test function names should start with "test"
    public function testBasics() {
      $this->assertEquals(square_digits(9119), 811181);
      $this->assertEquals(41636640, square_digits(24680));
      $this->assertEquals(19254981, square_digits(13579));
      $this->assertEquals(square_digits(0), 0);
    }
}