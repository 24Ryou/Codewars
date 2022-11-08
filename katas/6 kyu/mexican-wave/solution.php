<!-- mexican-wave -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function wave($people){
  $people = str_split($people);
  $new = [];
  foreach ($people as $i => $val){
    if (ctype_alpha($val)){
      $c = implode("" , array_slice($people , 0 , $i)) . strtoupper($val) . implode("" , array_slice($people , $i+1));
      array_push($new , $c);
    }
  }
  return $new;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function wave($people){
  $result = [];
  
  for($i = 0; $i < strlen($people); $i++) {
    if(ctype_space($people[$i])) continue;
    $result[] = substr_replace($people, strtoupper($people[$i]), $i, 1);
  }
  return $result;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTest extends TestCase
{
    public function testThatSomethingShouldHappen() {
      $this->assertSame(["Hello", "hEllo", "heLlo", "helLo", "hellO"], wave("hello"));
      $this->assertSame(["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"], wave("codewars"));
      $this->assertSame([], wave(""));
      $this->assertSame(["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"], wave("two words"));
      $this->assertSame([" Gap ", " gAp ", " gaP "], wave(" gap "));
    }
}