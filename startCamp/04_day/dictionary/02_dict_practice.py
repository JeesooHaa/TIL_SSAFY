"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.

# for num in range(len(score.values())):
#     num = num + 1

# value_sum = 0
# for value in score.values():
#     value_sum += value
    
# print(value_sum/num) // 


# for subject_score in score.values():
#     total_score = total_score + subject_score 

total_score = sum(score.values())
average_score = total_score / len(score.values())
print(average_score)





# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 120
    }
}

# 아래에 코드를 작성해 주세요.

# for i in scores:
    
#     for num in range(len(scores[i].values())):
#         num = num + 1

#     value_sum = 0   
#     for value in scores[i].values():
#         value_sum += value
    
#     print(value_sum/num)

total_score = 0 
count = 0 

for person_score in scores.values():
    total_score += sum(person_score.values())
    count += len(person_score)

average_score = total_score / count 
print(average_score)




# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# for key in city:
#     print(key, sum(city[key])/len(city[key]))

for key, value in city.items():
    average_temp = sum(value) / len(value)
    print(f'{key} : {average_temp}')


# sum([1, 3, 4]) # 8
# len 3
# max 4
# min 1










# # 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# print(max(city))
# print(min(city))






# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')