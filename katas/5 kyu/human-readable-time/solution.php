<!-- human-readable-time -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function human_readable($seconds) {

  $hour = $seconds/3600;
  $minute = ($hour - (int)$hour) * 60;
  $second = ($minute - (int)$minute) * 60;

  return sprintf("%02d:%02d:%02d", $hour , $minute , round($second));
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function human_readable(int $seconds): string
{
  return sprintf('%02d:%02d:%02d', $seconds / 3600, ($seconds % 3600) / 60, $seconds % 60);
}
/* ---------------------------------- TEST ---------------------------------- */
class MyExampleTestCases extends TestCase  {
  
  public function testBasicTests(){
  $this->assertSame('00:00:00', human_readable(0));
  $this->assertSame('00:00:05', human_readable(5));
  $this->assertSame('00:01:00', human_readable(60));
  $this->assertSame('23:59:59', human_readable(86399));
  $this->assertSame('99:59:59', human_readable(359999));
  }
}