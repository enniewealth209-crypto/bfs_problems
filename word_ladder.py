# Import deque from collections to use it for BFS
from collections import deque

# Function to find the length of the shortest transformation sequence from beginWord to endWord
def ladderLength(beginWord, endWord, wordList):
    # Create a set of words for O(1) lookups
    wordSet = set(wordList)
    
    # If endWord is not in the wordList, return 0 as it's impossible to transform
    if endWord not in wordList:
        return 0
    
    # Initialize a queue for BFS with the starting word and initial step count
    queue = deque([(beginWord, 1)])
    
    # Perform BFS until the queue is empty
    while queue:
        word, steps = queue.popleft()
        
        # Check if the current word is the target word
        if word == endWord:
            return steps
        
        # Generate all possible transformations of the current word by changing one letter at a time
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                newWord = word[:i] + c + word[i+1:]
                
                # If the new word is in the wordSet, add it to the queue and remove it from the set to avoid cycles
                if newWord in wordSet:
                    queue.append((newWord, steps + 1))
                    wordSet.remove(newWord)
    
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))