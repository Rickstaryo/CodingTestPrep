# Input
N = int(input())
book_rank = {}
for i in range(N):
    book = input()
    if book in book_rank:
        book_rank[book] += 1
    else:
        book_rank[book] = 1
# Count and sorting
result = sorted(book_rank.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
