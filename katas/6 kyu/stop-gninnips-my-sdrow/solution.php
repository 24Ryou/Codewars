<!-- stop-gninnips-my-sdrow -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function spinWords(string $str): string {
  $words = explode(" " , $str);
  $result = array();
  foreach($words as $word){
    if (strlen($word) >= 5) {
      $word = strrev($word);
    }
    array_push($result , $word);
  }
  return implode(" " , $result);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function spinWords(string $str): string {
  return preg_replace_callback('/\w{5,}/', function($matches) {return strrev($matches[0]);}, $str);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testBasicTests() {
      $this->assertEquals("emocleW", spinWords("Welcome"));
      $this->assertEquals("Hey wollef sroirraw", spinWords("Hey fellow warriors"));
      $this->assertEquals("This is a test", spinWords("This is a test"));
      $this->assertEquals("This is rehtona test", spinWords("This is another test"));
      $this->assertEquals("You are tsomla to the last test", spinWords("You are almost to the last test"));
      $this->assertEquals("Just gniddik ereht is llits one more", spinWords("Just kidding there is still one more"));
      $this->assertEquals("ylsuoireS this is the last one", spinWords("Seriously this is the last one"));
    }
}