<!-- find-the-missing-letter -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function find_missing_letter(array $array): string {
  $c = ord($array[0]);
  foreach ($array as $chr) {
    if ($c == ord($chr)) {
      $c++;
    }
    else return chr($c);
  }
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function find_missing_letter(array $array): string {
  $alphabet = range($array[0], $array[count($array) - 1]);
  return array_values(array_diff($alphabet, $array))[0];
}
/* ---------------------------------- TEST ---------------------------------- */
class FindTheMissingLetterTest extends TestCase {
  public function testDescriptionExamples() {
    $this->assertEquals("e", find_missing_letter(['a','b','c','d','f']));
    $this->assertEquals("P", find_missing_letter(["O", "Q", "R", "S"]));
  }
}