<!-- sum-without-highest-and-lowest-number -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function sumArray($array) {
  sort($array , SORT_NUMERIC);
  array_shift($array);
  array_pop($array);
  return array_sum($array);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function sumArray( $array ) {
  return array_sum( $array ) - ( max( $array ) + min( $array ) );
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testExample() {
        $this->assertSame(16, sumArray([6, 2, 1, 8, 10]));
    }
}