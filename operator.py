# Basic arithmetic
print(15 + 7) # → 22
print(15 - 7) # → 8
print(15 * 7) # → 105
# Division always gives float in Python 3
print(7 / 2) # → 3.5 (float)
print(4 / 2) # → 2.0 (float, not 2!)
# Floor division — rounds DOWN always
print(17 // 5) # → 3 (not 3.4)
print(-17 // 5) # → -4 (rounds DOWN, not towards zero!)
# Modulus — the remainder after floor division
print(17 % 5) # → 2 (17 = 3×5 + 2)
print(10 % 2) # → 0 (10 divides evenly — no remainder)
print(7 % 2) # → 1 (7 is odd)
# Exponentiation
print(2 ** 10) # → 1024
print(64 ** 0.5) # → 8.0 (square root)
print(27 ** (1/3)) # → 3.0 (cube root)
# Basic comparisons
print(10 == 10) # → True
print(10 != 5) # → True
print(10 > 20) # → False
# Chained comparisons — unique to Python, reads like maths
x = 5
print(1 < x < 10) # → True (x is between 1 and 10)
print(0 <= x <= 5) # → True
print(5 < x < 10) # → False (x is not greater than 5)
# String comparisons — lexicographic (letter by letter)
print("apple" < "banana") # → True ('a' < 'b' in Unicode)
print("Python" == "python") # → False (case-sensitive!)
# Comparing booleans with numbers
print(1 == True) # → True (True equals 1 in Python)
print(0 == False) # → True (False equals 0 in Python)
print(1 == "1") # → False (int and str are different types)
# Compound assignment operators
score = 50
score += 10 # score is now 60
score *= 2 # score is now 120
score -= 20 # score is now 100
print(score) # → 100
# Multiple assignment — assign several variables in one line
a = b = c = 0 # all three become 0
print(a, b, c) # → 0 0 0
# Tuple unpacking — assign different values in one line
x, y, z = 1, 2, 3
print(x, y, z) # → 1 2 3
# Swap variables — Pythonic way, no temporary variable needed
a, b = 10, 20
a, b = b, a # swap!
print(a, b) # → 20 10
# and — both conditions must be True
age = 20
has_id = True
print(age >= 18 and has_id) # → True (both conditions satisfied)
# or — at least one condition must be True
is_student = True
is_teacher = False
print(is_student or is_teacher) # → True (one is True)
# not — inverts the boolean value
print(not True) # → False
print(not False) # → True
# Short-circuit with 'and' — right side skipped if left is False
print(False and 1/0) # → False (no ZeroDivisionError!)
# Short-circuit with 'or' — right side skipped if left is True
print(True or 1/0) # → True (no ZeroDivisionError!)
# Combining logical operators with comparison operators
marks = 72
print(marks >= 40 and marks <= 100) # → True (valid score range)
print(marks < 40 or marks > 100) # → False (not out of range)
# bin() shows the binary representation of any number
print(bin(5)) # → 0b101
print(bin(3)) # → 0b11
# AND — 1 only where both bits are 1
print(5 & 3) # → 1 (0101 & 0011 = 0001)
# OR — 1 where either bit is 1
print(5 | 3) # → 7 (0101 | 0011 = 0111)
# XOR — 1 where bits are different
print(5 ^ 3) # → 6 (0101 ^ 0011 = 0110)
# Left shift — multiply by powers of 2
print(5 << 1) # → 10 (5 × 2)
print(5 << 2) # → 20 (5 × 4)
# Right shift — divide by powers of 2
print(20 >> 1) # → 10 (20 ÷ 2)
print(20 >> 2) # → 5 (20 ÷ 4)
# Membership — checking if a value exists in a sequence
print("py" in "python") # → True
print("Java" in "python") # → False
print("z" not in "hello") # → True
# Identity — == checks value equality, is checks object identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b) # → True (same values)
print(a is b) # → False (different objects in memory)
print(a is c) # → True (same object — c points to a)
# The correct way to check for None — always use 'is'
x = None
print(x is None) # → True ✅ correct
print(x == None) # → True ⚠️ works but not recommended
# * before + (same as BODMAS)
print(2 + 3 * 4) # → 14 (* before +)
print((2 + 3) * 4) # → 20 (parentheses first)
# ** is right to left
print(2 ** 3 ** 2) # → 512 (2 ** (3 ** 2) = 2 ** 9)
print((2 ** 3) ** 2) # → 64 (different result with brackets!)
# Comparison before logical operators
print(5 > 3 and 2 < 4) # → True (comparisons first, then and)
print(not True or True) # → True (not binds tighter than or)
# When unsure — always use parentheses for clarity
result = (5 + 3) * (10 - 4)
print(result) # → 48 (clear and unambiguous)