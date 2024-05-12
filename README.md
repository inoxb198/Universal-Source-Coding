#Universal Source Coding#
To implement the following pieces of code as intended must understand the following algorithm we must infer the problem as an example

A User continuously inputs data in a file which is picked up by the "number_of_char_counter.py" file and as soon as a chunk of data has been put it runs the "egd_for_stat_proj_v1.py" to obtain the optimal weights using those optimal weights the "huffman_encoder.py" file will encode and create a dictonary with its corresponding binary string 

When a user writes another piece of text it will get the optimal weights and create the corresponding dictionary and concatenate it with the previous dictionary if the ordering of weights remains the same we do not need to apply huffman encoding if not we note the changes in the encoding scheme and incorporate it within the dictionary 

now we keep on doing like this 

For decoding at every step for the 1st step we decode directly 
from the second step onwards we note the changes in the dictionary made and correspondingly decode 

