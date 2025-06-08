#1337c0de #1268 - Search Suggestions System

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #sort the products
        products.sort()

        # ar array to store result in
        #initialize l to 0 and r to the producst array length - 1

        result = []
        l, r = 0, len(products) - 1

        #loop over characters in serach word

        for i in range(len(searchWord)):
            #assign search_word_letter to the current character in search Word
            search_word_letter = searchWord[i]

            # while left is less than right and the *length of the current product word is less than the position of
            # the search letter (we know it cant be a suggestion because the letter's index wouldnt be in the word)
            # or if the products current letter doesnt equal the serach words current letter

            while l <= r and (len(products[l]) <= i or products[l][i] != search_word_letter):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != search_word_letter):
                r -= 1
            #by moving the pointer positions it essentially removes the product from the list

            #checks words_left which can actually be considered
            #if that number is greater than or equal to three, append leftmost three words
            words_left = r - l + 1
            if words_left >= 3:
                result.append([products[l], products[l + 1], products[l + 2] ])
            elif words_left == 2:
                result.append([products[l], products[l + 1]])
            elif words_left == 1:
                result.append([products[l]])
            else:
                result.append([])
        return result
