# counter.py
#
# ICS 32A Fall 2019
# Code Example
#
# This module defines a class called Counter, which is a kind of object
# called a "counter", whose goal is to count how many times its "count"
# method has been called.  Each time you call "count", it increments
# its count and returns it, so each time you call "count", you'll receive
# a value one greater than the value you received the previous time.  It
# is also possible to reset the counter and to "peek" at its count (i.e.,
# see the value without changing it).
#
# Counter objects have one private attribute, _count, which specifies
# how many times its count() method has been called.
#
# If you run this module in IDLE, you would be able to do this in the
# interpreter:
#
#     >>> c1 = Counter()
#     >>> c1.count()
#     1
#     >>> c1.count()
#     2
#     >>> c1.count()
#     3
#     >>> c1.peek()
#     3
#     >>> c2 = Counter()
#     >>> c2.count()
#     1
#     >>> c1.count()
#     4
#     >>> c1.peek()
#     4
#     >>> c1.reset()
#     >>> c1.peek()
#     0
#     >>> c1.count()
#     1
#     >>> c2.count()
#     2


class Counter:
    def __init__(self):
        '''Initializes a Counter with a count of zero'''
        self.reset()


    def count(self) -> int:
        '''Increments and returns the count'''
        self._count += 1
        return self._count


    def peek(self) -> int:
        '''Returns the count without updating it'''
        return self._count


    def reset(self) -> None:
        '''Resets the counter, so that its value is zero'''
        self._count = 0


# So why do we care about being able to do this?  In a sense, it seems like
# a Counter can't do anything that an integer can't also do.  You can
# initialize an integer to 0; you can increment it; you can look at its
# value without changing it; and you can reset it back to 0 again.  So why
# bother with writing a class?
#
# The reason isn't because Counters can do things that integers can't.
# It's actually the opposite: Integers can do a lot of things that
# Counters can't.  You can multiply an integer by 9.  You can set it
# to -5.  You can divide it by 3 and get back a float.  But none of
# those things would be desirable if we want one of our counters, the
# goal of which is to provide *only* the abilities we have here and
# nothing else.
#
# So, in this case, we've built an abstraction around a Counter not because
# it provides new behavior that integers don't have, but because it *limits*
# the behavior to only what we want.  That eliminates whole categories of
# mistakes we might make, which is a really important part of designing
# high-quality software.  You *will* make mistakes writing programs.  But
# if you go out of your way to make it harder (or even impossible) to make
# certain kinds of mistakes, your programs will certainly be better for it.
#
# Of course, this also seems unpalatable at first, because classes are new
# territory and you still may not have your mind around them.  But how long
# do you think it would take for someone who already knows how to write
# classes in Python to write this one?  Weighing that against the time saved
# not hunting for mistakes that now can't be made, that investment will
# likely pay off very nicely going forward.
