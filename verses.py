vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
lines_num=int(input("How many lines? "))
lines=[]

for x in range(0,lines_num):
  inpTxt=''.join(['write line nr ',str(x+1),': '])
  newLine=input(inpTxt).lower()
  count_vowels=0
  count_consonants=0
  for z in newLine:
    if z in vowels:
      count_vowels+=1
    elif z in consonants:
      count_consonants+=1
  lines.append({"line":newLine,"vowels":count_vowels,"consonants":count_consonants})
print(''.join(['How many lines will there be? ',str(lines_num)]))
total_vowels=0
total_consonants=0
for l in lines:
  vowels=l["vowels"]
  consonants=l["consonants"]
  line=l["line"]
  total_vowels+=vowels
  total_consonants+=consonants
  print(''.join([str(line),'      vowels:',str(vowels),', consonants:',str(consonants)]))
print(''.join(['Total vowels: ',str(total_vowels)]))
print(''.join(['Total consonants: ',str(total_consonants)]))