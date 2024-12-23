import re
#Weak Password Detector
class PasswordComplexityChecker:
    def __init__(self):
        """
        Initialize the password complexity checker.
        """
        self.uppercase_pattern = re.compile(r'[A-Z]')
        self.lowercase_pattern = re.compile(r'[a-z]')
        self.digit_pattern = re.compile(r'\d')
        self.special_char_pattern = re.compile(r'[$%*&_]')
        
    def check_password(self, password):
        """
        Check if the password meets the complexity requirements.
        """
        issues = []
        
        if not self.uppercase_pattern.search(password):
            issues.append("Password must contain at least one uppercase letter.")
        
        if not self.lowercase_pattern.search(password):
            issues.append("Password must contain at least one lowercase letter.")
        
        if not self.digit_pattern.search(password):
            issues.append("Password must contain at least one digit.")
        
        if not self.special_char_pattern.search(password):
            issues.append("Password must contain at least one special character from '$', '%', '*', '&', '_'.")
        
        if issues:
            return False, issues
        else:
            return True, ["Password meets the complexity requirements."]
    
    def get_user_input(self):
        """
        Get the password input from the user.
        """
        password = input("Enter a password to analyze: ")
        valid, issues = self.check_password(password)
        
        if valid:
            print("Password is valid!")
        else:
            print("Password is invalid:")
            for issue in issues:
                print(f" - {issue}")



password_checker = PasswordComplexityChecker()
password_checker.get_user_input()
