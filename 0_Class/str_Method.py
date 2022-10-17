# 문자열 슬라이싱
# [:] : 처음부터 끝까지
# [start:] : start부터 끝까지
# [:end] : 처음부터 end-1까지
# [start:end] : start부터 end-1까지
# [start:end:step] : step만큼 건너뛰면서 start부터 end-1까지
# [::-1] : 역순

test = "abcd lalalala gotcha"
print(test)
print(test[:])
print(test[3:])
print(test[:10])
print(test[4:10])
print(test[::2])

# find(), index() : returning the indext result
# difference between two method is there will -1 one got error but the other one not
print(test.find("gotcha"))
print(test.index("abcd"))
print(test.find("lalala"))
# print(test.index("치"))

path = "c:\\test\\abcd\\abcde.jpg"
print(path)
print(path.rfind("\\"))

# Spliting the last fie
print(path[path.rfind("\\")+1:])
a = "   testsu   "
print(path.split())
print(a.strip())


a = "aaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbb"
print(a.count("aa"))
