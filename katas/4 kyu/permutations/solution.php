<!-- permutations -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function permutations(string $str): array
{
  if (strlen($str) < 2) {
    return [$str];
  }

  $result = [];
  $stop = strlen($str) - 1;
  for ($i = 0; $i <= $stop; $i++) {
    $substr = substr($str, 0, $i) . substr($str, $i + 1);
    foreach (permutations($substr) as $per) {
      $result[] = $str[$i] . $per;
    }
  }
  return array_unique($result);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
final class PermutationsTest extends TestCase {
  private function assertEquivalent(array $expected, array $actual, string $msg = '') {
    sort($expected);
    sort($actual);
    $this->assertSame($expected, $actual, $msg);
  }
  public function testDescriptionExamples() {
    $this->assertEquivalent(['a'], permutations('a'));
    $this->assertEquivalent(['ab', 'ba'], permutations('ab'));
    $this->assertEquivalent(['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'], permutations('aabb'));
  }
}