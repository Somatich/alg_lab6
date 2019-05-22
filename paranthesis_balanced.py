#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stack import Stack, StackOverflowError, StackIsEmptyError
s = '({[()]}{<>})'
def is_paranthesis_balanced(s):
    a = list(s)
    parat = Stack(len(a))
    for i in a:
        print(i)
        try:
            if i == '(':
                parat.push('(')
            elif i == ')':
                if parat.pop() != '(':
                    print('круглые скобочки не закрыты')
                    return False
            elif i == '[':
                parat.push('[')
            elif i == ']':
                if parat.pop() != '[':
                    print('квадратные скобочки не закрыты')
                    return False
            elif i == '{':
                parat.push('{')
            elif i == '}':
                if parat.pop() != '{':
                    print('фигурные скобочки не закрыты')
                    return False
            elif i == '<':
                parat.push('<')
            elif i == '>':
                if parat.pop() != '<':
                    print('треугольные скобочки не закрыты')
                    return False
        except StackOverflowError:
            print('лишняя закрывающая скобочка DETECTED')
            return False
        except StackIsEmptyError:
            print('лишняя открывающая скобочка DETECTED')
            return False
    if parat.__len__() == 0:
        print('выражение кайфовое')
        return True
    else:
        return False
print(is_paranthesis_balanced(s))

#is_paranthesis_balanced(s = '({[()]}{<>})')