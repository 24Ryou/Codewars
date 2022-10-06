<!-- persistent-bugger -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function persistence(int $num): int {
  $c = 0;
  while ($num > 9){
    $n = array_map('intval' , str_split($num));
    $num = array_reduce($n , fn($x ,$y) => $x*$y, 1);
    $c++;
  }
  return $c;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function persistence(int $num): int {
  $count = 0;
  while ($num > 9) {
    $num = array_product(str_split($num));
    $count++;
  }
  return $count;
}
/* ---------------------------------- TEST ---------------------------------- */
class PersistenceTest extends TestCase {
  public function testDescriptionExamples() {
    $this->assertEquals(3, persistence(39));
    $this->assertEquals(4, persistence(999));
    $this->assertEquals(0, persistence(4));
  }
}