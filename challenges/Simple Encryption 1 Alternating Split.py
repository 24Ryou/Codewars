import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def decrypt(encrypted_text, n):
  if encrypted_text != None:
    v = int(len(encrypted_text)/2)
    encrypted_text = list(encrypted_text)
    for x in range(n):
      odd  = list(encrypted_text[:v])
      even = list(encrypted_text[v:])
      encrypted_text[1::2] = odd
      encrypted_text[::2] = even
    return "".join(encrypted_text)
  else : return encrypted_text

def encrypt(text, n):
  for x in range(n):
    odd  = text[1::2]
    even = text[::2]
    text = odd+even
  return text
# ------------------------------ clever solution ----------------------------- #
def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text

def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
# ----------------------------------- test ----------------------------------- #
test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

test.assert_equals(encrypt("", 0), "")
test.assert_equals(decrypt("", 0), "")
test.assert_equals(encrypt(None, 0), None)
test.assert_equals(decrypt(None, 0), None)