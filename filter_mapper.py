#!/usr/bin/python
import sys
import csv

# In this exercise, we are interested in the field 'body' (which is the 5th field, 
# line[4]). The objective is to count the number of forum nodes where 'body' either 
# contains none of the three punctuation marks: period ('.'), exclamation point ('!'), 
# question mark ('?'), or else 'body' contains exactly one such punctuation mark as the 
# last character. There is no need to parse the HTML inside 'body'. Also, do not pay
# special attention to newline characters.

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:

       if  "." not in line[4] and "!" not in line[4] and "?" not in line[4]:
            
           writer.writerow(line)
            
       elif ("." in line[4] and "!" not in line[4] and "?" not in line[4] and line[4][-1]== "." and line[4].count(".")==1):
           writer.writerow(line)         
       elif ("." not in line[4] and "!" in line[4] and "?" not in line[4] and line[4][-1]== "!" and line[4].count("!")==1):
           writer.writerow(line)         
       elif ("." not in line[4] and "!" not in line[4] and "?" in line[4] and line[4][-1]== "?" and line[4].count("?")==1):
           writer.writerow(line)         



test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
    
    

