
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
