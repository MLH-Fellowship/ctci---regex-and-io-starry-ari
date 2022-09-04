# Write the solution for "Filter Vowels".
import re
with open("../outputs/email_out.csv", 'w') as f:
    vowel_count = 0
    for i in f:
        if (i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I'
                or i == 'i' or i == 'O' or i == 'o'
                or i == 'U' or i == 'u'):
            vowel_count += 1
