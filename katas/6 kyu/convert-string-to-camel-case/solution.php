<!-- convert-string-to-camel-case -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function toCamelCase($str){
  $old = strpos($str , '_') ? explode("_" , $str) : explode("-" , $str);
  $new = array_map('ucwords' , $old);
  array_shift($new);
  array_unshift($new , $old[0]);
  return implode("" , $new);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function toCamelCase($str){
  return preg_replace_callback("~[_-](\w)~", function($m) { return strtoupper($m[1]); }, $str);
}
/* ---------------------------------- TEST ---------------------------------- */
class TestCases extends TestCase {
  public function testSampleCases() {
    $this->assertEquals("theStealthWarrior", toCamelCase("the_stealth_warrior"), "toCamelCase('the_stealth_warrior') did not return correct value");
    $this->assertEquals("theStealthWarrior", toCamelCase("the-Stealth-Warrior"), "toCamelCase('the-Stealth-Warrior') did not return correct value");
  }
}
