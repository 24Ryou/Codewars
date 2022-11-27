<!-- grasshopper-terminal-game-combat-function-1 -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function combat($health, $damage) {
  return $damage > $health ? 0 : $health - $damage;  
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MyTest extends TestCase
{
    public function testSample() {
      $this->assertSame(95, combat(100, 5));
      $this->assertSame(84, combat(92, 8));
      $this->assertSame(0, combat(20, 30));
    }
}