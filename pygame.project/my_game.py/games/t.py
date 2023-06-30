class x():
    def __init__(self):
        self.x= 1
z = x()

f = [z,z]
for i in range(1,3):
    print(f[i-1].x)
z.x = 2
for i in range(1,3):
    print(f[i-1].x)

