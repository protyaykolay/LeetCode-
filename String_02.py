# Check If Sentence Is Pangram
# LeetCode 1832

class Solution(object):
    def checkIfPangram(self, sentence):
        seen = [False] * 26
        count = 0

        for char in sentence:
            index = ord(char) - ord('a')

            if not seen[index]:
                seen[index] = True
                count += 1

                if count == 26:
                    return True

        return count == 26


# Example
sentence = "thequickbrownfoxjumpsoverthelazydog"

solution = Solution()
result = solution.checkIfPangram(sentence)

print("Is the sentence a pangram?", result)