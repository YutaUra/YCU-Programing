# ブログを作れるモジュールの開発

作成日：20191118\
更新日：20191118

# 目的
[ワードプレス](https://ja.wordpress.com/)というサービス？ソフトウェア？がある。
これは簡単にサイトやブログを作れるようにするためのものであり、PHPという言語で書かれている。
一切プログラムを書かなくてもいい感じのサイトが作れる。

Pythonでもwebサイトを作れるライブラリーは存在するが、ワードプレス程簡単ではない。
簡単なブログなら一切コードを書かなくていいようなテンプレートモジュールがあってもいいのではないかと思い、開発しようと思った。

# 具体的に
イメージは上のワードプレスをPythonで再現する感じである。
基本的にGUI操作のみでブログの作成を行えるようにする。

# 使おうと思っているライブラリー
・Django
webサイトを開発するためのライブラリーで、個人で使用経験もあるので採用する。

# 目標！

コマンド1つ打てばサイトが構築される！

例： `pysite create` -> サイトが作られる！

## 要件
- [ ] コア設定をLive編集できる。
- [ ] ブログが書ける