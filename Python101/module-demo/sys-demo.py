import sys

print(sys.version)
print(sys.executable)
print(sys.platform)

#for line in sys.stdin:
#    if line.strip() == "exit":
#        break
#    sys.stdout.write(">> {}".format(line))

for i in range(1,5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

for i in range(1,5):
    print(i)

# Status bar
import time

for i in range(0, 51):
    time.sleep(0.1)
    sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(50-i)))
    sys.stdout.flush()
sys.stdout.write("\n")


print(sys.argv) # [sys-demo.py]
# sys.argv[0] is always the name of the script

if (len(sys.argv) != 3):
    print(f"[X] To run {sys.argv[0]} enter a username and password")
    sys.exit(5)

username = sys.argv[1]
password = sys.argv[2]

sys.exit(0)
