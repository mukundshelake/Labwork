"""
The program to edit the .qvb file that is for CMM programming. 

We know for making the Imaging programs, we have to manually put the line like this "Video.Export "Hole1.bmp",FileType:=1" 
after every Report.Feature line in order to take the photo of the video window. To add this line we require the feature name
OR basically the name that we want the resulting image to have. That is most of the time the 'Tag' in the 'Results.ReportFeature"
line.

NOTE: This program works on .txt files, but the CMM codes are in .qvb. So one first has to copy the code from .qvb to a .txt 
file and input that file here. And then again has to copy the edited code into a .qvb file to feed into CMM.

Inputs: File path to the code to be edited. Put it inside the inputs/QVBCodes
Output: Edited code with the image taking abilities.

Status: Done
To Do: Correct the maximum inscribed circle calculation.
"""

import os
import re

def copy_paste_string_in_quotes(file_path, word):
    lines = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith(word):
                match = re.search('"([^"]*)"', line)
                if match:
                    string_in_quotes = match.group(1)
                    lines.append(line.strip())
                    ## Below is the line that will be pasted in the code.
                    lines.append('Video.Export "%s.bmp",FileType:=1' %string_in_quotes)
                else:
                    lines.append(line.strip())
            else:
                lines.append(line.strip())
    with open(file_path, 'w') as f:
        for line in lines:
            f.write(line + os.linesep)

file_path = 'inputs\QVBcode.txt'
word = 'Results.ReportFeature'
copy_paste_string_in_quotes(file_path, word)