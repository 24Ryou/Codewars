<!-- create-phone-number -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function createPhoneNumber($numbersArray) {
  $a1 = implode("" , array_slice($numbersArray , 0 , 3));
  $a2 = implode("" , array_slice($numbersArray , 3 , 3));
  $a3 = implode("" , array_slice($numbersArray , 6));
  return '('.$a1.')'.' '.$a2.'-'.$a3;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function createPhoneNumber(array $digits): string {
  return sprintf("(%d%d%d) %d%d%d-%d%d%d%d", ...$digits);
}

function createPhoneNumber($numbersArray) {
  preg_match('/(\d{3})(\d{3})(\d{4})/', implode('', $numbersArray), $matches);
  return '('.$matches[1].') '.$matches[2].'-'.$matches[3];
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase {
  public function testBasicTests() {
    $this->assertEquals('(123) 456-7890', createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));
    $this->assertEquals('(111) 111-1111', createPhoneNumber([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]));
  }
}