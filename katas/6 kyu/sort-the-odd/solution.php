<!-- sort-the-odd -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function sortArray(array $arr) : array {
  $odd = [];
  foreach ($arr as $key=>$item){
    if ($item % 2 != 0){
      $odd[]=$item;
      $arr[$key] = "odd";
    }
  }
  rsort($odd);
  foreach ($arr as $key=>$item){
    if ($item == "odd"){
      $arr[$key] = array_pop($odd);
    }
  }
  return $arr;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class ExampleTest extends TestCase
{
    public function testBasic() {
      $this->assertEquals([1, 3, 2, 8, 5, 4], sortArray([5, 3, 2, 8, 1, 4]));
      $this->assertEquals([1, 3, 5, 8, 0], sortArray([5, 3, 1, 8, 0]));
      $this->assertEquals([], sortArray([]));
    }
}
