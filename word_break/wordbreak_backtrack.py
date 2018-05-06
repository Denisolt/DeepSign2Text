from read_english_dictionary import *

# Prints all possible word breaks of given string
def wordBreak(word, tolerance = 0):
    # find all possible results
    results = []
    # last argument is prefix
    wordBreakUtil(word, (0, ""), results)
    n = len(results)
    # continue only if some answers
    if n > 0:
        # prioritize fewer spaces
        results.sort()
        # find candidates with fewer spaces
        minimum = results[0][0] + tolerance
        index = n
        for i in range(1, n):
            if results[i][0] > minimum:
                index = i
                break
        results = results[:i]
    # process results
    result = []
    for pair in results:
        result.append(pair[1])
    # print (results)
    return result

# result store the current prefix with spaces between words
def wordBreakUtil(word, pair, results):
    n = len(word)
    count, result = pair
    # Process all prefixes one by one
    for i in range(1, n+1):
        # extract substring from 0 to i in prefix
        prefix = word[:i]
        
        # if dictionary conatins this prefix, then we check for remaining string.
        # Otherwise we ignore this prefix (there is no else for this if) and try next
        if check_word(prefix):
            # if no more elements are there, print it
            if (i == n):
                # add this element to previous prefix
                # result += prefix
                results.append((count, result + prefix))
                return None
            wordBreakUtil(word[i:], (count+1, result + prefix + " "), results);

if __name__ == '__main__':
    define_words("words_dictionary_small.json")
