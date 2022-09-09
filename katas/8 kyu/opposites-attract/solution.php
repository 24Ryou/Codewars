<!-- opposites-attract -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function lovefunc($flower1, $flower2) {
  return $flower1%2 != $flower2%2 ? true : false;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function lovefunc(int $flower1, int $flower2) : bool {
  return ($flower1 % 2 !== $flower2 % 2);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testExample() {
        $this->assertTrue(lovefunc(1, 4));
        $this->assertFalse(lovefunc(2, 2));
        $this->assertTrue(lovefunc(0, 1));
        $this->assertFalse(lovefunc(0, 0));
    }
}