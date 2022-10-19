<!-- find-the-unique-string -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function find_uniq($arr) {

  if (in_array("" , $arr) || in_array(" " , $arr)){
    $arr = array_filter( $arr , fn($x) => $x != "" && $x != " "); return end($arr);
  }
  
  $cn = function(String $str) { $r = array_unique(str_split(strtolower($str))) ; sort($r) ; return implode("" , $r);};

  $s = $w = array_map($cn , $arr);
  sort($s);
  $ndx = $s[0] == $s[1] ? array_keys($w , end($s)) : array_keys($w , $s[0]);
  return $arr[$ndx[0]];
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class FindUniqTest extends TestCase
{
  // test function names should start with "test"
  public function testSampleCases() {
    $this->assertSame('BbBb', find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]));
    $this->assertSame('foo', find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]));
    $this->assertSame('victor', find_uniq([ 'silvia', 'vasili', 'victor' ]));
    $this->assertSame('Harry Potter', find_uniq([ 'Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter' ]));
    $this->assertSame('a', find_uniq([ '     ', 'a', ' ' ]));
  }
}