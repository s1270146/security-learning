# アイドルスキャン

![ネットーワーク](https://media.istockphoto.com/id/1451699455/ja/%E3%83%99%E3%82%AF%E3%82%BF%E3%83%BC/%E6%8E%A5%E7%B6%9A%E4%BA%BA%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF.jpg?s=612x612&w=0&k=20&c=qm7aCXU_YNff_YJ2NAhAQaitlkypglqs219qat2HDLY=)

ネットワークセキュリティの学習

アイドルスキャンについて、学習したものをまとめました。

## アイドルスキャンとは

代理のスキャン用ホストを利用して、ターゲットホストのポートの開放状況を判断する。

代理のホストを使用するので、スキャン元のIPアドレスが攻撃先に記録されない。

## 方法

1. 攻撃元ホスト、ターゲットホスト、ゾンビホストが存在する
1. 攻撃元ホストからゾンビホストのIPアドレスでSYNパケットをターゲットホストに送信
1. ターゲットホストから、ターゲットホストのポートが開いていればSYN/ACK、閉じていればRST/ACKをゾンビホストに送信
1. ゾンビホストがターゲットホストからSYN/ACKパケットを受けとった場合はACKをターゲットホストに送信、RST/ACKを受け取った場合は何も送信しない 
1. 攻撃元のホストは↑を観察することでターゲットホストのポートが開いているかを確認することができる

![アイドルスキャン、オープンの場合](https://nmap.org/book/images/idle-scan-open.png)

## Javaコード

2023/7/17 コードがあっている気がしないのでもう一度確認する必要がある。一応Gitのリンクだけ。修正箇所が大あり

https://github.com/s1270146/security-learning/blob/main/network/idlescan/IdleScan.java

## 参考資料

- http://www.wata-lab.meijo-u.ac.jp/file/seminar/2004/2004-SEMI1-Kunihiko_Mizuno.pdf
- https://nmap.org/book/idlescan.html