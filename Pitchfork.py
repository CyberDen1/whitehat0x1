import os

file = open('user.txt', 'r')

lines1 = 0

for line in file:
    lines1 += 1

file.close()
	
file = open('pass.txt', 'r')

lines2 = 0

for line in file:
    lines2 += 1

file.close()

file = open('user.txt', 'r')
for line in file:
    lines1 += 1
    fin = open("result_user.txt", "a")
    fin.write(line * lines2);
    fin.close()

def loop1():
    file = open('pass.txt', 'r')
    global lines1
    for line in file:
        lines1 += 1
        fin = open("result_pass.txt", "a")
        fin.write(line);
        fin.close()

file = open('user.txt', 'r')

lines3 = 0

for line in file:
    lines3 += 1

file.close()
	
for i in range(lines3):
    loop1()
