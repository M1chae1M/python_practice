moves=[]

def inputData():
  while True:
    data=input(''.join(['Give the coordinates of the field:'])).split()
    if 0<int(data[0])<=8 and 0<int(data[1])<=8:
      return data
    else:
      print('You entered a number outside the range of 1-8!')
      
for x in range(0,2):
  moves.append(
    tuple(
      map(
        int,
        inputData()
      )
    )
  )
  
pair1=moves[0]
pair2=moves[1]
horizontalMove=abs(pair1[0]-pair2[0])
verticalMove=abs(pair1[1]-pair2[1])

if horizontalMove==verticalMove:
  print('YES')
elif horizontalMove==0:
  print('YES')
elif verticalMove==0:
  print('YES')
else:
  print('No')