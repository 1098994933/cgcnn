from itertools import combinations, permutations


def if_cross(a1, b1, a2, b2):
    """[a1,b1,a2,b2]时间是否存在相交"""
    if(max(a1, a2) < min(b1, b2)):
        return True
    else:
        return False
def is_time_cross(startTimes,endTimes):
    """判断是否存在交集"""
    dict_a = {(startTimes[i],endTimes[i]) for i in range(startTimes)}
    time_list = []
    for i in dict_a:
        time_list = time_list + list(range(i[0],i[1]))
    if len(set(time_list)) == len(time_list):
        return False
    else:
        return True


if __name__ == '__main__':
    # N = 4
    # max_profit = 0
    # startTime = [1,5,4,1]
    # endTime = [2,6,6,5]
    # profit = [10,15,20,15]
    N = input()
    startTime = input().split()
    endTime = input().split()
    profit = input().split()
    c = (0,1)
    print("策略", c)
    # 遍历单次策略
    total_profits = 0
    startTimes = [startTime[i] for i in c]
    endTimes = [endTime[i] for i in c]
    profits = [profit[i] for i in c]
    chosen = []
    # 遍历组合 中的每个选择 判断是否能加入
    for k in range(len(c)):
        if (len(chosen) == 0):
            chosen.append((startTimes[k], endTimes[k]))
            total_profits = total_profits + profits[k]
        is_cross = False
        # 如果存在重合 直接返回0 否则返回加和
        for i in chosen:
            if(if_cross(startTimes[k], endTimes[k], i[0], i[1])) == True:
                is_cross = True
                total_profits = 0
            else:
                chosen.append((startTimes[k], endTimes[k]))
        # 返回结果
        if is_cross == False:
            total_profits = 0
            for i in c:
                total_profits = total_profits+profit[i]
    print("利润", total_profits)
    print("选择时间段", chosen)
    print("=============")
    if total_profits > max_profit:
        max_profit = total_profits