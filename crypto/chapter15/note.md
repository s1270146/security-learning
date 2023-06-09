# 15章

## メモ
- hashlib, binasciiは標準ライブラリ
- Length Extension Attack が ハッシュに対する主な攻撃方法

## Length Extension Attack
- Merkle-Damgard構造を持つハッシュ関数に対して有効
  - メッセージを分割して分割したデータを順番にハッシュしていく
- この攻撃では、データを付け加える