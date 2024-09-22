import unittest

from my_library import EditDistance, SequenceBased, TokenBased, PhoneticSensitive

#Example for EditDistance english language
ed = EditDistance()
str1 = "karolin"
str2 = "kathrin"

print(ed.hamming_distance(str1, str2))  # hamming_distance
print(ed.levenshtein_distance(str1, str2))  #levenshtein_distance
print(ed.damerau_levenshtein_distance(str1, str2))  #damerau_levenshtein_distance  
print(ed.jaro_distance(str1, str2))  #jaro_distance
print(ed.jaro_winkler_distance(str1, str2))  #jaro_winkler_distance

#Example for EditDistance persion language

ed = EditDistance()
str1 = "کارولین"
str2 = " کاترین"

print(ed.hamming_distance(str1, str2))  # hamming_distance
print(ed.levenshtein_distance(str1, str2)) #levenshtein_distance
print(ed.damerau_levenshtein_distance(str1, str2))  #damerau_levenshtein_distance  
print(ed.jaro_distance(str1, str2)) #jaro_distance
print(ed.jaro_winkler_distance(str1, str2))  #jaro_winkler_distance

#-------------------------------------------------------------------------------------------------------------------------------


# Example usage for english language:
sb = SequenceBased()
sequence1 = "AFGBCDGH"
sequence2 = "AFGEDFHR"

result = sb.longest_common_substring(sequence1, sequence2)
print(f"The Longest Common Subsequence is: {result}")

# Example usage for persion language:
sb = SequenceBased()
sequence1 = "سلام دنیا"
sequence2 = "سلام بر دنیا"

result = sb.longest_common_substring(sequence1, sequence2)
print(f"The Longest Common Subsequence is: {result}")
#----------------------------------------------------------------------------------------------------------------------------
# Example usage for english language :
# Create an instance of the SequenceBased class
seq_based = SequenceBased()

# Test case 1: Two sequences with a common substring
seq1 = "banana"
seq2 = "anana"
result = seq_based.longest_common_substring(seq1, seq2)
print("Longest common substring:", result)  # Should print "anana"

# Test case 2: Two sequences with no common substring
seq1 = "abcde"
seq2 = "fghij"
result = seq_based.longest_common_substring(seq1, seq2)
print("Longest common substring:", result)  # Should print ""

# Test case 3: Two sequences with a common substring of length 1
seq1 = "hello"
seq2 = "world"
result = seq_based.longest_common_substring(seq1, seq2)
print("Longest common substring:", result)  # Should print "l"

# Test case 4: Two sequences with a common substring at the beginning
seq1 = "abcdef"
seq2 = "abcdxyz"
result = seq_based.longest_common_substring(seq1, seq2)
print("Longest common substring:", result)  # Should print "abcd"

# Test case 5: Two sequences with a common substring at the end
seq1 = "xyzabcdef"
seq2 = "uvwxyzabcd"
result = seq_based.longest_common_substring(seq1, seq2)
print("Longest common substring:", result)  # Should print "abcd"

# Example usage for persion language:
seq1 = ["ماشین", "ماشین_دوم", "ماشین_سوم"]
seq2 = ["ماش", "ماشین_دوم", "ماشین_چهارم"]
result = [SequenceBased().longest_common_substring(seq1[i], seq2[i]) for i in range(len(seq1))]
print(result)
#--------------------------------------------------------------------------------------------------------------------------------
seq_based = SequenceBased()
pattern = "text"
text = "This is a test text."
result = seq_based.gestalt_pattern_matching(pattern, text)
print(result)

seq_based = SequenceBased()
pattern = "متن"
text = "این یک متن تست است."
result = seq_based.gestalt_pattern_matching(pattern, text)
print(result)

#--------------------------------------------------------------------------------------------------------
#generate_qgrams
# Example usage for english language
tb = TokenBased()
sequence = "hello"
q = 2

qgrams = tb.generate_qgrams(sequence, q)
print(f"The {q}-grams for the string '{sequence}' are: {qgrams}")

# Example usage for persion language

sequence = "سلام"
q = 2

qgrams = tb.generate_qgrams(sequence, q)
print(f"The {q}-grams for the string '{sequence}' are: {qgrams}")

#--------------------------------------------------------------------------------------------------------------------
# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
coefficient = TokenBased.overlap_coefficient(set1, set2)
print(f"The overlap coefficient between {set1} and {set2} is {coefficient}.")

# Example usage with English words:
english_set1 = {"apple", "banana", "orange", "grape", "melon"}
english_set2 = {"orange", "grape", "watermelon", "pineapple"}
english_coefficient = TokenBased.overlap_coefficient(english_set1, english_set2)
print(f"The overlap coefficient between English sets is {english_coefficient}.")

# Example usage with Persian words:
persian_set1 = {"سیب", "موز", "پرتقال", "انگور", "هندوانه"}
persian_set2 = {"پرتقال", "انگور", "هندوانه", "انبه"}
persian_coefficient = TokenBased.overlap_coefficient(persian_set1, persian_set2)
print(f"The overlap coefficient between Persian sets is {persian_coefficient}.")
#-------------------------------------------------------------------------------------------------------

from collections import Counter
import numpy as np

# Define two bags of words
bag1 = ["apple", "orange", "banana", "apple", "banana", "apple"]
bag2 = ["apple", "banana", "banana", "orange", "orange"]

# Calculate the bag Euclidean distance
distance = TokenBased.bag_euclidean_distance(bag1, bag2)

print("Bag Euclidean Distance:", distance)
#---------------------------------------------------------------------------------------------------------
# استفاده از کلاس و متد
sequence1 = "AGTACGCA"
sequence2 = "TATGC"
phonetic_sensitive = PhoneticSensitive()
score, position = phonetic_sensitive.smith_waterman(sequence1, sequence2)

print(f"Max Score: {score}")
print(f"Position of Max Score: {position}")

# استفاده از کلاس و متد
sequence1 = "موتورسیکلت"
sequence2 = "موتور"
phonetic_sensitive = PhoneticSensitive()
score, position = phonetic_sensitive.smith_waterman(sequence1, sequence2)

print(f"Max Score: {score}")
print(f"Position of Max Score: {position}")
#----------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# ساخت یک نمونه از کلاس
phonetic_sensitive = PhoneticSensitive()

# مثال استفاده از تابع درون کلاس
str1 = "kitten"
str2 = "sitting"
result = PhoneticSensitive.editex_distance(str1, str2)
print(f"Editex distance between '{str1}' and '{str2}': {result}")
# اجرای تست تطابق اسایلابها
syllables1, syllables2 = phonetic_sensitive.align_syllables("banana", "bəˈnɑː.nə")
print("Syllables 1:", syllables1)
print("Syllables 2:", syllables2)

