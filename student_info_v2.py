# Student Information Formatter
# Version 2: Added String Formatting

print("STUDENT INFORMATION FORMATTER")
print("--------------------------------")

# Inputs with .strip() to clean extra whitespace
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

# String Formatting
full_name = f"{first_name} {last_name}".title()
name_code = f"{first_name} {last_name}".upper()
section_upper = section.upper()
fav_subject_title = favorite_subject.title()

# Character Count Calculation
char_count = len(full_name)

# Formatted Output
print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", section_upper)
print("Favorite Subject:", fav_subject_title)
print("Character Count:", char_count)
