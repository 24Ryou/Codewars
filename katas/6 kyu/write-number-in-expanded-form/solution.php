<!-- write-number-in-expanded-form -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function expanded_form(int $n): string {
  $split = str_split($n);
  $num_digits = count($split);
  $numbers_arr = [];
  foreach ($split as $digit) {
    if ($digit != 0) {
      $numbers_arr[] = $digit . str_repeat(0, $num_digits - 1);
    }
    $num_digits--;
  }
  return implode(' + ', $numbers_arr);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class ExpandedFormTest extends TestCase {
  public function testDescriptionExamples() {
    $this->assertSame("10 + 2", expanded_form(12));
    $this->assertSame("40 + 2", expanded_form(42));
    $this->assertSame("70000 + 300 + 4", expanded_form(70304));
  }
}