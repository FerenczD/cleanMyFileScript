#!/usr/bin/python3
import os

# Variables and flags
found = 0
fCounter = 0

print("Welcome to the overused comment deleter script!\n")
print("I will suggest you put this script on the same directory as the file you want to use")
print("You need to copy and paste the generated file into the original file location to apply changes")
input("Press Enter to continue...")

infile = input("\nType input file: ").rstrip()
outfile = infile

if not os.path.exists("generated files"):
    os.mkdir("generated files")

outfile = "generated files/" + outfile

comNbrs = int(input("How many comments do you want to delete?: "))

comment = [0]*comNbrs

for i in range (0, comNbrs):
    comment[i] = input("Type comment you want to delete: ").rstrip()

fi = open(infile, "r+")
fo = open(outfile, "w")

print("Comments to delete: ")
print(comment)

while True:
    line = fi.readline()

    for string in comment:
        if string in line:
            fCounter+=1
            found = 1
            continue
        
    if found == 0:
        fo.write(line)

    found = 0

    # EOF
    if not line:
        break

fi.close()
fo.close()

print("\nNumber of comment deleted: %d" %(fCounter))
input("Press Enter to continue...")
