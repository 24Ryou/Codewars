<!-- the-observed-pin -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function getPINs($observed) {
  $variants = [
    "1" => ["1", "2", "4"],
    "2" => ["1", "2", "3", "5"],
    "3" => ["2", "3", "6"],
    "4" => ["1", "4", "5", "7"],
    "5" => ["2", "4", "5", "6", "8"],
    "6" => ["3", "5", "6", "9"],
    "7" => ["4", "7", "8"],
    "8" => ["5", "7", "8", "9", "0"],
    "9" => ["6", "8", "9"],
    "0" => ["8", "0"]
  ];
  
  $digits = str_split($observed);
  $result = $variants[array_shift($digits)];
  if($digits){
    $result = array_reduce($digits, function($result, $digit) use ($variants){
      $rr = [];
      foreach($result as $r){
        foreach($variants[$digit] as $m){
          $rr[] = $r.$m;          
        }
      }
      return $rr; 
    }, $result);
  }
  return $result;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MyTest extends TestCase
{
    // test function names should start with "test"
    public function testSample() {
        $expectations = [
            "8" => ["5", "7", "8", "9", "0"], 
            "11" => ["11", "22", "44", "12", "21", "14", "41", "24", "42"], 
            "369" => ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"], 
        ];
        foreach ($expectations as $pin => $expect) {
            $actual = getPINs($pin);
            sort($actual);
            sort($expect);
            $this->assertSame($expect, $actual);
        }
    }
}