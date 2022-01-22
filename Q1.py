# def function(name,num):
#     i=0
#     while i<len(name):
#         if i%2!=num:
#             b="RCN"
#         if i%2==num:
#             b="TAX"
#         i+=1
#     print(b)
# function("TRACXN",1)
# function("TRACXN",0)

# def number(i,num):
#     while i<=num:
#         if i%3==0 and i%5==0:
#             print(i,"FIZZBIZZ")
#         elif i%3==0:
#             print(i,"FIZZ")
#         elif i%5==0:
#             print(i,"BIZZ")
#         else:
#             print(i)
#         i+=1
# number(1,100)

def maxProfit(price, n):
    profit = [0]*n
    max_price = price[n-1]
    for i in range(n-2, 0, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit[i] = max(profit[i+1], max_price - price[i])
    min_price = price[0]
    for i in range(1, n):
        if price[i] < min_price:
            min_price = price[i]
        profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
    result = profit[n-1]
    return result
print(maxProfit([100,180,260,310,40,535,695],6))