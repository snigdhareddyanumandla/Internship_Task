from solutions import (
    word_frequency, char_frequency, first_non_repeating_char, are_anagrams,
    first_repeating_char, move_zeros_to_end, second_highest, remove_duplicates,
    find_missing_number, find_pair_with_sum, closest_to_zero, common_elements,
    rotate_right, max_consecutive_sum, find_all_pairs,
)

print("Q1:", word_frequency("python is easy and python is powerful"))
print("Q1 extra:", word_frequency("to be or not to be"))

print("Q2:", char_frequency("banana"))
print("Q2 extra:", char_frequency("hello"))

print("Q3:", first_non_repeating_char("swiss"))
print("Q3 extra:", first_non_repeating_char("aabb"))

print("Q4:", are_anagrams("listen", "silent"))
print("Q4 extra:", are_anagrams("hello", "world"))

print("Q5:", first_repeating_char("programming"))
print("Q5 extra:", first_repeating_char("abc"))

print("Q6:", move_zeros_to_end([0, 3, 0, 1, 2, 0, 4]))
print("Q6 extra:", move_zeros_to_end([0, 0, 5]))

print("Q7:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 extra:", second_highest([5, 5, 5]))

print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 extra:", remove_duplicates([1, 1, 1]))

print("Q9:", find_missing_number([1, 2, 4, 5, 6], 6))
print("Q9 extra:", find_missing_number([2, 3, 4, 5], 5))

print("Q10:", find_pair_with_sum([2, 7, 11, 15], 9))
print("Q10 extra:", find_pair_with_sum([1, 2, 3], 10))

print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 extra:", closest_to_zero([-4, 4, 7]))

print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 extra:", common_elements([1, 1, 2], [1, 3]))

print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 extra:", rotate_right([1, 2, 3], 5))

print("Q14:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 extra:", max_consecutive_sum([-5, -1, -3]))

print("Q15:", find_all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 extra:", find_all_pairs([3, 3, 3], 6))

