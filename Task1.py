class UserInputValidator:
    def validate_positive_integers(self, input_list):

        valid_numbers = [int(item) for item in map(str, input_list) if item.isdigit() and int(item) > 0]

        print(f"Validation complete: {len(valid_numbers)} valid positive integers found.")
        
        return valid_numbers

validator = UserInputValidator()

Valid = [12, 3, "asd", -2]

valid_numbers = validator.validate_positive_integers(Valid)

print(valid_numbers)