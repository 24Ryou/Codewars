<!-- multiples-of-3-or-5 -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function solution($number){
  // return array_sum(array_filter(range(1 , $number-1) , fn($x)=> $x%3 == 0 or $x%5 == 0 ? $x : null)); // phpunit 8
  return array_sum(array_filter(range(1 , $number-1) , function($x){ if($x%3 == 0 or $x%5 == 0) return $x;})); // phpunit 7
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class SolutionFunction extends TestCase
{
  public function testBasics() {
    $this->assertEquals(23, solution(10));
  }
}