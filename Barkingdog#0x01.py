
def func1(N):
    sum = 0
    for i in range(1,N+1):
        if i%3 == 0 or i%5==0:
            sum += i
    return sum


# print(func1(34567))


def func2(arr, N):
    
    for i, num in enumerate(arr):
        target = 100-num
        if target in arr and arr.index(target) != i:
            return 1
    return 0

a = [4, 13, 63, 87]

# print(func2(a, len(a)))
        

def func3(N):
    if N == 1:
        return 1

    
    
    lend, rend = 1, N
    while True:
        
        if rend-lend == 1:
            return 0
        start = (lend+rend)//2
        
        if start*start > N:
            rend = start
        elif start*start < N:
            lend = start
        
        elif start*start == N:
            return 1

print(func3(756580036))
        
        
# def func4(N):
    
#     for i in range(N,1,-1):
#         base = N
#         while (base//2)%2 == 0:
#             base = base//2
        

N, X = map(int, input().split())

arr = list(map(int, input().split()))

answer = []
for n in arr:
    if n < X:
        answer.append(n)

print(*answer)