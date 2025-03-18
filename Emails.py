
import re

def extract_emails_from_file(file_path):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    emails = re.findall(email_pattern, content)
    return emails

# Example usage
file_path = './code.txt'  
emails = extract_emails_from_file(file_path)

for email in emails:
    print(email)



import re

def validate_password(password):
    password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$'
    
    if re.match(password_pattern, password):
        return "Password is valid."
    else:
        return "Password is invalid. It must contain at least one uppercase letter, one lowercase letter, one number, and one special character. It should be at least 8 characters long."

password = "Passw0rd@2025"
print(validate_password(password)) 

password = "weakpassword"
print(validate_password(password)) 




import re

def validate_telephone_number(phone_number):
    phone_pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    
    if re.match(phone_pattern, phone_number):
        return "Phone number is valid."
    else:
        return "Phone number is invalid. It should be in the format (XXX) XXX-XXXX or XXX-XXX-XXXX."

phone_number = "(123) 456-7890"
print(validate_telephone_number(phone_number))

phone_number = "123-4567"
print(validate_telephone_number(phone_number)) 

