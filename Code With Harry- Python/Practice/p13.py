matrix=[[1,2,3],[4,5,6],[7,8,9]]

# b=[]
#
# for i in matrix:
#     for j in i:
#         b.append(j)
# print(b)

b=[j for i in matrix for j in i]
print(b)