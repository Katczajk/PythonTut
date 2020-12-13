import base64
import hashlib

klarschrift = "Mein Text in Klarschrift"
text_in = bytes(klarschrift,encoding='UTF8')
output = hashlib.md5(text_in)
output_base64 = base64.b64encode(text_in)
print('Original Text in Klarschrift         ',klarschrift)
print('Bytes in Hex Format mit upper String ',str.upper(text_in.hex()))
print('Hash MD5 in Hex Uppercase            ',str.upper(output.hexdigest()))
print('Input to Base64 from bytes to string ',str(bytes.decode(output_base64)))

ages = {
    'Test1' : 30
}

age = ages.get('Test','Unknown')
print(age)