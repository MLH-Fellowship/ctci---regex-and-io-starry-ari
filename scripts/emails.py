# Write the solution for "New Emails".
import re
with open("emails.csv") as f:
    txt = f.read()
    re.sub('@gmail.com', '@mlh.io', txt)