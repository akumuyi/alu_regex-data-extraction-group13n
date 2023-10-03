import re
import json

# Open the username.txt file for reading
with open("Username.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Compile the regular expression for extracting usernames
username_regex = re.compile(r"@[^\s]+")

# Extract all of the usernames from the text
usernames = username_regex.findall(text)

# Create a JSON object to store the extracted usernames
json_object = {
    "usernames": usernames
}

# Write the JSON object to a file
with open("usernames.json", "w") as f:
    for username in usernames:
        print(username)

