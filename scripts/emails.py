# Write the solution for "New Emails".
import re

with open("../outputs/email_out.csv", 'w') as o:
    with open("../inputs/emails.csv", "r") as f:
        for line in f:
            name = re.split(',', line)
            o.write(name[0] + "mlh.io\n")
