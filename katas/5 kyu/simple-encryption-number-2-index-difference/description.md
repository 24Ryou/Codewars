For encrypting strings this region of chars is given (in this order!):

* all letters (ascending, first all UpperCase, then all LowerCase)
* all digits (ascending)
* the following chars: `.,:;-?! '()$%&"` 

These are 77 chars! (This region is zero-based.)<br/>

Write two methods: <br/>
```csharp
string Encrypt(string text)
string Decrypt(string encryptedText)
```

def encrypt(text)
def decrypt(encrypted_text)
