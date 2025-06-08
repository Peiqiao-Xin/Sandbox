"""

  try
    num ← int(input("enter the numerator: "))
    den ← int(input("enter the denominator: "))
    print(num / den)
  except valueError
    print("numerator and denominator must be valid numbers!")
  except zeroDivisionError
    print("cannot divide by zero!")
  print("finished.")
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")