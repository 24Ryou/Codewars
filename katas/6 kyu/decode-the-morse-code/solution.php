<!-- decode-the-morse-code -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function morse($chr) {
  $MORSE_CODE = [
    '.-'=> 'A', '-...'=> 'B', '-.-.'=> 'C', '-..'=> 'D', '.'=> 'E', '..-.'=> 'F',
    '--.'=> 'G', '....'=> 'H', '..'=> 'I', '.---'=> 'J', '-.-'=> 'K', '.-..'=> 'L',
    '--'=> 'M', '-.'=> 'N', '---'=> 'O', '.--.'=> 'P', '--.-'=> 'Q', '.-.'=> 'R',
    '...'=> 'S', '-'=> 'T', '..-'=> 'U', '...-'=> 'V', '.--'=> 'W', '-..-'=> 'X',
    '-.--'=> 'Y', '--..'=> 'Z',
    '-----'=> '0', '.----'=> '1', '..---'=> '2', '...--'=> '3', '....-'=> '4',
    '.....'=> '5', '-....'=> '6', '--...'=> '7', '---..'=> '8', '----.'=> '9',
    '.-.-.-'=> '.', '--..--'=> ',', '..--..'=> '?', '.----.'=> "'", '-.-.--'=> '!',
    '-..-.'=> '/', '-.--.'=> '(', '-.--.-'=> ')', '.-...'=> '&', '---...'=> '=>',
    '-.-.-.'=> ';', '-...-'=> '=', '.-.-.'=> '+', '-....-'=> '-', '..--.-'=> '_',
    '.-..-.'=> '"', '...-..-'=> '$', '.--.-.'=> '@', '...---...'=> 'SOS'
  ];
  return $MORSE_CODE[$chr];
}

function decode_morse(string $code): string {
  $result = array();
  $code = trim($code);
  $words = explode("   " , $code);
  foreach ($words as $word) {
    $chrs = explode(" " , $word);
    $temp = array_map('morse', $chrs);
    array_push($result , implode("",$temp));
    ;
  }
  return implode(" " , $result);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function decode_morse(string $code): string {
  return strtr(trim($code), MORSE_CODE + ['  ' => ' ',' ' => '']);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testBasicCases() {
        $this->assertEquals('HEY JUDE', decode_morse('.... . -.--   .--- ..- -.. .'));
    }
}