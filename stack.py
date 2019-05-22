#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.storage = [0] * size
        self.head = -1
        self.size = size

    def push(self, v):
        if self.head < self.size-1:
            self.storage[self.head + 1] = v
            self.head += 1
            return
        else:
            raise StackOverflowError
        
    def pop(self):
        if self.head > -1:
            b0x = self.storage[self.head]
            self.storage[self.head] = 0
            self.head -= 1
            return b0x
        else:
            raise StackIsEmptyError

    def __len__(self):
        return self.head + 1

#
#s = [1,2,3,4,5,6,7]
#i = Stack(1000)
#for l in s:
#    i.push(l)
#    print(i.pop())
