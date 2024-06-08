import re
email=input("Enter email").strip()

if re.search(r"^\w+@(\w\.)?\w\.edu$",email,re.IGNORECASE):
    print ("valid")
else:
    print("invalid")