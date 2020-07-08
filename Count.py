s = "cheRry"
count = 0
for i in s:
    if i == 'c':
        count1 = count + 1
    elif i == 'h':
        count2 = count + 1
    elif i == 'e':
        count3 = count + 1
    elif i == 'r':
        count4 = count + 1
    elif i == 'R':
        count5 = count + 1
    elif i == 'y':
        count6 = count + 1
print('c:'+str(count1),'h:'+str(count2),'e:'+str(count3),'r:'+str(count4+count5),'y:'+str(count6))