<!-- unique-in-order -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function uniqueInOrder($iterable){
  $arr = array();

  if (gettype($iterable) === "string") {
    if (strlen($iterable) < 2) return $iterable == "" ? [] : [$iterable];
    else $iterable = str_split($iterable);
  }

  array_push($arr,$iterable[0]);
  foreach (range(0 , count($iterable)-2)  as $i){
    if ($iterable[$i] != $iterable[$i+1]) array_push($arr , $iterable[$i+1]);
  }
  return $arr;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function uniqueInOrder($iterable){ 
  $arr = is_string($iterable) ? str_split($iterable) : $iterable;
  $ret = array_reduce($arr, function($carry, $item) {
    if ($item != end($carry)) {
      $carry[] = $item;
    }
    return $carry;
  }, []);
  
  return $ret;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    // test function names should start with "test"
    public function testSampleTest() {
      $this->assertSame(['A','B','C','D','A','B'], uniqueInOrder('AAAABBBCCDAABBB'));
      $this->assertSame([], uniqueInOrder(''));
      $this->assertSame(['A'], uniqueInOrder('A'));
    }
}