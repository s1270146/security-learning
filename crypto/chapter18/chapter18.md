# RSA暗号

# RSA暗号に対する基本的な攻撃

## 同報通信

同じ情報をRSAで暗号化して複数に送るときは注意が必要

$k$個の公開鍵$(N_i, e)$を用いて、あるメッセージ$m$を用いて暗号文$c_1,c_2,\cdots,c_k$を計算すると

$$
\begin{array}{l}
c_1 \equiv m^e \pmod {N_1} \\
c_2 \equiv m^e \pmod {N_2} \\
\vdots \\
c_k \equiv m^e \pmod {N_k} 
\end{array}
$$

