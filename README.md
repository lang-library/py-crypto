# py-jccrypto

## To install

pip install jccrypto

## Short Description (Japanese)

```
Q. 128bit AES暗号化されたファイルを解読するのにはどのくらいの時間がかかりますか？

A. 時間をかけたところで解読できませんよ。
   AES暗号は共通鍵暗号ですので、複合化したときの平文が解らないと、総当たりしたところで「どのキーで複合すると正しく複合できているのか」が判断できません。
   せめて、英文テキストとかいう条件がわかっていればある程度は可能ですけど、総当たりですからファイルサイズと計算速度次第ってことになります。
   これが公開鍵暗号なら、暗号化キーから数学的に（膨大なCPU時間をかければ）複合化キーを計算することができますけどね。
```

```
AES-128bit は key(16byte=128bit), iv(16byte=128bit) で 指定される key, iv の組み合わせは 256bit のアドレス空間があります。

【2 の 256 乗を計算してみた】 http://darutk-oboegaki.blogspot.com/2014/04/2-256.html
2^256 を十進数で表すと 78 桁で、無量大数の十億倍くらいの値であることが分かりました。 ちゃんとした方法でランダムに生成した 256 ビットのハッシュ値が偶然ぶつかるかもしれないなんてことを心配するのは馬鹿げていることを理解しました。いや、馬鹿げているのは理解していたのですけど、実際に計算してみると、どれだけ途方もなく馬鹿げているのかが分かった、という話です。

どれくらい大きな数字なのか例えで考えてみます。

    太陽の寿命が来るまで今から 50 億年のあいだ、
    100 億人の人が、
    毎ナノ秒 1 兆個の数値を消費していく活動があり、
    その活動を、太陽系が属するこの銀河系の全ての星（～2,000 億くらい）でおこなうと、

消費される数字の個数は、50 億年 × 100 億人 × 100000000 ナノ秒 × 60 秒 × 60 分 × 24 時間 × 365 日 × 1 兆個 × 2000 億個(星) で 59 桁の数字になります。こんなに頑張って消費しても、50 億年後 (太陽が赤色巨星になって太陽系が崩壊する頃) に消費し終わっているのは、(59 桁) / (78 桁) = 10^-19、つまり全体の 100 京分の 1 です。
```

```
----

# 鍵の生成
key = 'abcdefghijklmnop'.encode()
# IVの生成
iv = '1234567890123456'.encode()
# 鍵とIVで暗号化クラスオオブジェクト生成
cr = JcCrypto(key, iv)

↑こんな適当な鍵とIVでは推測されてしまう可能性もありますが・・・

----

# 任意の文字列から暗号化クラスオブジェクトを作る方法
cr2 = JcCryptoFromString("Python")

①「Python」のSHA256(32bytes=256bit)を求める ⇒ 18885f27b5af9012df19e496460f9294d5ab76128824c6f993787004f6d9a7db
②上下16bytes(16進数32桁)ずつに分割
   upper = 18885f27b5af9012df19e496460f9294
   lower = d5ab76128824c6f993787004f6d9a7db
③ upper を鍵, lower をIVとして暗号化クラスオブジェクトを作成
   return JcCrypto(upper, lower)

----

↑の「任意の文字列から暗号化クラスオブジェクトを作る方法」を使うととても強力です。(ただし「Python」を推測されたらアウト)

そこで、パスワード生成 https://www.graviness.com/app/pwg/ で以下のようなランダムなパスワードを生成して
5{$HtT<M)}<$&*_yEp[]-3>n*5e&)G<J

cr2 = JcCryptoFromString("5{$HtT<M)}<$&*_yEp[]-3>n*5e&)G<J")
としてしまえば、SHA256は、463cf456a504a0a1fb331981d799f5fb4e58af867977e246d7cbf54a97546d34 となり
十進数では、31769596586757812275155959797078663488097707046160970084875920216559577230644 (10進77桁) となります。
このような鍵、IVを総当たりで求めることは「もはや不可能」です。

----
```

## Sample code

```
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
```
