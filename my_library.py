import unicodedata
import numpy
from collections import Counter
#class EditexDistance:
class EditDistance:

    def hamming_distance(self, str1, str2):
        if len(str1) != len(str2):
            raise ValueError("Strings must be of equal length")

        distance = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance += 1

        return distance

    def levenshtein_distance(self, str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)

        # Create a matrix to store the distances between substrings
        matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

        # Initialize the matrix with values from 0 to len_str1 for the first column
        for i in range(len_str1 + 1):
            matrix[i][0] = i

        # Initialize the matrix with values from 0 to len_str2 for the first row
        for j in range(len_str2 + 1):
            matrix[0][j] = j

        # Fill the matrix using dynamic programming
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                cost = 0 if str1[i - 1] == str2[j - 1] else 1
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j - 1] + cost
                )

        return matrix[len_str1][len_str2]

    def damerau_levenshtein_distance(self, str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)

        # Create a matrix to store the distances between substrings
        matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

        # Initialize the matrix with values from 0 to len_str1 for the first column
        for i in range(len_str1 + 1):
            matrix[i][0] = i

        # Initialize the matrix with values from 0 to len_str2 for the first row
        for j in range(len_str2 + 1):
            matrix[0][j] = j

        # Fill the matrix using dynamic programming
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                cost = 0 if str1[i - 1] == str2[j - 1] else 1

                # Calculate transposition cost
                transposition_cost = 1
                if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j- 1]:
                    transposition_cost = 0

                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j - 1] + cost,
                    matrix[i - 2][j - 2] + transposition_cost # Transposition
                )

        return matrix[len_str1][len_str2]

    def jaro_distance(self, str1, str2):
        # Length of strings
        len_str1 = len(str1)
        len_str2 = len(str2)

        # Matching distance (maximum number of characters to match)
        match_distance = max(len_str1, len_str2) // 2 - 1
        if match_distance < 0:
            match_distance = 0

        # Arrays to store matching characters
        str1_matches = [False] * len_str1
        str2_matches = [False] * len_str2

        # Count of matching characters
        matches = 0

        # Count of transpositions
        transpositions = 0

        # Find matching characters
        for i in range(len_str1):
            start = max(0, i - match_distance)
            end = min(i + match_distance + 1, len_str2)

            for j in range(start, end):
                if not str2_matches[j] and str1[i] == str2[j]:
                    str1_matches[i] = True
                    str2_matches[j] = True
                    matches += 1
                    break

        # If there are no matches, return 0
        if matches == 0:
            return 0.0

        # Count transpositions
        k = 0
        for i in range(len_str1):
            if str1_matches[i]:
                while not str2_matches[k]:
                    k += 1
                if str1[i] != str2[k]:
                    transpositions += 1
                k += 1

        transpositions //= 2   # Divide by 2 as transpositions were counted twice

        # Calculate Jaro distance
        similarity = (
            matches / len_str1 +
            matches / len_str2 +
            (matches - transpositions) / matches
        ) / 3

        return similarity

    def jaro_winkler_distance(self, str1, str2, prefix_scale=0.1):
        # Jaro similarity
        jaro_similarity = self.jaro_distance(str1, str2)

        # Length of common prefix (up to a maximum of 4 characters)
        prefix_length = 0
        max_prefix_length = min(4, min(len(str1), len(str2)))
        for i in range(max_prefix_length):
            if str1[i] == str2[i]:
                prefix_length += 1
            else:
                break

        # Calculate Jaro-Winkler distance
        jaro_winkler_distance = jaro_similarity + (prefix_length * prefix_scale * (1 - jaro_similarity))

        return jaro_winkler_distance

class SequenceBased:
    def lcs(str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)

        # Create a table for storing the LCS lengths
        lcs_table = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

        # Fill the table with LCS lengths
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
                else:
                    lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

        # Find the LCS string
        lcs_string = ""
        i, j = len_str1, len_str2
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs_string = str1[i - 1] + lcs_string
                i -= 1
                j -= 1
            elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return lcs_table[len_str1][len_str2], lcs_string

    def longest_common_substring(self, seq1, seq2):
        m = [[0] * (1 + len(seq2)) for i in range(1 + len(seq1))]
        longest, x_longest = 0, 0
        for x in range(1, 1 + len(seq1)):
            for y in range(1, 1 + len(seq2)):
                if seq1[x - 1] == seq2[y - 1]:
                    m[x][y] = m[x - 1][y - 1] + 1
                    if m[x][y] > longest:
                        longest = m[x][y]
                        x_longest = x
                else:
                    m[x][y] = 0
        return seq1[x_longest - longest: x_longest]


    def gestalt_pattern_matching(self, pattern, text):
        # Your gestalt pattern matching logic here
        # This could involve comparing patterns based on structure, not just characters
        # This example simply checks if the pattern is a substring of the text
        if pattern in text:
            return True
        else:
            return False
from collections import Counter
import numpy as np

class TokenBased:
    @staticmethod
    def generate_qgrams(input_string, q):
        """
        Generate q-grams for the given input string.

        :param input_string: The input string.
        :param q: The size of the q-grams.
        :return: A list of q-grams.
        """
        qgrams = []
        for i in range(len(input_string) - q + 1):
            qgram = input_string[i:i + q]
            qgrams.append(qgram)
        return qgrams

    @staticmethod
    def overlap_coefficient(set_A, set_B):
        intersection = len(set_A.intersection(set_B))
        min_size = min(len(set_A), len(set_B))
        overlap = intersection / min_size if min_size != 0 else 0
        return overlap

    @staticmethod
    def jaccard_similarity(set1, set2):
        """
        Calculate the Jaccard similarity between two sets.

        :param set1: The first set.
        :param set2: The second set.
        :return: The Jaccard similarity.
        """
        intersection_size = len(set(set1).intersection(set2))
        union_size = len(set(set1).union(set2))
        return intersection_size / union_size if union_size > 0 else 0.0

    @staticmethod
    def dice_coefficient(set1, set2):
        """
        Calculate the Dice coefficient between two sets.

        :param set1: The first set.
        :param set2: The second set.
        :return: The Dice coefficient.
        """
        intersection_size = len(set(set1).intersection(set2))
        total_size = len(set1) + len(set2)
        return (2.0 * intersection_size) / total_size if total_size > 0 else 0.0
    
    @staticmethod
    def editex_distance(str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)

        # Create a distance matrix
        distance = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

        # Initialize the distance matrix
        for i in range(len_str1 + 1):
            distance[i][0] = i
        for j in range(len_str2 + 1):
            distance[0][j] = j

        # Fill in the matrix
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                cost = 0 if str1[i - 1] == str2[j - 1] else 1
                distance[i][j] = min(distance[i - 1][j] + 1,  # Deletion
                                     distance[i][j - 1] + 1,  # Insertion
                                     distance[i - 1][j - 1] + cost)  # Substitution or no change

        # Return the editex distance
        return distance[len_str1][len_str2]

    @staticmethod
    def bag_euclidean_distance(bag1, bag2):
        freq1 = Counter(bag1)
        freq2 = Counter(bag2)
        all_items = set(freq1) | set(freq2)
        
        vector1 = np.array([freq1[item] for item in all_items])
        vector2 = np.array([freq2[item] for item in all_items])
        
        distance = np.linalg.norm(vector1 - vector2)
        return distance


class PhoneticSensitive:
    def __init__(self):
        pass

    def smith_waterman(self, seq1, seq2, match=2, mismatch=-1, gap_penalty=-1):
        rows = len(seq1) + 1
        cols = len(seq2) + 1

        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        max_score = 0
        max_pos = (0, 0)

        for i in range(1, rows):
            for j in range(1, cols):
                if seq1[i - 1] == seq2[j - 1]:
                    score = match
                else:
                    score = mismatch

                diagonal = matrix[i - 1][j - 1] + score
                up = matrix[i - 1][j] + gap_penalty
                left = matrix[i][j - 1] + gap_penalty

                matrix[i][j] = max(0, diagonal, up, left)

                if matrix[i][j] > max_score:
                    max_score = matrix[i][j]
                    max_pos = (i, j)

        return max_score, max_pos
    def __init__(self):
        pass

    @staticmethod
    def editex_distance(str1, str2):
        m, n = len(str1), len(str2)

        # ماتریس برای ذخیره اطلاعات امتیازها
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # پر کردن ماتریس
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],        # حذف
                                       dp[i - 1][j],        # اضافه
                                       dp[i - 1][j - 1])    # جابجایی

        return dp[m][n]




    def align_syllables(self, word1, word2):
        from nltk.tokenize import SyllableTokenizer
        tokenizer = SyllableTokenizer()
        syllables1 = tokenizer.tokenize(word1)
        syllables2 = tokenizer.tokenize(word2)

        # Perform alignment logic between syllables1 and syllables2

        return syllables1, syllables2