# 数独を解くプログラムを作成する
作成日: 2019/10/25\
更新日: 2019/10/25

## 目的
数独を自動で解きたい

## 具体的に
入力 : 9 * 9の盤面に数字がいくつかの数字が埋まっている\
出力 : 全ての答えの組み合わせ

## オブジェクトの定義
Board : 9 * 9の盤面\
Block : 9個のCellの集まり(縦、横、3*3)\
Cell  : 1つのマス

## 方向
    ステートの最小単位
    Cell : {
        number : {
            default : None,
            mean : 確定した数字,
        },
        allowed : {
            default : set(1~9),
            mean : マスに入る可能性がある文字,
        },
    }
    Gropu : {
        cells : {
            default : set([x, y]),
            mean : Board内のCellのIndexの集合
        },
        filled : {
            default : set(),
            mean : 既に埋まっている数字たち
        }
    }
    Board : {
        cell_2d : {
            default : [[Cell]*9]*9,
            mean : 9×9のCellの集合
        },
        col : {
            default : [Group * 9],
            mean : 横の列のグループ,
        },
        row : {
            default : [Group * 9],
            mean : 縦の行のグループ,
        },
        block : {
            default : [Group * 9],
            mean : 3*3の正方形のグループ
        }
    }

