for i in range(1, 11):
  for j in range(i,i*10+1,i):
    print( j , end=" ")
    print( )
    
#example
for i in range(1,3):
  j=1
  while j<3:
    print(i,j)
    j+=1
  print("gfg")
  
  #application of nested loop
  ll=[[10,20,30],[40,50,60],[70,80,90]]
  for i in ll:
    for j in i:
      print(j,end=" ")
    print()
      