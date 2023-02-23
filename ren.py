from janome.tokenizer import Tokenizer
#形態素解析に必要なライブラリ
 

print('形態素解析を始めます')    

string = input("文字を入力してください")
#入力した文字を「string」に格納

t = Tokenizer()
#Tokenzierのインスタンスを変数「t」とする
tokens = t.tokenize(string)
#形態素形跡実行・メソッドに対象の文字列を渡す？
 
for token in tokens:#単語の取り出し
    print(token)
