# Q1 Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq

# Q2  Find the Frequency of Each Character in a Word
def char_frequency(word):
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Q3 Find the First Non-Repeating Character in a Word
def first_non_repeating_char(word):
    freq = char_frequency(word)
    for ch in word:
        if freq[ch] == 1:
            return ch
    return None

# Q4 Check if Two Words are Anagrams
def are_anagrams(s1, s2):
    return char_frequency(s1) == char_frequency(s2)

# Q5 Find the First Repeating Character in a Word
def first_repeating_char(text):
    seen = set()
    for ch in text:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

# Q6 Move All Zeros to the End of an Array
def move_zeros_to_end(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    return non_zeros + zeros

# Q7 Find the Second Highest Number in an Array
def second_highest(nums):
    distinct = sorted(set(nums), reverse=True)
    if len(distinct) < 2:
        return None
    return distinct[1]

# Q8 Remove Duplicates from an Array
def remove_duplicates(nums):
    seen = set()
    result = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

# Q9 Find the Missing Number in a Sequence
def find_missing_number(nums, n):
    return n * (n + 1) // 2 - sum(nums)

# Q10 Find a Pair with a Given Sum in an Array
def find_pair_with_sum(nums, target):
    seen = set()
    for x in nums:
        need = target - x
        if need in seen:
            return [need, x]
        seen.add(x)
    return []

# Q11 Find the Number Closest to Zero in an Array
def closest_to_zero(nums):
    return min(nums, key=lambda x: (abs(x), -x))

# Q12 Find Common Elements in Two Arrays    
def common_elements(list1, list2):
    set2 = set(list2)
    result = []
    for x in list1:
        if x in set2 and x not in result:
            result.append(x)
    return result

# Q13 Rotate an Array to the Right by k Steps
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]

# Q14 Find the Maximum Sum of Consecutive Elements in an Array
def max_consecutive_sum(nums):
    best = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        best = max(best, nums[i] + nums[i + 1])
    return best

# Q15 Find All Pairs with a Given Sum in an Array
def find_all_pairs(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(p) for p in sorted(pairs)]


