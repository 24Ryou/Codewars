<!-- detect-pangram -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function detect_pangram($string) { 

  $text = trim(strtolower($string));
  $letters = str_split("thequickbrownfoxjumpsoverthelazydog");

  foreach ($letters as $letter){
    if (!strstr($text , $letter)) {
      return false;
    }
  }

  return true;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyExampleTestCases extends TestCase {
  public function testBasicTests() {
  # Pangrams:
  $result4 = detect_pangram("The quick brown fox jumps over the lazy dog.");
  $this->assertEquals(true, $result4);
  $result5 = detect_pangram("1L%r+f4G!e7w V z q6M h4d F3b+t O2n e K^g+c#S^i4i X7c-u P5d7j Y6a(a B");
  $this->assertEquals(true, $result5);
  
  # Not pangrams:
  $result1 = detect_pangram("A pangram is a sentence that contains every single letter of the alphabet at least once.");
  $this->assertEquals(false, $result1 );
  $result2 = detect_pangram("5B!e i J x*p F h d!A:o q D y n6L%u9i.G9f2g4C a h+K!m+z:R t!j:B w s C");
  $this->assertEquals(false, $result2);
  }
}