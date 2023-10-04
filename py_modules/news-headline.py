import re

# Open the News-Headline.txt file for reading
with open("/alu_regex-data-extraction-group13/txt_vault/News-Headline.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Compile the regular expression for extracting news headlines
headline_regex = re.compile(r"(?P<headline>\w+(?:\s+\w+)*)\s+:\s+(?P<subheader>\w+(?:\s+\w+)*)")

# Extract all of the news headlines from the text
headline_lists = headline_regex.findall(text)

# Print the results of the regular expression matching to the console
for headline_list in headline_lists:
    print(headline_list)

