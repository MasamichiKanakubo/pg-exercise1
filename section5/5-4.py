#ans

print('スライムがあらわれた！')
print('スライムはなかまになりたそうにじっとこっちを見ている。')


answer = input('[0]仲間にする\n[1]戦う\n[2]逃げる\n選択:')
if answer == 0:
    print('スライムはなかまになった！')
elif answer == 1:
    print('勇者はスライムを倒した！')
else:
    print('勇者は逃げた！')
    

"""
選択しがながったるいので改行\nを使う
わざわざ改行を行っているので選択しの横に入力部分を作るのは野暮
改行して選択用の行を作る
answerをstringでうけとるので例外処理は不要
"""