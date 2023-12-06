"""
@AssessMeTester_StringSimilarity.py
@brief String similarity algorithms for testers (Pytest)

Two versions:


@version 2.0
"""

import difflib



##Checking overlaping of two strings, A is the string we are searcing, B is the obained source 
##The minimum_overlapping_length defines the minimum overlaping match length - if the matched substring is shorter, it is ignored
#This is used to find string A in the string B, and checks the overlaping percentage. The string B can be some longer source
def get_string_overlaping_percentage(A, B, minimum_overlapping_length):
    # Create a SequenceMatcher object to compare the strings
    matcher = difflib.SequenceMatcher(None, A, B)

    # Get the matching blocks
    matching_blocks = matcher.get_matching_blocks()
   
    total_matching_chars=0
    for match in matching_blocks:
        if match.size>=minimum_overlapping_length:
            #print("MAtch size:" + str(match.size))
            #matching_substring = A[match.a:match.a + match.size]
            #print("Matching substring:", matching_substring)
            total_matching_chars +=match.size

    # Calculate the percentage of overlap
  
    overlap_percentage = (total_matching_chars / len(A))

    return overlap_percentage


##Calculate similarity between two stings
#First, it removes the emtpy space and tabs, then calls SequenceMatcher
#This is used when two strings should be similar. 
def string_similarity(s1, s2):
    # Calculate similarity ratio
    s1 = s1.replace(" ", "").replace("\t","")
    s2 = s2.replace(" ", "").replace("\t","")
    s1 = s1.strip()
    s2 = s2.strip()
    #with open("expected.txt", 'w') as file:
    #    file.write(s1)
    #with open("captured.txt", 'w') as file:
    #    file.write(s2)

    similarity_ratio = difflib.SequenceMatcher(None, s1, s2).ratio()
    return similarity_ratio