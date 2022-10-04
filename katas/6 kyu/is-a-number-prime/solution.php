<!-- is-a-number-prime -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function is_prime(int $n): bool {
  var_dump($n);
  if ($n <= 1) return false;
  if ($n == 2) return true;
  foreach (range(2 , intval($n**(0.5))+1) as $i){
    if ($n % $i == 0) return false;
  }
  return true;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
final class IsPrimeTest extends TestCase {
  public function testExamples() {
    $this->assertFalse(is_prime(0));
    $this->assertFalse(is_prime(1));
    $this->assertTrue(is_prime(2));
    $this->assertTrue(is_prime(5), 'Your function should work for the example provided in the Kata Description');
  }
}