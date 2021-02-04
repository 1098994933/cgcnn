from itertools import combinations, permutations
# def get_max_profit():
#     pass

a = [1, 2, 3, 4]
b = [2, 4, 6, 8]
c = list(combinations(a, 2))
if __name__ == '__main__':
    # N = input()
    # startTime = input().split()
    # endTime = input().split()
    # profit = input().split()

    N = 4
    print(list(combinations([i for i in range(N)], 2)))
    startTime = [1,5,4,1]
    endTime = [2,6,6,5]
    profit = [10,15,20,15]
    average = [profit[i]/(endTime[i]-startTime[i]) for i in range(len(startTime))]
    print(average)
    # chose all possiable
    print(startTime[(0,1)])

