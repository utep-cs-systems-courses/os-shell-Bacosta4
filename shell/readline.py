#! /usr/bin/env python3

from os import read

next = 0
limit = 0

def getChar():
    global next
    global limit

    if next == limit:
        next = 0
        limit = read(0,1000)

        if limit == 0:
            return "EOF"

        if next < len(limit) -1:
            c = chr(limit[next])
            next += 1
            return c
        else:
            return "EOF"

def readLine():
    global next
    global limit

    line = " "
    c = gChar()
    while (c != '' and c != "EOF"):
        line += c
        c = gChar()
        next = 0
        limit = 0

        return line
