from jccrypto import AES, AES128FromString, AES256FromString

text = "Pythonの暗号化ライブラリとそれらの概要を表にまとめました。非常にたくさんのライブラリがあることがわかりました。それぞれのライブラリが得手不得手を持っているためユースケースに応じて適切なライブラリを使用する必要があります。"

# 鍵の生成
#key = 'abcdefghijklmnop'.encode()
key = '12345678901234567890123456789012'.encode()
# IVの生成
iv = '1234567890123456'.encode()

cr = AES(key, iv)

print("")
encoded = cr.encode_text(text)
print("encoded={}".format(encoded))
decoded = cr.decode_text(encoded)
print("decoded={}".format(decoded))

print("")
text_bytes = text.encode()
print("text_bytes={}".format(text_bytes))

print("")
encoded = cr.encode_bytes(text_bytes)
print("encoded={}".format(encoded))
decoded = cr.decode_bytes(encoded)
print("decoded={}".format(decoded))

print("")
text2 = decoded.decode()
print("text2={}".format(text2))

print("")
list = [11, 22, 33]
encoded = cr.encode_pickle(list)
decoded = cr.decode_pickle(encoded)
print("decoded={}".format(decoded))

print("")
cr2 = AES128FromString("this is password!")
list = [111, 222, 333]
encoded = cr2.encode_pickle(list, protocol=4)
decoded = cr2.decode_pickle(encoded)
print("decoded={}".format(decoded))

print("")
cr3 = AES256FromString("this is password!")
list = [1111, 2222, 3333]
encoded = cr3.encode_pickle(list, protocol=4)
decoded = cr3.decode_pickle(encoded)
print("decoded={}".format(decoded))
