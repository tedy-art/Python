X = 1
Y = 1
Z = 1
N = 2

ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print(ans)

# if __name__ == '__main__':
#     x = 1
#     y = 1
#     z = 1
#     n = 2
#     output=[]
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 if i+j+k==n:
#                     continue
#                 else:
#                     output.append([i,j,k])
    
#     print(output)
                      