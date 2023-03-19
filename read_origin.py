#Making script importable as a module.
if __name__ == '__main__':

#importing regular expressions
    import re

#printing the message that we're opening origin.txt.
    print('Opening origin.txt as input file')
#now we want to open the origin.txt file as the input, and we want the output to be our results from the pattern search.
    with open('origin.txt', 'r') as in_stream:
        print('Opening output_origin.txt as output file')    
        with open('output_origin.txt', 'w') as out_stream:
#Now we create a for loop that will start at line 1, then iterate over each line, and record the line number and matching word.
            for line_number, line in enumerate (in_stream, start = 1):
#Creating line_find to search for the matching word in each line. 
                line_find = re.compile(r'\b(heritable|inheritance|inherit|inherited|inheritable)\b', re.IGNORECASE)
#Creating match_the_line match the line number with the word.
                match_the_line = line_find.finditer(line)
#Here is the for loop that will take the matches from match_the_line and put them into an output file.
                for match in match_the_line:
#Now appending each matching line number and matching word to the output file, ensuring that the info is separated by a tab.
                        out_stream.write(f"{line_number}\t{match.group(0)}\n")
