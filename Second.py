from Task1 import UserInputValidator

validation1 = UserInputValidator()
validation2 = UserInputValidator()

is_it_integers1 = [13, "Love", "Hate", 2, -2]
is_it_integers2 = ["Exam", 20, 999, "Hope", 0]

valid1 = validation1.validate_positive_integers(is_it_integers1)
valid2 = validation2.validate_positive_integers(is_it_integers2)

print(valid1)
print(valid2)