# Day 19: Code Implementation
# Practical Algorithms: Hash Maps, Frequency Counting & Two Pointers
# Write your implementations here independently.


def two_sum(numbers:list[int],target:int)-> tuple[int,int] | None:
    seen = {}
    for index, num  in enumerate(numbers):
        complement = target - num 
        if complement  in seen:
            return (seen[complement],index)
        seen[num] = index

def most_frequent_word(text:str) -> tuple[str,int]:
    counts = {}
    words = text.lower().split()
    for word in words:
        if word in counts:
            counts[word] +=1
        else:
          counts[word] = 1
    best_word = ""
    max_count = 0

    for word,count in counts.items():
        if count > max_count:
            max_count = count
            best_word = word
    return (best_word,max_count)


def is_palidrome_two_pointer(text:str) -> bool:
    clean = "".join(c.lower() for c in text if c.isalnum())
    left = 0
    right = len(clean) - 1

    while left < right:
        if clean[left] != clean[right]:
            return False
        left += 1   # Move inward from left
        right -= 1  # Move inward from right

    return True