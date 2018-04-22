import string

class Pass_test():
    def long_enough(pw):
        return len(pw) >= 6

    def has_lowercase(pw):
        return len(set(string.ascii_lowercase).intersection(pw)) > 0

    def has_uppercase(pw):
        return len(set(string.ascii_uppercase).intersection(pw)) > 0

    def has_numeric(pw):
        return len(set(string.digits).intersection(pw)) > 0

    def has_special(pw):
        return len(set(string.punctuation).intersection(pw)) > 0

    def test_password1(pw, tests=[long_enough, has_lowercase, has_uppercase, has_numeric]):
        for test in tests:
            if not test(pw):
                print(test.__doc__)
                return False
        return True

    def test_password2(pw, tests=[long_enough, has_lowercase, has_uppercase, has_special]):
        for test in tests:
            if not test(pw):
                print(test.__doc__)
                return False
        return True
