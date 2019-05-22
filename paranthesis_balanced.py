#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stack import Stack, StackOverflowError, StackIsEmptyError
s = '({[()]}{<>})'
def is_paranthesis_balanced(s):
    paradic = {'{':'}', '[':']', '(':')','<':'>',}
    a = list(s)
    if len(a) == 0:
        return True
    parat = list()
    for i in a:
        print('para',i)
        print(parat)
        if i in paradic.keys():
            parat.append(i)
        elif len(parat)>0 and i == paradic[parat[-1]]:
            parat.pop()
        else:
            return False
    if len(parat) == 0:
        print('выражение кайфовое')
        return True
    else:
        return False
print(is_paranthesis_balanced(s))

#is_paranthesis_balanced(s = '({[()]}{<>})')