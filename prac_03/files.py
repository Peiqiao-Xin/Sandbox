"""

open "name.txt" for write as out_file
name ← input("What is your name? ")
print name to out_file
close out_file

open "name.txt" for read as in_file
name ← read_all(in_file).strip()
close in_file
print "Hi " + name + "!"

open "numbers.txt" for read as in_file
number1 ← int(read_line(in_file))
number2 ← int(read_line(in_file))
close in_file
print number1 + number2

total ← 0
open "numbers.txt" for read as in_file
for line in in_file
  total ← total + int(line)
close in_file
print total
"""

# 1.
# We can write using print or write, out_file.write(name)
# In most cases, print is easier and more familiar
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2.
# Here we choose read() because we want the whole contents
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
# Here we choose readline() because we need separate lines, and we don't want every line
# It would be inefficient to use readlines() and then select only the first 2 values
# Note that .strip() is unnecessary since int() handles that whitespace
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4.
# Here we choose for line in file because we want every line
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)