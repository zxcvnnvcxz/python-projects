def maxProfit(prices):
    maxProf = 0
    mini = prices[0]

    for i in range(1, len(prices)):
        cost = prices[i] - mini
        maxProf = max(maxProf, cost)
        mini = min(mini, prices[i])

    return maxProf

if __name__ == "__main__":
    List = [7,1,5,3,6,4]
    List1 = [7, 6, 4, 3, 1]
    List2 = [1,2]
    List3 = [2,4,1]
    List4 = [2,1,2,0,1]
    print(maxProfit(List))
    print(maxProfit(List4))