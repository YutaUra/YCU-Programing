# コードレビュー用のディレクトリです。

## 目的
1. 自分のコードを他人に評価してもらうことで、よりいいロジック、コードにしていく。
1. 他人のコードを評価することで、客観的にみる思考を自分のコーディングにも生かす。

## コードエディターについて
コードエディター（jupyter notebookも含む）とはプログラムを書くための専用のソフトのことである。\
Python理解ではほとんどをJupyterで書いていたと思うが、規模の大きいプログラムを書いたりする場合は、普通のpythonファイルに書くことが普通である。
> Jupyterでは作った関数やクラスをほかのファイルで使うことができない（できるかもしれないが普通しない）ので、まとまりのあるものなどを作る際や、ファイルを分けたりする際には不適合である。

そこで、コードレビューでは各自好きなエディターを使ってもらいます。（これも練習だと思って！）\
いろいろなエディターがあるのでいくつか紹介します。[おススメ](#PyCharm)

### Visual Studio Code[ページ](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)
マイクロソフト社のコードエディター。通称:VSCode\
完全フリーなので世界的に人気度も高いように思える。
### Atom[ページ](https://atom.io/)
GitHub社のコードエディター\
こちらも完全フリーである。\
VSCodeよりかは人気度は下がるかな～という印象
### PyCharm[ページ](https://www.jetbrains.com/pycharm/)
Jetbrains社のコードエディター\
コミュニティ版は無料で、プロ版は有料（学生はプロ版も無料）。\
PyCharmとあるだけあってPython開発のためのエディターである。（他にもC, Java, PHP,...などそれぞれに特化したエディターを提供している)\
一番おススメする。


本当に何を使っても全然OKです。迷うならPyCharmにしよう。アドバイス等もできるので

# 指南
以下で実際にプログラムを作る際のポイント等を順次上げていきます。
## 1. 目的を明確にする
「何をしたいか」が明確でないプログラムは無駄が多くなり、必要以上に頭を使わなきゃいけなくなります。

「*本当の目的*・**なんでそれをしたいか**」と一致しているかをよく考える。

本当の目的：いつも寝坊をしてしまうのでそれを防ぎたい。\
悪い例：\
目的：スケジュール管理ができるプログラム\

いい例：\
目的：アラームを鳴らしてくれるプログラム\

## 2. 必要要素を考える
目的を決めたら「ハイ、スタート！」ではありません。

目的(,真の目的)のためには何が必要かを考えます。

ここの出来や、内容次第で出来上がるプログラムは変わります。

アラームを鳴らしてくれるプログラム\
悪い例：

    ・ アラームを鳴らす関数

いい例：

    ・アラームを鳴らす関数
        ・音楽を鳴らす関数
            ・音を鳴らす関数
        ・設定時刻に動く関数
    ・アラームを設定する関数

## 3. 中身はおいといてコードの全体の流れを作る
どういうことかというと、2. で決まったことを1つずつ作ればいいのだけれども、1つずつ作る前に、主要な要素の枠だけ先に作っちゃう。\
その時に[docstring](https://qiita.com/kanatatsu64/items/d3ef79be0ae0409c8681)も一緒に書くといい。
```python
# main.py
from alarm import Alarm

def set_alerm(d_time, remind=0):
  """アラームをセットする関数
  :param d_time: 設定する日時
  :param remind: リマインドするときの間隔（0でなし）
  :type d_time: datetime
  :type remind: int
  """
  alarm = Alarm(d_time, remind)
  alarm.set()
```
```python
# alerm.py

class Alerm:
  def __init__(self, d_time, remind):
    self.time = d_time
    self.remind = remind
  
  def set(self):
    pass
```
的な

# 人のコードをレビューしよう！

## 大事なこと
1. ダメ出しはしないように気を付けよう。僕たちはみんな初心者。ダメダメなんです。。。
1. 何をしたいのかを理解をしよう。何をするためのプログラムかわからずにはレビューのしようがありません。
1. 良いところを積極的に言いましょう。「ここのプログラムは参考になるな」とか、「ここに気を付けているのかな」とか
1. 改善できそうなところを言ってみましょう。「自分ならここはこうするかも」とか、「その変数はこっちの名前にしたほうがいいかもね」とか

**コードレビューの目的には「みんなで力を合わせてプログラムを作る」ということもあるので、作成者の気持ちになって発言をしよう！**
