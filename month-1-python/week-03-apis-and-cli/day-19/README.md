# Day 19: Practical Algorithms in Python (Hash Maps, Two Pointers & Frequency Counting)

## Learning Objectives
1. Algorithmic thinking without heavy math: turning $O(N^2)$ brute-force solutions into $O(N)$ linear time.
2. The Hash Map pattern (`dict` and `collections.Counter`): frequency counting, instant lookup.
3. The Two-Pointer technique: opposite ends (`left`, `right`) on sorted lists.
4. Analyzing Time Complexity ($O$) and Space Complexity ($O$) of your code.
5. Why these patterns matter for AI: token frequency counting, embedding similarity candidates, and fast data deduplication.

---

## Daily Task: Practical Algorithm Challenges (Without AI)
In `algorithms.py`, implement 3 practical algorithmic functions:
1. `two_sum(numbers: list[int], target: int) -> tuple[int, int] | None`:
   - Find the two indices that add up to `target`.
   - Must run in **$O(N)$ time** using a dictionary/hash map (do NOT use nested loops $O(N^2)$!).
2. `most_frequent_word(text: str) -> tuple[str, int]`:
   - Tokenizes a text string into words (lowercased, punctuation removed).
   - Counts frequencies using a dictionary or `Counter`.
   - Returns the most frequent word and its occurrence count.
3. `is_palindrome_two_pointer(s: str) -> bool`:
   - Strips non-alphanumeric characters and checks if the string is a palindrome using **two pointers (`left = 0`, `right = len - 1`)** without reversing the entire string in memory.

---

## Developer English Task: Algorithm Walkthrough (C1)
Explain in 3-4 professional C1 sentences how your hash map `two_sum` algorithm achieves $O(N)$ linear time complexity compared to the $O(N^2)$ nested loop approach.

---

## Mandarin Chinese Task: Lesson 2 (Numbers & Work Time)
Learn numbers 1-10 and how to say hours/time for your work shift:
- `一, 二, 三, 四, 五, 六, 七, 八, 九, 十` (1 to 10)
- `点` (*diǎn* = o'clock)
- Sentence: "I work at 7 o'clock" (`我七点上班`)
