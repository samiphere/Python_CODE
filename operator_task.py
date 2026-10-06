# Arithmetic Operators in Python
# Basic arithmetic
print(15 + 7)  # → 22 (Addition)
print(15 - 7)  # → 8 (Subtraction)
print(15 * 7)  # → 105 (Multiplication)

# Division always gives float in Python 3
print(7 / 2)  # → 3.5 (Float Division)
print(4 / 2)  # → 2.0 (Float Division)

# Floor division — rounds DOWN always
print(17 // 5)  # → 3 (Floor Division)
print(-17 // 5)  # → -4 (Rounds down towards negative infinity)

# Modulus — the remainder after floor division
print(17 % 5)  # → 2 (17 = 3×5 + 2)
print(10 % 2)  # → 0 (Even)
print(7 % 2)  # → 1 (Odd)

# Exponentiation
print(2**10)  # → 1024 (Power)
print(64**0.5)  # → 8.0 (Square root)
print(27 ** (1 / 3))  # → 3.0 (Cube root)

# Comparison (Relational) Operators
# Basic comparisons
print(10 == 10)  # → True (Equal to)
print(10 != 5)  # → True (Not equal to)
print(10 > 20)  # → False (Greater than)

# Chained comparisons — unique to Python, reads like maths
x = 5
print(1 < x < 10)  # → True (x is between 1 and 10)
print(0 <= x <= 5)  # → True (Less than or equal to)
print(5 < x < 10)  # → False

# String comparisons — lexicographic (letter by letter in Unicode)
print("apple" < "banana")  # → True ('a' < 'b')
print("Python" == "python")  # → False (Case-sensitive!)

# Comparing booleans with numbers
print(1 == True)  # → True (True equals 1 in Python)
print(0 == False)  # → True (False equals 0 in Python)
print(1 == "1")  # → False (int and str are different types)

# Assignment & Compound Assignment Operators
# Compound assignment operators
score = 50
score += 10  # score is now 60 (score = score + 10)
score *= 2  # score is now 120 (score = score * 2)
score -= 20  # score is now 100 (score = score - 20)
print(score)  # → 100

# Multiple assignment — assign several variables in one line
a = b = c = 0  # all three become 0
print(a, b, c)  # → 0 0 0

# Tuple unpacking — assign different values in one line
x, y, z = 1, 2, 3
print(x, y, z)  # → 1 2 3

# Swap variables — Pythonic way, no temporary variable needed
a, b = 10, 20
a, b = b, a  # swap!
print(a, b)  # → 20 10

# Logical Operators
# and — both conditions must be True
age = 20
has_id = True
print(age >= 18 and has_id)  # → True

# or — at least one condition must be True
is_student = True
is_teacher = False
print(is_student or is_teacher)  # → True

# not — inverts the boolean value
print(not True)  # → False
print(not False)  # → True

# Short-circuit evaluation
print(False and 1 / 0)  # → False (right side skipped, no ZeroDivisionError)
print(True or 1 / 0)  # → True (right side skipped, no ZeroDivisionError)

# Combining logical operators with comparison operators
marks = 72
print(marks >= 40 and marks <= 100)  # → True
print(marks < 40 or marks > 100)  # → False

# Bitwise Operators
# Helper to view binary representation
print(bin(5))  # → 0b101
print(bin(3))  # → 0b011

# Bitwise AND (&) — 1 only where both bits are 1
print(5 & 3)  # → 1 (0101 & 0011 = 0001)

# Bitwise OR (|) — 1 where either bit is 1
print(5 | 3)  # → 7 (0101 | 0011 = 0111)

# Bitwise XOR (^) — 1 where bits are different
print(5 ^ 3)  # → 6 (0101 ^ 0011 = 0110)

# Left Shift (<<) — multiply by powers of 2
print(5 << 1)  # → 10 (5 × 2^1)
print(5 << 2)  # → 20 (5 × 2^2)

# Right Shift (>>) — divide by powers of 2
print(20 >> 1)  # → 10 (20 ÷ 2^1)
print(20 >> 2)  # → 5 (20 ÷ 2^2)

# Membership Operators
# Checking existence in sequences (strings, lists, etc.)
print("py" in "python")  # → True
print("Java" in "python")  # → False
print("z" not in "hello")  # → True

# Identity Operators
# Checking if two variables point to the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # → True (same values)
print(a is b)  # → False (different objects in memory)
print(a is c)  # → True (same object in memory)

# Checking for None — best practice is using identity ('is')
x = None
print(x is None)  # → True ✅ recommended way
print(x == None)  # → True ⚠️ works, but not recommended