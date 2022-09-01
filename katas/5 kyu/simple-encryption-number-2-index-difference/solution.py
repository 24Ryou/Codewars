import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def encrypt(text):
  region = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') + list('''.,:;-?! '()$%&"''')
  if text != None and text != "":
    if any(x in region for x in text):
      _text = text[0::2]
      text_ = [x.swapcase() if x in region[0:52] else x for x in text[1::2]]
      text = [_text[i//2] if i%2 == 0 else text_[i//2] for i in range(len(text))]
      text = "".join(list(region[-region.index(text[0])-1]) + [region[region.index(text[i-1]) - region.index(text[i])] for i in range(1 , len(text))])
    else : raise Exception("Error")
  return text

def decrypt(encrypted_text):
  region = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') + list('''.,:;-?! '()$%&"''')
  if encrypted_text != None and encrypted_text != "" :
    if any(x in region for x in encrypted_text): 
      x = list(region[76-region.index(encrypted_text[0])])
      for i in range(1 , len(encrypted_text)):
        x.insert(i , encrypted_text[i])
        x.append(region[region.index(x[i-1]) - region.index(x[i])])
        del x[i]
      encrypted_text = "".join([x[i].swapcase() if i%2 != 0 else x[i] for i in range(len(x))])
    else : raise Exception("Error")
  return encrypted_text
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(encrypt("Business"), "&61kujla")
test.assert_equals(encrypt("Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!"), "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w")
test.assert_equals(encrypt("This is a test!"), "5MyQa9p0riYplZc")
test.assert_equals(encrypt("This kata is very interesting!"), "5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p")

test.describe('Basic Decrypt Tests')
test.assert_equals(decrypt("$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"), "Do the kata \"Kobayashi-Maru-Test!\" Endless fun and excitement when finding a solution!")
test.assert_equals(decrypt("5MyQa9p0riYplZc"), "This is a test!")
test.assert_equals(decrypt("5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p"), "This kata is very interesting!")

test.describe('None or Empty')
test.assert_equals(encrypt(""), "")
test.assert_equals(decrypt(""), "")
test.assert_equals(encrypt(None), None)
test.assert_equals(decrypt(None), None)

test.describe('Not Allowed Chars')
test.expect_error("Not allowed chars should lead to an Error", lambda: encrypt("A5#"))
test.expect_error("Not allowed chars should lead to an Error", lambda: decrypt("A5#"))