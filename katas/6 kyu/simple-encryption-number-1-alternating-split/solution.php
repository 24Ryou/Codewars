<!-- simple-encryption-number-1-alternating-split -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function encrypt($text, $n) {
  if (!empty($text) && $n > 0){
    $array = str_split($text);
    foreach(range(0,$n-1) as $i){
      $odd = array_filter($array, function ($input) {return $input & 1;}, ARRAY_FILTER_USE_KEY);
      $even = array_filter($array, function ($input) {return !($input & 1);}, ARRAY_FILTER_USE_KEY);
      $array = array_merge($odd,$even);
    }
    return implode("",$array);
  }
  else return $text;
}

function decrypt($text, $n) {
  if (!empty($text) && $n > 0){
    $arr = str_split($text);
    $hlf = count($arr)/2;
    foreach(range(0,$n-1) as $i){
      $result = array();
      $odd = array_slice($arr,0,$hlf);
      $even = array_slice($arr,$hlf);
      while(!empty($odd) || !empty($even)) {
        if(!empty($even)) {
          $result[] = array_shift($even);
        }
        if(!empty($odd)) {
          $result[] = array_shift($odd);
        }
      }
      $arr = $result;
    }
    return implode("",$arr);
  }
  else return $text;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function encrypt($text, $n) {
  if ($n <= 0) return $text;
  
  $result = $text;
  
  for ($i = 0; $i < $n; $i++) {
    $map  = str_split($result, 1);
    $even = array_filter($map, function($k) { return ($k % 2 === 0); }, ARRAY_FILTER_USE_KEY);
    $odd  = array_filter($map, function($k) { return ($k % 2 !== 0); }, ARRAY_FILTER_USE_KEY);
  
    $result = implode('', $odd) . implode('', $even);
  }

  return $result;
}

function decrypt($text, $n) {
  if ($n <= 0) return $text;
  
  $result = $text;
  
  for ($i = 0; $i < $n; $i++) {
    $map  = str_split($result, 1);
    $even = array_slice($map, 0, floor(count($map) / 2));
    $odd  = array_slice($map, floor(count($map) / 2));
  
    $result = '';
    for ($x = 0; $x < count($map); $x++) {
      $result .= ($x % 2 === 0) ? array_shift($odd) : array_shift($even);
    }

  }

  return $result;
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testEncryptExampleTests() {  
        $this->assertSame("This is a test!", encrypt("This is a test!", 0));
        $this->assertSame("hsi  etTi sats!", encrypt("This is a test!", 1));
        $this->assertSame("s eT ashi tist!", encrypt("This is a test!", 2));
        $this->assertSame(" Tah itse sits!", encrypt("This is a test!", 3));
        $this->assertSame("This is a test!", encrypt("This is a test!", 4));
        $this->assertSame("This is a test!", encrypt("This is a test!", -1));
        $this->assertSame("hskt svr neetn!Ti aai eyitrsig", encrypt("This kata is very interesting!", 1));
    }
    public function testDecryptExampleTests() {   
        $this->assertSame("This is a test!", decrypt("This is a test!", 0));
        $this->assertSame("This is a test!", decrypt("hsi  etTi sats!", 1));
        $this->assertSame("This is a test!", decrypt("s eT ashi tist!", 2));
        $this->assertSame("This is a test!", decrypt(" Tah itse sits!", 3));
        $this->assertSame("This is a test!", decrypt("This is a test!", 4));
        $this->assertSame("This is a test!", decrypt("This is a test!", -1));
        $this->assertSame("This kata is very interesting!", decrypt("hskt svr neetn!Ti aai eyitrsig", 1));
    }
    public function testNullorEmpty() {
        $this->assertSame("", encrypt("", 0));
        $this->assertSame("", decrypt("", 0));
        $this->assertSame(null, encrypt(null, 0));
        $this->assertSame(null, decrypt(null, 0));
    }
}