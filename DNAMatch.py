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

        # 



