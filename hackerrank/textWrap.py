# https://www.hackerrank.com/challenges/text-wrap/problem
# https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/
import textwrap


def wrap(inputString, maxWidth):
    wrappedString = ''
    wrapper = textwrap.TextWrapper(width=maxWidth)
    wordList = wrapper.wrap(text=inputString)
    for word in wordList:
        wrappedString += word + '\n'
    return wrappedString


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
