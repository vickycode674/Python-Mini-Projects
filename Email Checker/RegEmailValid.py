#a-z
#0-9
# . _ time 1
# @ time 1
# .  2,3


import re
Email_conditon = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Enter your Email : ')

if re.search(Email_conditon,user_email):
    print("Right Email")
else:
    print("Wromg email")

# Certainly! Let's break down the regular expression `^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$` character by character:
#
# 1. `^`: Asserts the start of a line.
#
# 2. `[a-z]+`: Matches one or more lowercase alphabetic characters from a to z.
#
# 3. `[\._]?`: Matches either a dot `.` or an underscore `_` zero or one time. The `?` makes the preceding character class optional.
#
# 4. `[a-z0-9]+`: Matches one or more lowercase alphabetic characters from a to z or digits from 0 to 9.
#
# 5. `[@]`: Matches the "@" symbol.
#
# 6. `\w+`: Matches one or more word characters, which include letters, digits, and underscores.
#
# 7. `[.]`: Matches a dot `.`.
#
# 8. `\w{2,3}`: Matches two or three word characters, representing the top-level domain (TLD).
#
# 9. `$`: Asserts the end of a line.
#
# So, altogether, the regular expression `^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$` is used to validate an email address format. It checks for the following:
#
# - Starts with one or more lowercase alphabetic characters.
# - May contain an optional dot `.` or underscore `_`.
# - Followed by one or more lowercase alphabetic characters or digits.
# - Contains the "@" symbol.
# - Followed by one or more word characters.
# - Followed by a dot `.`.
# - Ends with two or three word characters representing the top-level domain (TLD), like `.com`, `.org`, `.net`, etc.