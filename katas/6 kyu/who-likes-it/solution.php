<!-- who-likes-it -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function likes( $names ) {
  if (count($names) == 0) return 'no one likes this';
  if (count($names) == 1) return $names[0] . " likes this";
  if (count($names) == 2) return implode(" and " , $names) . " like this";
  if (count($names) == 3) return  $names[0] . ', ' . implode(" and " , array_slice($names , 1)) . " like this";
  if (count($names)  > 3) return  $names[0] . ', ' . $names[1] ." and ". strval(count($names) - 2) . " others like this";
}
/* ----------------------------- CLEVER SOLUTION ---------------------------- */
function likes(array $names): string {
  switch (count($names)) {
    case 0:
      return 'no one likes this';
    case 1:
      return vsprintf('%s likes this', $names);
    case 2:
      return vsprintf('%s and %s like this', $names);
    case 3:
      return vsprintf('%s, %s and %s like this', $names);
    default:
      return sprintf('%s, %s and %d others like this', $names[0], $names[1], count($names) - 2);
  }
}
/* ---------------------------------- TEST ---------------------------------- */
class ExampleTestCases extends TestCase {

  public function testReturnCorrectText() {

      $this->assertSame( 'no one likes this', likes( [] ) );
      $this->assertSame( 'Peter likes this', likes( [ 'Peter' ] ) );
      $this->assertSame( 'Jacob and Alex like this', likes( [ 'Jacob', 'Alex' ] ) );
      $this->assertSame( 'Max, John and Mark like this', likes( [ 'Max', 'John', 'Mark' ]) );
      $this->assertSame( 'Alex, Jacob and 2 others like this', likes( [ 'Alex', 'Jacob', 'Mark', 'Max' ] ) );
      $this->assertSame( '1, 2 and 2 others like this', likes( [ 1 , 2 , 3 , 4 ] ) );
  }
}