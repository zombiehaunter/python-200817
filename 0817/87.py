mscore = int(input("enter math score:"))
escore = int(input("enter english score:"))
if mscore>=0 and mscore<=100 and escore>=0 and escore<=100:
    if mscore>=90 and escore>=90:
        print("有獎品 ")
    
    elif mscore<60 and escore<60:
        print("punishnment!!")
        
    elif escore<60 or mscore<60: 
        print("keep going")
else:
    print("error!")