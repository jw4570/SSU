money = int(input())
price = int(input())

change = money - price
c1000 = change//1000
change %= 1000

c500 = change//500
change %= 500

c100 = change//100
change %= 100

c50 = change//50
change %= 50

c10 = change//10
change %= 10

print(money-price, c1000, c500, c100, c50, c10, sep ="\n")