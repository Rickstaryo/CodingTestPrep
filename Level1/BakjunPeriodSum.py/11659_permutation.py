N, K = map(int, input().split())
tem_list = list(map(int, input().split()))

part_sum = sum(tem_list[:K])
result_list = [part_sum]

for i in range(0, len(tem_list)-K):
    part_sum = part_sum - tem_list[i] + tem_list[i+K]
    result_list.append(part_sum)

print(max(result_list))
