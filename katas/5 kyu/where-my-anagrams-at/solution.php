<!-- where-my-anagrams-at -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function anagrams(string $word, array $words): array {
  $z = array_filter($words , function($x) use ($word) {
    $a = str_split($x);
    $b = str_split($word);
    sort($a);
    sort($b);
    if ($a == $b) return $x;
  });
  return array_values($z);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
final class AnagramsTest extends TestCase {
  public function testExamples() {
    $this->assertEquals(['a'], anagrams('a', ['a', 'b', 'c', 'd']));
    $this->assertEquals(['carer', 'arcre', 'carre'], anagrams('racer', ['carer', 'arcre', 'carre', 'racrs', 'racers', 'arceer', 'raccer', 'carrer', 'cerarr']));
    $this->assertEquals(['aabb', 'bbaa'], anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), 'Your function should work for an example provided in the Kata Description');
    $this->assertEquals(['carer', 'racer'], anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), 'Your function should work for an example provided in the Kata Description');
    $this->assertEquals([], anagrams('laser', ['lazing', 'lazy',  'lacer']), 'Your function should work for an example provided in the Kata Description');
  }
}