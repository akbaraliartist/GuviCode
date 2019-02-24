print("Enter 'x' for exit.");
num = input();
if num == 'x':
    exit();
try:
    year = int(num);
except ValueError:
    print("Please, enter year...exiting...");
else:
    if((year%4 == 0) and (year%100 != 0)):
        print("yes");
    elif((year%100 == 0) and (year%400 == 0)):
    	print("yes");
    elif(year%400 == 0):
    	print("yes");
    else:
    	print("no");
