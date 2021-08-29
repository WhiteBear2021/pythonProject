import heapq
# stock 현재 재고, dates 공급하는 각각의 날짜 오름차순 정렬되어있음, supplies 4일 20톤 10일 5톤 15일 10톤, k날 이후 다시 가동된다
ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    answer = 0
    current_day_index = 0
    max_heap=[]

    # date를 기준으로 반복할 것이다
    while stock < k:
        for date_index in range(current_day_index,len(dates)):
            print(date_index,dates[date_index],stock,supplies[date_index])
            if dates[date_index]<=stock:
                heapq.heappush(max_heap,-supplies[date_index])
            else:
                current_day_index=date_index
                break
        answer+=1
        stock+=-heapq.heappop(max_heap)
        print("stock is",stock)
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))