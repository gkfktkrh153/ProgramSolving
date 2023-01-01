def solution(cacheSize, cities):
    for i,city in enumerate(cities):
        cities[i] = city.upper()
    num = 1
    cache = ["" for i in range(cacheSize)]
    sequence = [0 for i in range(cacheSize)]   # 사용된 순서
    answer = 0
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            
            hit = 0
            hitIndex = -1
            for i in range(cacheSize): # 캐시 히트 확인
                if city == cache[i]:
                    hit = 1
                    hitIndex = i
                    break
            if hit == 1:
                sequence[hitIndex] = num
                num += 1
                answer += 1 
            else:
                minIndex = 0
                for i in range(cacheSize):
                    if sequence[minIndex] > sequence[i]:
                        minIndex = i # 가장 오래전에 사용된 인덱스
                #print(minIndex)
                sequence[minIndex] = num
                cache[minIndex] = city
                num += 1
                answer += 5
            #print(cache)
            #print(sequence,answer)
    return answer