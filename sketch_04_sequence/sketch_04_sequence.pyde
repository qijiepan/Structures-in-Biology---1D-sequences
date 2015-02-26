sequence1 = []
sequence2 = []
matchscore = 2
gapscore = -2
mismatchscore = -1
# read the data from the file, and preprocessing
with open("/Users/kevin/desktop/CS582/04-Sequence/data.txt") as f:
    line = f.readlines()
for i in range(len(line)):    
    line[i] = line[i].strip('\n')
for i in range(1,6):
    for char in line[i]:
        sequence1.append(char)
for i in range(7,12):
    for char in line[i]:
        sequence2.append(char)

print len(sequence1)+1,len(sequence2)+1
#set the matrix
multilist = [[0 for col in range(len(sequence1)+1)] for row in range(len(sequence2)+1)]

#initialization
for i in range(len(sequence1)+1):
  multilist[0][i] = 0
for i in range(len(sequence2)):
  multilist[i+1][0] = 0

#print multilist
# fill the matrix

for i in range(len(sequence1)):
  for j in range(len(sequence2)):
    if(sequence1[i]==sequence2[j]):# match +2, gap -2
      multilist[j+1][i+1]= max(multilist[j][i]+matchscore,multilist[j+1][i]+gapscore,multilist[j][i+1]+gapscore)
    if(sequence1[i]!=sequence2[j]):# mismatch -1, gap -2
      multilist[j+1][i+1]= max(multilist[j][i]+mismatchscore,multilist[j+1][i]+gapscore,multilist[j][i+1]+gapscore)

# to get the max value and the position.            
position = [0,0]
maxvalue = -1
for i in range(len(sequence1)+1):
    for j in range(len(sequence2)+1):
        if multilist[j][i]>maxvalue:
            maxvalue = multilist[j][i]
            position[0]= i-1
            position[1]= j-1

print maxvalue,position


#draw the sequnce 
def draw_sequence():
  i=0
  j=0
  
  textSize(16)
  stroke(255) 
  fill(0)
  # read from ending to the begining 
  while (position[0]>=0 and position[1]>=0): 
    if(multilist[position[1]+1][position[0]+1]==matchscore+multilist[position[1]][position[0]]):
        fill(255,0,0)
        text(sequence1[position[0]],700-20*i,500-40*j)
        text(sequence2[position[1]],700-20*i,520-40*j)
        position[1] -= 1
        position[0] -= 1
    elif(multilist[position[1]+1][position[0]+1]==multilist[position[1]+1][position[0]]+gapscore):
        fill(0) 
        text(sequence1[position[0]],700-20*i,500-40*j)
        text("_",700-20*i,520-40*j)
        position[0] -= 1
    elif(multilist[position[1]+1][position[0]+1]==multilist[position[1]][position[0]+1]+gapscore):
        fill(0) 
        text("_",700-20*i,500-40*j)
        text(sequence2[position[1]],700-20*i,520-40*j)
        position[1] -= 1
    elif(multilist[position[1]+1][position[0]+1]==multilist[position[1]][position[0]]+mismatchscore):
        fill(0) 
        text(sequence1[position[0]],700-20*i,500-40*j)
        text(sequence2[position[1]],700-20*i,520-40*j)
        position[1] -= 1
        position[0] -= 1
    i +=1
    if(i>30):
      fill(0,0,255)
      text("sequence1",23*i,500-40*j)
      text("sequence2",23*i,520-40*j)
      j += 1
      i = 0
    if(position[0]==0 or position[1]==0):
        fill(0,0,255)
        text("sequence1",23*31,500-40*j)
        text("sequence2",23*31,520-40*j)


     
  

    
def setup():
    size(800,600)
    background(255)
    textSize(16)
    stroke(255) 
    fill(0)
   


def draw():
    draw_sequence()
