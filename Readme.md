#Python3 勉強ノート
##モジュールの探し方
    標準ライブラリ
    https://docs.python.org/ja/3/
    標準ライブラリが使えると強い

##ディクショナリ
ディクショナリ名 ={キー名:要素}

##セット
集合を扱うのに便利
和集合 | 差集合 - 交わり & 対象差 ^
重複しないリストみたいなの
※要素は数値や文字列のみ！！
変更できるとsetの性質を保てないから

##タプル
要素が変更できないリスト　そのまんま
ディクショナリのキーやsetの要素につかえる

##比較演算子
数値の大小を比較したいとき文字列のままだと失敗することあり
比較は同じ型でやる
###論理演算子
and or　有

##While文
for文だと書きづらいものをcontinue文,break文を用いて楽にかける
continue文:ループの先頭へ
break文：ループを抜ける

##ループ文でのelse
ループをbreakなしで終了したときに実行される

##defalut引数
デフォルト値を持つ関数は後ろにまとめる
引数をキーワード指定すると順番関係なしに設定できる。デフォルト引数がいくつかあるときに便利

##メソッド
mcz.index()
の.indexのようなもの

##オブジェクト指向
データと命令を一緒にしてしまおうっていう考え
データと命令（メソッド）が一緒になっているものをオブジェクトという

##~進数
~進数を数値型と文字型で変換できる

##ビット演算
and(&),or(|),xor(^)とかシフト演算子(>>,<<)とかつかえる
