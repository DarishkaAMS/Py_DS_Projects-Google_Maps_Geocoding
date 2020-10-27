import os

# Absolute path
this_file_path = os.path.abspath(__file__)
print(this_file_path)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
print("BASE_DIR", BASE_DIR, "ENTIRE_PROJECT_DIR", ENTIRE_PROJECT_DIR)

# email_txt = "templates/email.txt"

email_txt = os.path.join("templates", "email.txt")

content = ''

with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name='DarishkaAMS'))