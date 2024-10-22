# Question 1A
# TOP-DOWN Approach

def dna_match_topdown(DNA1, DNA2):
    """
    This function uses a top-down approach of dynamic programming to
    find similarities between two sequences.
    """

    memo_table = {}

    def dna_matching(i, j):

        # Basecase: An empty string will not match anything
        if i == 0 or j == 0:
            return 0

        # Check for dupes
        if (i, j) in memo_table:
            # Returns the values already obtained for i and j.
            return memo_table[(i, j)]

        # Matching: When the characters match, let them be stored.
        if DNA1[i - 1] == DNA2[j - 1]:
            memo_table[(i, j)] = 1 + dna_matching(i - 1, j - 1)
        else:



