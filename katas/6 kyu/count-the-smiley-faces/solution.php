<!-- count-the-smiley-faces -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function count_smileys($arr): int {
  return count(preg_grep("/[:;][-~]?[)D]/" , $arr));
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase {
  public function testBasics() {
    $this->assertEquals(0, count_smileys([]));
    $this->assertEquals(4, count_smileys([':D',':~)',';~D',':)']));
    $this->assertEquals(2, count_smileys([':)',':(',':D',':O',':;']));
    $this->assertEquals(1, count_smileys([';]', ':[', ';*', ':$', ';-D']));
  }
}