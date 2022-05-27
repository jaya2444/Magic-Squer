# Magic Square is that kind of square in which sum of each row, sum of each column and sum of both the diagonals is equal. 


magic_square = [
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]
]
i=0
sum=0
sum1=0
sum2=0
while i<len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if i==0:
            sum=sum+magic_square[i][j]
        elif i==1:
            sum1=sum1+magic_square[i][j]
        else:
            sum2=sum2+magic_square[i][j]
        row=sum,sum1,sum2
        j=j+1
    i=i+1
print("row",sum)
print("row1",sum1)
print("row2",sum2)
print(row)
i=0
Sum=0
Sum1=0
Sum2=0
while i<len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if j==0:
            Sum=Sum+magic_square[j][i]
        elif j==1:
            Sum1=Sum1+magic_square[j][i]
        else:
            Sum2=Sum2+magic_square[j][i]
        col=Sum,Sum1,Sum2
        j=j+1
    i=i+1
print("col",Sum)
print("col2",Sum1)
print("col3",Sum2)
print(col)
i=0
dright=0
dleft=0
while i<len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if i==j:
            dright+=magic_square[i][j]
        if i+j==len(magic_square[i])-1:
            dleft+=magic_square[i][j]
        d=dright,dleft
        j+=1
    i+=1
print(dright)
print(dleft)
if col==row and dright==dleft and sum==sum1==sum2:
    print("it is magic square")
else:
    print("it is not magic square")

