l =[]

while True:
    a = int(input("Inserire un numero (0 per terminare): "))
    if a == 0:
        break
    else:
        l.append(a)


for i in l:
    print("*"*i)
      
        
