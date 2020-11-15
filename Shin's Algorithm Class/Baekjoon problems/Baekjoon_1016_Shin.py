# 백준 1016 제곱 ㄴㄴ 수
# Baekjoon 1016

# Created by sw0817 on 2020. 11. 16..
# Copyright © 2020 sw0817. All rights reserved.

# See : https://www.acmicpc.net/problem/1016

import math

min_num, max_num = map(int, input().split())

# 범위 내 숫자가 제곱 ㄴㄴ 수인지 확인한다. 우선은 모두 제곱 ㄴㄴ 수로 초기화.
results = [1] * (max_num - min_num + 1)

# max_num 의 약수로 가능한 모든 제곱수들의 집합
squares = []

for i in range(2, int(math.sqrt(max_num)+1)):
    squares.append(i ** 2)

# 모든 제곱수에 관해
for square in squares:

    # 범위 내 수에서 가장 작은 현재 제곱수의 배수를 찾고,
    # results 배열에서의 idx 는 다음과 같다.
    idx = (math.ceil(min_num / square) * square) - min_num

    # 배열을 벗어나지 않는 선에서
    while idx <= max_num - min_num:

        # 제곱수의 배수는 제곱 ㄴㄴ 수가 아니므로 배열에서 0으로 갱신하고
        results[idx] = 0

        # 제곱수만큼 더해서 제곱수의 다음 배수 값을 확인한다.
        idx += square

# 배열의 합이 제곱 ㄴㄴ 수의 갯수
print(sum(results))