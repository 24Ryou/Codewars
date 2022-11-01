<!-- weight-for-weight -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function orderWeight($str) {
  $nums = explode(" ", $str);
  
  usort($nums, function ($a, $b) {
    $sumA = array_sum(str_split((string) $a));
    $sumB = array_sum(str_split((string) $b));
    
    if ($sumA === $sumB) return strcmp($a, $b);
    
    return $sumA > $sumB;
  });
  
  
  return implode(' ', $nums);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class OrderWeightTestCases extends TestCase
{
    public function testBasics() {
      $this->assertSame("2000 103 123 4444 99", orderWeight("103 123 4444 99 2000"));
      $this->assertSame("11 11 2000 10003 22 123 1234000 44444444 9999", orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123"));
    }
}