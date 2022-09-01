from ntpath import join
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def DNA_strand(dna) :
  return dna.translate(dna.maketrans('ATGC' , 'TACG'))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():     
        test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
        test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
        test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")