# extract-the-domain-name-from-a-url-1
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
import re
def domain_name(url):
  return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")