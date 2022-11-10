<!-- encrypt-this -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function encryptThis($text): string
{
  $arr = explode(" " ,$text);
  if ($arr == ['']) return "";
  $arr = array_map(function($x){
    $arrWord = str_split($x);
    if (count($arrWord) > 2) return "" . ord($arrWord[0]) . end($arrWord) . implode("" , array_slice($arrWord , 2 , -1)) . $arrWord[1];
    elseif (count($arrWord) == 2) return "" . ord($arrWord[0]) . end($arrWord);
    else return "" . ord($arrWord[0]);
  } , $arr);
  return implode(" " , $arr);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function encryptThis($text): string {
  return preg_replace_callback('/\b\w(\w?)(\w*?)(\w?)\b/', fn($m) => ord($m[0]).$m[3].$m[2].$m[1], $text);
}
/* ---------------------------------- TEST ---------------------------------- */

class ExampleTest extends TestCase
{
  public function testSimple()
  {
    $this->assertSame("65", encryptThis("A"));
    $this->assertSame("65 119esi 111dl 111lw 108dvei 105n 97n 111ka", encryptThis("A wise old owl lived in an oak"));
    $this->assertSame("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp", encryptThis("The more he saw the less he spoke"));
    $this->assertSame("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare", encryptThis("The less he spoke the more he heard"));
    $this->assertSame("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri", encryptThis("Why can we not all be like that wise old bird"));
    $this->assertSame("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple", encryptThis("Thank you Piotr for all your help"));
  }
}