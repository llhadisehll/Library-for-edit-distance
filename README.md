# library for different edit distance methods
Edit distance, also known as Levenshtein distance, is a measure of the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into another.

In other words, it's a way to quantify the difference between two strings by counting the minimum number of operations needed to transform one string into the other.

## In this library, what algorithms have we used?
    - Hamming distance calculator
    - Levenshtein Distance Calculator
    - DamerauLevenshteinDistance
    - JaroWinkler Distance Calculator
    - JaroDistanceCalculator


Each class has a main method that calculates the distance between two character strings. Also, the JaroWinklerDistanceCalculator class has a submethod that calculates Jaro's similarity.

 To use these classes, it is enough to create an instance of the desired class and pass character strings as parameters. Then, you can use the main method of the class to calculate the distance between the strings.

---------------------------------------------------------------------------------------------------------------------------------------------------
## The HammingDistance Calculator class

This class is designed to calculate the Hamming distance between two strings of equal length. The Hamming distance is a measure of the number of positions at which the corresponding symbols are different.

Here's a breakdown of the class:

Initialization

The class takes three parameters in its constructor:

- `str1`: The first string to compare.

- `str2`: The second string to compare.

 - `language` : The language of the strings ( e.g. , 'fa' for Persian, 'en' for English). This parameter is used to handle special cases for languages that require it.
 
### Hamming Distance Calculation

The ***hamming_distance*** method calculates the Hamming distance between the two input strings. Here's how it works:

1. It checks if the two strings are of equal length. If not, it raises a ***ValueError***.

2.  It initializes a variable ***distance*** to 0, which will store the Hamming distance.

3. It iterates over the length of the strings using a for loop.

4. For each position, it checks if the corresponding symbols in the two strings are different. If they are, it increments the ***distance*** variable by 1.

5. If the language is Persian (or any other language that requires special handling), it checks for special cases, such as characters with multiple forms (e.g., ی and ى). If the characters are considered the same, it doesn't increment the ***distance*** variable.

6. Finally, it returns the calculated Hamming distance.

### Example Usage

Here's an example of how to use the HammingDistanceCalculator class:

**Calculate the Hamming distance between "کارولین" and "کاترین" (Persian)**
```python
string1 = "کارلین"
string2 = "کاترین"
language = 'fa'
hamming_distance_calculator = HammingDistanceCalculator(string1, string2, language)
distance = hamming_distance_calculator.hamming_distance()
print(f"The Hamming distance between '{string1}' and '{string2}' is {distance}.")
```

**Calculate the Hamming distance between "karolin" and "kathrin" (English)**
```python
string1 = "karolin"
string2 = "kathrin"
language = 'en'
hamming_distance_calculator = HammingDistanceCalculator(string1, string2, language)
distance = hamming_distance_calculator.hamming_distance()
print(f"The Hamming distance between '{string1}' and '{string2}' is {distance}.")
```
This code would output:
```python
 #output for fa language

==> The Hamming distance between 'کارلین' and 'کاترین' is 2 .

#output for en language
==> The Hamming distance between 'karolin' and 'kathrin' is 3.
```
### Review results
The Hamming distance is 2 because there are two positions where the corresponding symbols are different between the two strings.

First, it should be explained that the Hamming distance is calculated for two character strings of the same length. If the length of two character strings is different, Hamming distance is not defined for them.

Here, the two character substrings "Carlyn" and "Catherine" have length 6. So we can calculate the Hamming distance for them. To calculate the Hamming distance, we need to check the value of each method and if the two methods are not equal, we increase the distance.

For the character strings "Carlene" and "Catherine", we consider two methods together:

- Work: Both threads start together.
- Lin: The two methods are equal in this position.

But in other places, the methods are not equal. Therefore, the Hamming distance for these two character strings is equal to 2.

Also, for the strings "karolin" and "kathrin", the Hamming distance is equal to 3, because the modes are not equal in three positions:

- k: At the beginning of two character strings, the starting character is not equal to the letter k.

- a: after the second position of two character strings, the second character is not equal to the letter a.

- i: after the fourth position of two character strings, the fourth character is not equal to the letter i.

Therefore, the Hamming distance for these two character strings is equal

For the strings "karolin" and "kathrin", the Hamming distance is 3. This means that the methods are not equal in the three positions.

For example, at the beginning of two character strings, the starting character is not equal to the letter k. Also, after the second position of two character strings, the second character is not equal to the letter a. Also, after the fourth position of two character strings, the fourth character is not equal to the letter i.

Therefore, the Hamming distance for these two character strings is equal to 3.



---------------------------------------------------------------------------------------------------------------------------------------------------


## the Levenshtein distance Calculator class
Levenshtein distance (also known as edit distance) is a measure of similarity between two strings, which we will call stringA and stringB. The distance is the number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

For example, the Levenshtein distance between "kitten" and "sitting" is 3, since the following three edits change one into the other:

1. Substitute "k" for "s".
2. Substitute "e" for "i".
3. Append "g" at the end.
***LevenshteinDistanceCalculator*** is a class that calculates the Levenshtein distance between two input strings. Here's an example of how to use this class:

```python
string1 = "karolin"
string2 = "kathrin"

calculator = LevenshteinDistanceCalculator(string1, string2)
distance = calculator.distance()

print(f"The Levenshtein distance between '{string1}' and '{string2}' is {distance}.")
```
In this example, the Levenshtein distance between "karolin" and "kathrin" is calculated as 3, since the following three edits change one into the other:

1. Substitute "o" for "a".

2. Substitute "i" for "th".

3. Append "n" at the end.

The ***LevenshteinDistanceCalculator*** class can be useful in various natural language processing tasks, such as spell checking, correction, and text similarity analysis.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## DamerauLevenshteinDistanceCalculator

The Damerau-Levenshtein distance (also known as Damerau distance) is a measure of similarity between two strings, which we will call **stringA** and **stringB**. It is a variant of the Levenshtein distance, with an additional operation: transposition of two adjacent characters. The distance is the number of single-character edits (insertions, deletions, substitutions, or transpositions) required to change one word into the other.

For example, the Damerau-Levenshtein distance between "kitten" and "sitten" is 2, since the following two edits change one into the other:

1. Transpose "k" and "i".

2. Substitute "k" for "s".

***DamerauLevenshteinDistanceCalculator*** is a class that calculates the Damerau-Levenshtein distance between two input strings. Here's an example of how to use this class:
```python
string1 = "karolin"
string2 = "kathrin"

calculator = DamerauLevenshteinDistanceCalculator(string1, string2)
distance = calculator.distance()

print(f"The Damerau-Levenshtein distance between '{string1}' and '{string2}' is {distance}.")
```
In this example, the Damerau-Levenshtein distance between "karolin" and "kathrin" is calculated as 3, since the following three edits change one into the other:

1-Substitute "o" for "a".

2-Substitute "i" for "th".

3-Append "n" at the end.

The **DamerauLevenshteinDistanceCalculator** class can be useful in various natural language processing tasks, such as spell checking, correction, and text similarity analysis. It is particularly useful when dealing with typographical errors, as it can capture transpositions that the standard Levenshtein distance cannot.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## JaroWinklerDistanceCalculator

The Jaro-Winkler distance is a measure of similarity between two strings, which we will call stringA and stringB. It is a variant of the Jaro distance, with an additional prefix rule that gives more weight to the beginning of the strings. The distance ranges from 0 (completely dissimilar) to 1 (identical).

The Jaro distance is calculated based on the number of common characters, transpositions, and the length of the strings. The Jaro-Winkler distance extends the Jaro distance by adding a prefix rule that rewards similarity at the beginning of the strings.

The Jaro-Winkler distance is calculated using the following formula:
```
JaroWinkler(stringA, stringB) = Jaro(stringA, stringB) + 0.1 * prefixLength * (1 - Jaro(stringA, stringB))
```

where prefixLength is the length of the longest common prefix of stringA and stringB, up to a maximum of 4 characters.

JaroWinklerDistanceCalculatoris a class that calculates the Jaro-Winkler distance between two input strings. Here's an example of how to use this class:

```python
string1 = "karolin"
string2 = "kathrin"

calculator = JaroWinklerDistanceCalculator(string1, string2)
distance = calculator.distance()

print(f"The Jaro-Winkler distance between '{string1}' and '{string2}' is {distance}.")

```
In this example, the Jaro-Winkler distance between "karolin" and "kathrin" is calculated as 0.855, which indicates a high degree of similarity.

The JaroWinklerDistanceCalculator class can be useful in various natural language processing tasks, such as fuzzy string matching, correction, and text similarity analysis. It is particularly useful when dealing with strings that have a high degree of similarity, but are not exactly the same.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## JaroDistanceCalculator

The Jaro distance is a measure of similarity between two strings, which we will call stringA and stringB. It is a string comparison metric that calculates the similarity between two strings based on the number of common characters, transpositions, and the length of the strings. The distance ranges from 0 (completely dissimilar) to 1 (identical).

The Jaro distance is calculated using the following formula:

```Jaro(stringA, stringB) = (matches / lengthA + matches / lengthB + (matches - transpositions / 2) / matches) / 3```

where:

- lengthA and lengthB are the lengths of **stringA** and **stringB**, respectively.

- **matches** is the number of common characters between **stringA** and **stringB**.

- **transpositions** is the number of transpositions between stringA and stringB.

**JaroDistanceCalculator** is a class that calculates the Jaro distance between two input strings. Here's an example of how to use this class:

```python
string1 = "karolin"
string2 = "kathrin"

calculator = JaroDistanceCalculator(string1, string2)
distance = calculator.distance()

print(f"The Jaro distance between '{string1}' and '{string2}' is {distance}.")

```
In this example, the Jaro distance between "karolin" and "kathrin" is calculated as 0.833, which indicates a moderate degree of similarity.

The **JaroDistanceCalculator** class can be useful in various natural language processing tasks, such as fuzzy string matching, correction, and text similarity analysis. It is particularly useful when dealing with strings that have a moderate degree of similarity, but are not exactly the same.