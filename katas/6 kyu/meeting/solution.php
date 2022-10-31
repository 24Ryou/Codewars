<!-- meeting -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function meeting(string $s): string {
  $result = array_map(function($pair) {
    return vsprintf('(%s, %s)', array_reverse(explode(':', $pair)));
  }, explode(';', strtoupper($s)));
  sort($result);
  return implode($result);
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
/* ---------------------------------- TEST ---------------------------------- */
class MeetingTestCases extends TestCase {

  public function dotest($s, $expect) {
      printf("s: %s\r\n", $s);
      $actual = meeting($s);
      printf("Actual: %s\r\n", $actual);
      printf("Expect: %s\r\n", $expect);
      $this->assertSame($expect, $actual);
      printf("%s\r\n", "-");
  }

  public function testBasics() {        
      $this->dotest("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:KERN;Megan:Stan;Alex:Korn", 
          "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)");
      $this->dotest("John:Gates;Michael:Wahl;Megan:Bell;Paul:Dorries;James:Dorny;Lewis:Steve;Alex:Meta;Elizabeth:Russel;Anna:Korn;Ann:Kern;Amber:Cornwell", 
          "(BELL, MEGAN)(CORNWELL, AMBER)(DORNY, JAMES)(DORRIES, PAUL)(GATES, JOHN)(KERN, ANN)(KORN, ANNA)(META, ALEX)(RUSSEL, ELIZABETH)(STEVE, LEWIS)(WAHL, MICHAEL)");
      
  }
}