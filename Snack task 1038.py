Line1=input().split()
X=int(Line1[0])
Y=int(Line1[1])
Total=0.0
if (X==1) :
    Total=4.00*Y
elif (X==2) :
    Total=4.50*Y
elif (X==3) :
    Total=5.00*Y
elif (X==4) :
    Total=2.00*Y
elif (X==5) :
    Total=1.50*Y
print("Total: R$ %0.2f"%Total)