<!-- function-1-hello-world -->
<?php
use PHPUnit\Framework\TestCase;
/* ------------------------------- MY SOLUTION ------------------------------ */
function greet(){
  return 'hello world!';
}
/* ---------------------------------- TEST ---------------------------------- */
class MyTestCases extends TestCase
{
    public function testHelloWorld() {
      $this->assertEquals("hello world!", greet());
    }
}