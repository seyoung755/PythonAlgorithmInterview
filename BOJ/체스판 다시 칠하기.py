# row, column = map(int, input().split())

# # print(row, column)

# board = []

# for i in range(row):
#     board.append(input())

# # print(board)
# # count = 0
# sub_board = []
# row1 = 'BWBWBWBW'
# row2 = 'WBWBWBWB'
# count = 0
# for c in range(column - 8 + 1):
#     for r in range(row - 8 + 1):
#         sub_board = board[c:][0]
#         temp = 0
#         print(sub_board)
#         if sub_board[0][0] == 'B':
#             for i,j in enumerate(sub_board):
#                 for n, char in enumerate(j):
#                     print(n,char)
#                     if i%2 == 0:
#                         if char != row1[n]:
#                             temp += 1
#                     else:
#                         if char != row2[n]:
#                             temp += 1
#                     count = max(temp, count)
        
#         else:
#             for i,j in enumerate(sub_board):
#                 for n, char in enumerate(j):
#                     print(n, char)
#                     if i%2 == 0:
#                         if char != row2[n]:
#                             temp += 1
#                     else:
#                         if char != row1[n]:
#                             temp += 1
#                     count = max(temp, count)
            

# print(row2[1])
            

        # count += 1
# print(count)
        


N = 8

str1 = 'WBWBWBWB'
str2 = 'BWBWBWBW'

pivot1 = [str1, str2]*4
pivot2 = [str2, str1]*4

def solve():
    row, column = map(int, input().split())
    arr = []

    for i in range(row):
        arr.append(input())
    rst = float('inf')
    for i in range(row-N+1):
        for j in range(column-N+1):
            count = 0
            for p in range(N):
                for q in range(N):
                    # if arr[i][j] == 'W':

                    if arr[i+p][j+q] != pivot1[p][q]:
                        count += 1
            rst = min(rst, count)
            count = 0
            for p in range(N):
                for q in range(N):
                    if arr[i+p][j+q] != pivot2[p][q]:
                        count += 1
            rst = min(count, rst)
    print(rst)                

solve()