if True:
    print("True")

if False:
    print("False") # never printed

if not False:
    print("Not False")

if 1 < 1:
    print("1<1") # never printed
elif 1 <= 0:
    print("1<=0") 
else:
    print("else 1")


if 1 < 1 :
    print("1<1") # never printed
elif 1<=1:
    print("1<=1") # it stopped here
elif 2<=2:
    print("2<=2") # never printed
else:
    print("else reached") # never printed


if 1 > 0 and 0 < 1:
    print("1 > 0 and 0 < 1")

if 0 < 1: print("0<1")

# Method 1
print("1 >= 1") if 1>=1 else print("1 < 1")

# Method 2
if 1 >= 1:
    print("1 >= 1")
else:
    print("1 < 1")

# --------------------------------------

# Method 1
if 0 > 1:
    print("1")
elif 0 < 1:
    print("2")
else:
    print("3")

# Method 2 
print("1") if 0 > 1 else print("2") if 0 < 1 else print("3")
