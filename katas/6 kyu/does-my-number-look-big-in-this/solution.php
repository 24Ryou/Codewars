<!-- does-my-number-look-big-in-this -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function narcissistic(int $value): bool {
  $string = strval($value);
  $pow = strlen($string);
  $result = array();
  foreach (str_split($string) as $digit) {
    array_push($result , $digit**$pow);
  }
  return array_sum($result) == $value ? true : false;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function narcissistic(int $value): bool {
  $digitCount = strlen($value);
  
  foreach(str_split($value) as $digit){
    $value -= pow($digit, $digitCount);
  }
  
  return $value === 0;
}
/* ---------------------------------- TEST ---------------------------------- */
class NarcissisticTest extends TestCase {
  public function testExamples() {
    $this->assertTrue(narcissistic(7), '7 is narcissistic');
    $this->assertTrue(narcissistic(371), '371 is narcissistic');
  }
}