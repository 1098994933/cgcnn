from itertools import combinations, permutations


def if_cross(a1, b1, a2, b2):
    """[a1,b1,a2,b2]时间是否存在相交"""
    if(max(a1, a2) < min(b1, b2)):
        return True
    else:
        return False


def is_time_cross(startTimes,endTimes):
    """判断是否存在交集"""
    dict_a = {(startTimes[i], endTimes[i]) for i in range(len(startTimes))}
    time_list = []
    for i in dict_a:
        time_list = time_list + list(range(i[0], i[1]))
    if len(set(time_list)) == len(time_list):
        return True
    else:
        return False

if __name__ == '__main__':
    N = 7
    max_profit = 0
    startTime = [1,5,4,1,1,1,6]
    endTime = [2,6,6,5,8,9,9]
    profit = [10,15,20,15,50,60,40]
    #
    # N = input()
    # startTime = input().split()
    # endTime = input().split()
    # profit = input().split()
    max_profit = 0

    for j in range(1, N+1):
        for c in list(combinations([i for i in range(N)], j)):
            print("策略", c)
            # 遍历单次策略
            total_profits = 0
            startTimes = [startTime[i] for i in c]
            endTimes = [endTime[i] for i in c]
            profits = [profit[i] for i in c]
            # 如果时间存在交集 则为无效策略
            if is_time_cross(startTimes,endTimes)== False:
                total_profits = 0
                print("无效")
            else:
                total_profits = 0
                for i in c:
                    total_profits = total_profits + profit[i]
            if total_profits > max_profit:
                max_profit = total_profits
    print(max_profit)