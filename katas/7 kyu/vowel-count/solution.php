<!-- vowel-count -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function getCount($str) {
  $vowelsCount = 0;
  $vowel = 'aeiou';
  foreach (str_split($str) as $chr) {
    if (strpos($vowel , $chr) !== false){
      $vowelsCount++;
    }
  }
  return $vowelsCount;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function getCount($str) {;
  return preg_match_all('/[aeiou]/i',$str,$matches);
}
/* ---------------------------------- TEST ---------------------------------- */
class VovelCountCase extends TestCase
{
    public function testBasics() {
      $this->assertEquals(5, getCount("abracadabra"));
    }
}