name=str(input("enter your name: "))
print("welcome",name)
print("\n")
print("\n")

print("choose one of the following: ")

#choosing the questions for the topics
print("(press 1 for), (addition questions)")
print("(press 2 for), (subtraction questions)")
print("(press 3 for), (multiplication questions)")
print("(press 4 for), (division questions)")
print("\n")
# taking user input/selection
user_input=int(input("enter your choice: "))
print("\n")

print("============================================================")
#====================[addition question]==========================
if user_input==1:
  print(name,"here are the addition questions")
  print("1: 245 + 378 =")
  print("(a-)613","                    ","(b-)623")
  print("(c-)633","                    ","(d-)643")
  #answer is b
  n1=(input("enter your answer: "))
  if n1=="b":
    print("correct answer")
  elif n1=="a":
    print("wrong answer")
  elif n1=="c":
    print("wrong answer")
  elif n1=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
 #-------------------------------------------------
  print("2: 567 + 289 =")
  print("(a-)856","                    ","(b-)765")
  print("(c-)876","                    ","(d-)678")
  #answer is a
  n2=str(input("enter your answer: "))
  if n2=="a":
    print("correct answer")
  elif n2=="b":
    print("wrong answer")
  elif n2=="c":
    print("wrong answer")
  elif n2=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#---------------------------------------------------
  print("3: 1,245 + 678 = ")
  print("(a-)5,432","                    ","(b-)3,455")
  print("(c-)1,923","                    ","(d-)1,234")
  #answer is c
  n3=str(input("enter your answer: "))
  if n3=="c":
    print("correct answer")
  elif n3=="b":
    print("wrong answer")
  elif n3=="a":
    print("wrong answer")
  elif n3=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#-----------------------------------------------------
  print("4: 3,456 + 2,789 =")
  print("(a-)6,546","                    ","(b-)6,543")
  print("(c-)6,665","                    ","(d-)6,245")
  #answer is d
  n4=str(input("enter your answer: "))
  if n4=="d":
    print("correct answer")
  elif n4=="b":
    print("wrong answer")
  elif n4=="c":
    print("wrong answer")
  elif n4=="a":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#--------------------------------------------------------
  print("5: 7,825 + 3,476 =")
  print("(a-)11,301","                    ","(b-)23,112")
  print("(c-)12,111","                    ","(d-)11,300")
  #answer is a
  n5=str(input("enter your answer: "))
  if n5=="a":
    print("correct answer")
  elif n5=="b":
    print("wrong answer")
  elif n5=="c":
    print("wrong answer")
  elif n5=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")

#now calculating the score:
  score=0
  if n1=="b":
    score=score+1
  else:
      score=score+0
  if n2=="a":
    score=score+1
  else:
    score=score+0
  if n3=="c":
    score=score+1
  else:
    score=score+0
  if n4=="d":
    score=score+1
  else:
    score=score+0
  if n5=="a":
    score=score+1
  else:
    score=score+0
  print("\n")
  print(name,"your score is",score,"/5")

#====================[subtract question]==========================

elif user_input==2:
  print(name,"here are the subtraction questions")
  print("1: 735 − 248 =")
  print("(a-)487","                    ","(b-)477")
  print("(c-)467","                    ","(d-)777")
  #answer is a
  s1=(input("enter your answer: "))
  if s1=="a":
    print("correct answer")
  elif s1=="b":
    print("wrong answer")
  elif s1=="c":
    print("wrong answer")
  elif s1=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
 #----------------------------------------
  print("2: 1,000 − 456 =")
  print("(a-)544","                    ","(b-)540")
  print("(c-)520","                    ","(d-)500")
  #answer is a
  s2=str(input("enter your answer: "))
  if s2=="a":
    print("correct answer")
  elif s2=="b":
    print("wrong answer")
  elif s2=="c":
    print("wrong answer")
  elif s2=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")

#---------------------------------------------------
  print("3: 2,345 − 1,278 =")
  print("(a-)1,060","                    ","(b-)1,061")
  print("(c-)1,067","                    ","(d-)2,067")
  #answer is c
  s3=str(input("enter your answer: "))
  if s3=="c":
    print("correct answer")
  elif s3=="b":
    print("wrong answer")
  elif s3=="a":
    print("wrong answer")
  elif s3=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#-----------------------------------------------------
  print("4: 5,678 − 2,934 =")
  print("(a-)1,744","                    ","(b-)2,222")
  print("(c-)2,741","                    ","(d-)2,744")
  #answer is d
  s4=str(input("enter your answer: "))
  if s4=="d":
    print("correct answer")
  elif s4=="b":
    print("wrong answer")
  elif s4=="a":
    print("wrong answer")
  elif s4=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#--------------------------------------------------------
  print("5: 8,500 − 3,675 =")
  print("(a-)4,826","                    ","(b-)4,827")
  print("(c-)4,825","                    ","(d-)3,825")
  #answer is c
  s5=str(input("enter your answer: "))
  if s5=="c":
    print("correct answer")
  elif s5=="b":
    print("wrong answer")
  elif s5=="a":
    print("wrong answer")
  elif s5=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")

#now calculating the score:
  score=0
  if s1=="a":
    score=score+1
  else:
    score=score+0
  if s2=="a":
    score=score+1
  else:
    score=score+0
  if s3=="c":
    score=score+1
  else:
    score=score+0
  if s4=="d":
    score=score+1
  else:
    score=score+0
  if s5=="c":
    score=score+1
  else:
    score=score+0
  print(name,"your score is",score,"/5")

#==================[multiply question]==================
elif user_input==3:
  print("here are the multiplication questions")
  print("1: 24 × 15 =")
  print("(a-)360","                    ","(b-)366")
  print("(c-)361","                    ","(d-)362")
  #answer is a
  m1=(input("enter your answer: "))
  if m1=="a":
    print("correct answer")
  elif m1=="b":
    print("wrong answer")
  elif m1=="c":
    print("wrong answer")
  elif m1=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
 #----------------------------------------
  print("2: 36 × 12 =")
  print("(a-)430","                    ","(b-)431")
  print("(c-)437","                    ","(d-)432")
  #answer is d
  m2=str(input("enter your answer: "))
  if m2=="d":
    print("correct answer")
  elif m2=="b":
    print("wrong answer")
  elif m2=="c":
    print("wrong answer")
  elif m2=="a":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")

#---------------------------------------------------
  print("3: 45 × 18 =")
  print("(a-)810","                    ","(b-)816")
  print("(c-)811","                    ","(d-)819")
  #answer is a
  m3=str(input("enter your answer: "))
  if m3=="a":
    print("correct answer")
  elif m3=="b":
    print("wrong answer")
  elif m3=="c":
    print("wrong answer")
  elif m3=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#-----------------------------------------------------
  print("4: 125 × 24 =")
  print("(a-)3,001","                    ","(b-)3,000")
  print("(c-)3,102","                    ","(d-)3,007")
  #answer is b
  m4=str(input("enter your answer: "))
  if m4=="b":
    print("correct answer")
  elif m4=="a":
    print("wrong answer")
  elif m4=="c":
    print("wrong answer")
  elif m4=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#--------------------------------------------------------
  print("5: 216 × 15 =")
  print("(a-)3,241","                    ","(b-)3,247")
  print("(c-)3,240","                    ","(d-)3,245")
  #answer is c
  m5=str(input("enter your answer: "))
  if m5=="c":
    print("correct answer")
  elif m5=="b":
    print("wrong answer")
  elif m5=="a":
    print("wrong answer")
  elif m5=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")

#now calculating the score:
  score=0
  if m1=="a":
    score=score+1
  else:
    score=score+0
  if m2=="d":
    score=score+1
  else:
    score=score+0
  if m3=="a":
    score=score+1
  else:
    score=score+0
  if m4=="b":
    score=score+1
  else:
    score=score+0
  if m5=="c":
    score=score+1
  else:
    score=score+0
  print(name,"your score is",score,"/5")

#===================[division questions]=====================

elif user_input==4:
  print("here are the division questions")
  print("1: 144 ÷ 12 =")
  print("(a-)12","                    ","(b-)15")
  print("(c-)16","                    ","(d-)11")
  #answer is a
  d1=(input("enter your answer: "))
  if d1=="a":
    print("correct answer")
  elif d1=="b":
    print("wrong answer")
  elif d1=="c":
    print("wrong answer")
  elif d1=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
 #----------------------------------------
  print("2: 225 ÷ 15 =")
  print("(a-)16","                    ","(b-)17")
  print("(c-)15","                    ","(d-)20")
  #answer is c
  d2=str(input("enter your answer: "))
  if d2=="c":
    print("correct answer")
  elif d2=="b":
    print("wrong answer")
  elif d2=="a":
    print("wrong answer")
  elif d2=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")

#---------------------------------------------------
  print("3: 480 ÷ 16 =")
  print("(a-)30","                    ","(b-)40")
  print("(c-)70","                    ","(d-)50")
  #answer is a
  d3=str(input("enter your answer: "))
  if d3=="a":
    print("correct answer")
  elif d3=="b":
    print("wrong answer")
  elif d3=="c":
    print("wrong answer")
  elif d3=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#-----------------------------------------------------
  print("4: 756 ÷ 21")
  print("(a-)35","                    ","(b-)36")
  print("(c-)37","                    ","(d-)33")
  #answer is b
  d4=str(input("enter your answer: "))
  if d4=="b":
    print("correct answer")
  elif d4=="a":
    print("wrong answer")
  elif d4=="c":
    print("wrong answer")
  elif d4=="d":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")
#--------------------------------------------------------
  print("5: 1,440 ÷ 24 =")
  print("(a-)61","                    ","(b-)77")
  print("(c-)66","                    ","(d-)60")
  #answer is d
  d5=str(input("enter your answer: "))
  if d5=="d":
    print("correct answer")
  elif d5=="b":
    print("wrong answer")
  elif d5=="c":
    print("wrong answer")
  elif d5=="a":
    print("wrong answer")
  else:
    print("invalid answer")
  print("\n")

#now calculating the score:
  score=0
  if d1=="a":
    score=score+1
  else:
    score=score+0
  if d2=="c":
    score=score+1
  else:
    score=score+0
  if d3=="a":
    score=score+1
  else:
    score=score+0
  if d4=="b":
    score=score+1
  else:
    score=score+0
  if d5=="d":
    score=score+1
  else:
    score=score+0
  print(name,"your score is",score,"/5")

#============the end of code=================
print("\n")
print("=================the end=================")
