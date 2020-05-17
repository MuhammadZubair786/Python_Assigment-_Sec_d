A=[1,5,6,213,8,35,67,98,65,55,100]
Large=A[0]
for i in range(0,len(A)):
    if(Large<A[i]):
        Large=A[i]
print("The Largest Number In The List ",Large)
