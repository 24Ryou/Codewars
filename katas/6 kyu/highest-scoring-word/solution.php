<!-- highest-scoring-word -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function high($x) {
  $dic = array();
  foreach (explode(" " , $x) as $word) {
    $sum = array_sum(array_map(function ($c){return ord($c)-96;} , str_split($word)));
    $dic[$word] = $sum;
  }
  return array_search(max($dic) , $dic);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testSampleTests() {
      $this->assertEquals('taxi', high('man i need a taxi up to ubud'));
      $this->assertEquals('volcano', high('what time are we climbing up the volcano'));
      $this->assertEquals('semynak', high('take me to semynak'));
    }
  
    public function testEdgeCaseTests() {
      $this->assertEquals('aa', high('aa b'));
      $this->assertEquals('b', high('b aa'));
      $this->assertEquals('bb', high('bb d'));
      $this->assertEquals('d', high('d bb'));
    }
}