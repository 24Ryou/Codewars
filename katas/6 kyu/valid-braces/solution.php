<!-- valid-braces -->
<?php
use PHPUnit\Framework\TestCase;

use function PHPUnit\Framework\any;

/* ------------------------------- MY SOLUTION ------------------------------ */
function validBraces($braces){
  while (strpos($braces, '{}') !== false || strpos($braces, '()') !== false || strpos($braces, '[]') !== false) {
    $braces = str_replace("{}" , "" , $braces);
    $braces = str_replace("()" , "" , $braces);
    $braces = str_replace("[]" , "" , $braces);
  }
  return $braces === "";
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function validBraces($braces){
  do {
    $braces = str_replace(['()', '[]', '{}'], '', $braces, $count);
  } while ($count);

  return empty($braces);  
}
/* ---------------------------------- TEST ---------------------------------- */
class ValidBracesTestCases extends TestCase
{
    public function testSamples() {
      $this->assertSame(true, validBraces("()"));
      $this->assertSame(false, validBraces("[(])"));
      $this->assertSame(false, validBraces("(})"));
      $this->assertSame(false, validBraces(")(}{]["));
      $this->assertSame(false, validBraces("())({}}{()][]["));
      $this->assertSame(true, validBraces("({})[({})]"));
      $this->assertSame(true, validBraces("(({{[[]]}}))"));
      $this->assertSame(true, validBraces("{}({})[]"));
    }
}