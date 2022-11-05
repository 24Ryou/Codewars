<!-- human-readable-duration-format -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function format_duration($seconds)
{

$data = [
  'second'=> floor($seconds) % 60,
  'minute'=> floor($seconds / 60) % 60,
  'hour'  => floor($seconds / (60 * 60)) % 24,
  'day'   => floor($seconds / (60 * 60 * 24)) % 365,
  //'month' => floor($seconds / (60 * 60 * 24 * 30)) % 12,
  'year'  => floor($seconds / (60 * 60 * 24 * 365)),
];

$result = '';
foreach ($data as $key => $interval)
{
  if($interval != 0) {
    $tmp = $interval.' '.$key.($interval > 1 ? 's' : '');
    $result = empty($result) ? $tmp : $tmp.', '.$result;
  }
}

return empty($result) ? 'now' : str_lreplace(',', ' and', $result);
}
    
function str_lreplace($search, $replace, $subject){
    $pos = strrpos($subject, $search);
    if($pos !== false)    {
        $subject = substr_replace($subject, $replace, $pos, strlen($search));
    }
    return $subject;
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MyTest extends TestCase {
  public function testExample() {
    $this->assertSame("1 second", format_duration(1));
    $this->assertSame("1 minute and 2 seconds", format_duration(62));
    $this->assertSame("2 minutes", format_duration(120));
    $this->assertSame("1 hour", format_duration(3600));
    $this->assertSame("1 hour, 1 minute and 2 seconds", format_duration(3662));
  }
}