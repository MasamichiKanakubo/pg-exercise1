#ans

"""
ハノイの塔の有名問題
漸化式を使った方法で解く
a_n+1とa_nの関係を考えてみる
a_1 = 1
a_2 = 3を初期条件で試してみる
a_3 = 7 ←今回問題になっているやつ. これくらいは手で数えられる
n+1個の円盤の移動について考えてみる
n個の円盤を移動するのにa_n回かかるとすると
左端にあるn+1個めの円盤を移動するのに1回かかる
そのあとn個の円盤を移動するのにa_n回かかる(n段の円盤をつくるのにa_n回かかったから)
ゆえにn+1個の円盤の移動にかかる時間はa_n+1 = 1 + a_n + a_n = 2a_n + 1
特性方程式を解いて等比型に帰着させてa_n = 2^n - 1が一般解
今回は再帰を使って解答を書いてみる
"""

def hanoi(n, stake1, stake2, stake3):
    if n == 1:
        print(f"1番を{stake1}から{stake3}へ移動")
        return
    hanoi(n - 1, stake1, stake3, stake2)
    print(f"{n}番を{stake1}から{stake3}へ移動")
    hanoi(n - 1, stake2, stake1, stake3)

n = 3
hanoi(n, 'A', 'B', 'C')

print('パズルが解けた！')
print('神殿の扉が開いた！')
print('勇者は宝箱を開けた！')
print('勇者は天空の剣を手に入れた！')