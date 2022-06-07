#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is not 0:
        return (len(sentence), sentence[0])
    else:
        return (len(sentence), None)
