# https://www.geeksforgeeks.org/problems/arrange-consonants-and-vowels/1

# Given a singly linked list having n nodes containing english alphabets ('a'-'z'). 
# # Rearrange the linked list in such a way that all the vowels come before the consonants while maintaining the order of their arrival.
# Input:
# n = 9
# linked list: a -> b -> c -> d -> e -> f -> g -> h -> i 
# Output: 
# a -> e -> i -> b -> c -> d -> f -> g -> h
# Explanation: 
# After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.


#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        if head is None or head.next is None:
            return head
        tmp = head
        lastVowel = None
        lastConso = None
        firstConso = None
        firstVowel = None
        vowels = {'a','e','i','o','u'};
        while tmp:
            if tmp.data in vowels:
                if firstVowel is None:
                    firstVowel = tmp
                    lastVowel = firstVowel
                else:
                    lastVowel.next = tmp
                    lastVowel = tmp

            else:
                if firstConso is None:
                    firstConso = tmp
                    lastConso = firstConso
                else:
                    lastConso.next = tmp
                    lastConso = tmp
            
            tmp=tmp.next
        lastConso.next = None
        if firstVowel:
            lastVowel.next=firstConso
        else:
            firstVowel = firstConso
        return firstVowel
