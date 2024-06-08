import re
url=input("enter the url of twitter").strip()
username=re.sub(r"^(https://:)?(www\.)?twitter\.com/","",url)
print(f"username: {username}")

 