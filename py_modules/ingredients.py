import re

# Open the Ingredients.txt file for reading
with open("/alu_regex-data-extraction-group13/txt_vault/Ingredients.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Strip all of the whitespace from the text
text = text.strip()

# Compile the regular expression for extracting ingredients lists
ingredients_regex = re.compile(r"(?P<ingredients>\b\w+(?:,\s\b\w+)*\b)", re.MULTILINE)

# Extract all of the ingredients lists from the text
ingredients_lists = ingredients_regex.findall(text)

# Print the extracted ingredients lists
for ingredients_list in ingredients_lists:
    print(ingredients_list)

