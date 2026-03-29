try:
    f = open("adadadad")
except:
    print("The file does not exists!")

try:
    adadasda
except:
    print("The file does not exists!")

try:
    f = open("adadadad")
except Exception as e:
    print(e)

try:
    adadad
except Exception as e:
    print(e)

try:
    f = open("adadadad")
except FileNotFoundError:
    print("The file does not exists!")
except Exception as e:
    print(e)
finally:
    print("this message!") # get's executed each time 

n = 10
if n == 0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise Exception("n must be a int!")

n = 1
assert(n != 0)
print(1/n)