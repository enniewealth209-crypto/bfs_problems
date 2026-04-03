from collections import defaultdict, deque
from os import path

def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    # Step 1: BFS
    parents = defaultdict(list)
    level = {beginWord}
    found = False

    while level and not found:
        next_level = defaultdict(list)

        for word in level:
            wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in wordSet:
                            next_level[new_word].append(word)

                            if new_word == endWord:
                                found = True

            level = next_level

            for word in next_level:
                parents[word].extend(next_level[word])

        # Step 2: Backtracking
        res = []

        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return

            for p in parents[word]:
                backtrack(p, path + [p])

        if found:
            backtrack(endWord, [endWord])

        return res
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord, endWord, wordList))