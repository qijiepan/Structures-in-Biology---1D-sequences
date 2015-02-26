# Structures-in-Biology---1D-sequences

#Describe the design of the visualization
    when two sequences have the same mark, they could use the same letter to make an alignment. As for the gap, I use "_" to represent. And for mismatch, the only thing I did is to keep the same as match.
    Here I set +2 for match, -1 for mismatch and -2 for gap. it would looking for from the largest score in the ending to the begining. So it will choose the best subsequence for the original sequence.
    Also I use red to mark the same letter for the sequences. 


# Additions.
Bio : the data is from 1433B_HUMAN	14-3-3 protein beta/alpha and 1433E_HUMAN	14-3-3 protein epsilon 
Tech: You can change different score for match or mismatch or gap to get the different alignment.

# Running  program.
    the program is based on python and processing, which is pyde. the data is from the data.txt
