<!-- youre-a-square -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function isSquare($n){
  return sqrt($n) === floor(sqrt($n)) ? true : false;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class IsSquareTest extends TestCase
{
    public function testShouldWorkForSomeExamples() {
        $this->assertFalse(isSquare(-1), "Negative numbers cannot be square numbers");
        $this->assertTrue(isSquare(0));       
        $this->assertFalse(isSquare(3));
        $this->assertTrue(isSquare(4));
        $this->assertTrue(isSquare(25));
        $this->assertFalse(isSquare(26));
    }
}