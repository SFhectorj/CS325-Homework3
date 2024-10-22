# Question 1A
# TOP-DOWN Approach

def dna_match_topdown(DNA1, DNA2):
    """
    This function uses a top-down approach of dynamic programming to
    find similarities between two sequences.
    """

    memo_table = {}

    def dna_matching(i, j):
        """
        This helper function will check the sequences for a match and will store
        the appropriate matches in the table.
        """

        # Basecase: An empty string will not match anything
        if i == 0 or j == 0:
            return 0

        # Check for dupes
        if (i, j) in memo_table:
            # Returns the values already obtained for i and j.
            return memo_table[(i, j)]

        # Matching: When the characters match, let them be stored.
        if DNA1[i - 1] == DNA2[j - 1]:
            # Recursively solve sub problems then store in memo_table.
            memo_table[(i, j)] = 1 + dna_matching(i - 1, j - 1)
        else:
            # Take the maximum of both possibilities
            memo_table[(i, j)] = max(dna_matching(i - 1, j), dna_matching(i, j - 1))

        return memo_table[(i, j)]

    # use the helper function
    return dna_matching(len(DNA1), len(DNA2))


# Question 1B
# BOTTOM-UP Approach
def dna_match_bottomup(DNA1, DNA2):
    """
    This function uses a bottom up approach of dynamic programming to
    find similarities between two sequences.
    """
    # We need the length of the sequences stored in variables
    m = len(DNA1)
    n = len(DNA2)

    # Sets up a 2D table with dimensions of (m+1) x (n+1).
    # The table is initialized to 0.
    dp_table = [[0] * (n + 1) for k in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Look for a match
            if DNA1[i - 1] == DNA2[j - 1]:
                # increment length
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                # No match
                dp_table[i][j] = max(dp_table)






