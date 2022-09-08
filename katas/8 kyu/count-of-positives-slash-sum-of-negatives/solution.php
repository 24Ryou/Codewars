<!-- count-of-positives-slash-sum-of-negatives -->
<?php
use PHPUnit\Framework\TestCase;

use function PHPUnit\Framework\isEmpty;

/* ------------------------------- MY SOLUTION ------------------------------ */
function countPositivesSumNegatives($input) {
  $c = 0;
  $s = 0;
  if (empty($input)){
    return [];
  }
  foreach ($input as $item){
    if ($item > 0) {
      $c += 1;
    }
    else {
      $s += $item;
    }
  }
  return [$c , $s];
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function countPositivesSumNegatives($input) {

  if (empty($input)) return [];

  $positive = 0;
  $negative = 0;
  foreach($input as $number) {
    $number > 0 ? $positive++ : $negative += $number;
  }
  
  return [$positive, $negative];
}
/* ---------------------------------- TEST ---------------------------------- */
class CountPositivesSumNegativesTestCases extends TestCase
{
    public function testExample() {
      $this->assertSame([10, -65], countPositivesSumNegatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]));
      $this->assertSame([8, -50], countPositivesSumNegatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]));
    }
}