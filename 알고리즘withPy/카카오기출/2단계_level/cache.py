from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache=deque([])
    for city in cities:
        city=city.lower()
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.append(city)
        else:
            answer+=5
            if cacheSize==0:
                continue
            else:
                if len(cache)==cacheSize:
                    cache.popleft()
                    cache.append(city)
                else:
                    cache.append(city)
            print(cache)
    return answer

print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(0,["Jeju", "Pangyo", "NewYork", "newyork"]))