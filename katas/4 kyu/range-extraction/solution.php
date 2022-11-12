<!-- range-extraction -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function solution(array $list): string
{
  $str = '';
  for($i = 0; $i < count($list) - 1;){
    if ($list[$i] + 1 < $list[$i + 1]){
      $str .= $list[$i] . ',';
      $i++;
    }else{
      $str .= $list[$i];
      $val = $list[$i];
      while ($i < count($list) - 1 && $list[$i] + 1 == $list[$i + 1]){
        $i++;
      }
      $str .= $list[$i] - $val == 1 ? ',' : '-';
    }
  }
  return $str . $list[count($list) - 1];
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class ExampleTest extends TestCase
{
    /**
     * @test
     */
    public function example(): void
    {
        self::assertSame(
            '-6,-3-1,3-5,7-11,14,15,17-20',
            solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
        );
    }
}
