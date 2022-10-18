<!-- can-you-get-the-loop -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function loop_size($node): int {
  $p1 = $node->getNext();
  $p2 = $node->getNext()->getNext();
  while ($p1 !== $p2) {
    $p1 = $p1->getNext();
    $p2 = $p2->getNext()->getNext();
  }
  $res = 1;
  $p2 = $p2->getNext();
  while ($p1 !== $p2) {
    $p2 = $p2->getNext();
    $res++;
  }
  return $res;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class LoopSizeTest extends TestCase {
  public function testFixed() {
    $this->assertSame(1, loop_size(Node::createChain(0, 1)));
    $this->assertSame(23, loop_size(Node::createChain(8778, 23)));
    $this->assertSame(8778, loop_size(Node::createChain(23, 8778)));
  }
}