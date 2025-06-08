#Reorder Data in Log Files - 1337c0de #937

#Ordering

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        result = []
         # go through every log, sort into letterLogs and digitLogs
        for log in logs:
        #letter logs end in a letter

        #digit logs end in a digit
            if log[-1].isdigit():\
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        #letter logs come before all digit logs
        #letters logs are sorted lexicographically

        #maintains relative ordering so 8 1 5 1 comes before 3 6 in the digit logs because of it's spot in the array

        letter_logs.sort(key= lambda x:(x.split()[1:], x.split()[0]))
        
        result = letter_logs + digit_logs
        return result
    
# Example usage
if __name__ == "__main__":
    logs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"
    ]
    
    solution = Solution()  # Create an instance of the Solution class
    reordered_logs = solution.reorderLogFiles(logs)  # Call the method with the logs
    print(reordered_logs)  # Print the result






