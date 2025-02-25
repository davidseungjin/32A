# polling.py
#
# ICS 32A Fall 2019
# Code Example
#
# This module provides a set of functions that implement the Polling protocol
# using sockets, allowing a Python program to connect to a Polling server and
# use it to send and view questions, view questions, vote on them, and so on,
# while insulating the program from the underlying details of how the
# protocol is implemented.
#
# It's important to note that the module contains no user interface and is
# not a "program" that can be executed.  Instead, it provides utility
# functions that can used by programs, in the same way that modules like
# "os" and "socket" do in the Python Standard Library.  It's fair to say,
# actually, that this module is a small library.  (See?  We can build our
# own libraries, too!)

from collections import namedtuple
import socket


# From our work with sockets in previous examples, we discovered that we
# needed to know three things about a connection at any given time:
#
# (1) The socket across which the connection is traveling
# (2) A pseudo-file object that lets us read input from that socket as
#     though we were reading from a text file
# (3) A pseudo-file object that lets us write input to that socket as
#     though we were writing to a text file
#
# Because these three things need to be available to various functions
# in our module, it's handy to create a kind of object to store all three,
# so we only have one thing to store, one thing to return, and one thing
# to pass as a parameter.  A namedtuple is a convenient way to do that.

PollingConnection = namedtuple(
    'PollingConnection',
    ['socket', 'input', 'output'])



# When we ask the Polling server for a list of questions that are available
# to vote on, there are a couple of things we want to know about each one.
# A handy way to keep all of that together is to use a namedtuple.  Similarly,
# we'll do the same with choices and results.

PollingQuestion = namedtuple(
    'PollingQuestion',
    ['question_id', 'question_text'])

PollingChoice = namedtuple(
    'PollingChoice',
    ['choice_id', 'choice_text'])

PollingResult = namedtuple(
    'PollingResult',
    ['choice_id', 'vote_count', 'choice_text'])



# These constants represent results that can be returned from some of
# the functions below.  When functions can return one or more of these
# values, they're described in the function's type annotation.

HELLO = 0
VOTED = 1
ALREADY_VOTED = 2
NO_QUESTION = 3
NO_CHOICE = 4
NO_USER = 5



# This is the simplest example of how you create new kinds of exceptions
# that are specific to your own program.  A class introduces a new type of
# object into your program.  In this case, we're introducing a new type called
# PollingProtocolError, and specifying that we want it to be a kind of
# exception (i.e., something that we can raise to indicate failure).  We'll
# talk a lot more about classes a little later in the course.

class PollingProtocolError(Exception):
    pass



# Set this to True if you want to see a trace of what gets sent to the server
# and what gets received back from it.  Before a program is "finished,"
# you'd want to set this back to False, but providing this ability makes
# it easy to see the underlying interactions between client and server
# -- which are otherwise invisible -- when you need to troubleshoot a
# problem.

_SHOW_DEBUG_TRACE = False



def connect(host: str, port: int) -> PollingConnection:
    '''
    Connects to a Polling server running on the given host and listening
    on the given port, returning a PollingConnection object describing
    that connection if successful, or raising an exception if the attempt
    to connect fails.
    '''

    polling_socket = socket.socket()
    
    polling_socket.connect((host, port))

    polling_input = polling_socket.makefile('r')
    polling_output = polling_socket.makefile('w')

    return PollingConnection(
        socket = polling_socket,
        input = polling_input,
        output = polling_output)



def hello(connection: PollingConnection, username: str) -> HELLO or NO_USER:
    '''
    Logs a user into the Polling service over a previously-made connection.
    If the attempt to send text to the Polling server or receive a response
    fails (or if the server sends back a response that does not conform to
    the Polling protocol), an exception is raised.
    '''

    # The _write_line and _expect_line functions are written below.  Their
    # goal is to hide the details of interacting with the socket (e.g.,
    # putting the correct newline sequence on the end of the line, remembering
    # to flush the output after writing it, etc.).  Notice how, given those
    # tools, the code we've written here is terse and clear, relative to
    # what it would look like if we had these details interspersed throughout
    # this function.
    _write_line(connection, 'POLLING_HELLO ' + username)

    response = _read_line(connection)

    if response == 'HELLO':
        return HELLO
    elif response.startswith('NO_USER '):
        return NO_USER
    else:
        raise PollingProtocolError()



def questions(connection: PollingConnection) -> [PollingQuestion]:
    '''
    Asks the Polling server for a list of the currently-available
    questions.  Returns a list of PollingQuestion objects to describe
    them.
    '''

    _write_line(connection, 'POLLING_QUESTIONS')

    count_words = _read_line(connection).split()

    if len(count_words) != 2 or count_words[0] != 'QUESTION_COUNT':
        raise PollingProtocolError()

    try:
        question_count = int(count_words[1])
    except ValueError:
        raise PollingProtocolError()

    questions = []

    for i in range(question_count):
        question_line = _read_line(connection)
        question_words = question_line.split()

        if len(question_words) < 3 or question_words[0] != 'QUESTION':
            raise PollingProtocolError()

        question_id = question_words[1]
        question_text = question_line[(10 + len(question_id)):]

        questions.append(PollingQuestion(question_id, question_text))

    return questions



def choices(connection: PollingConnection, question_id: str) \
        -> [PollingChoice] or NO_QUESTION:
    '''
    Asks the Polling server for a list of choices associated with a
    question.  Returns a list of PollingChoice objects that describes
    them.  If the question does not exist, returns NO_QUESTION instead.
    '''

    _write_line(connection, 'POLLING_CHOICES ' + question_id)

    count_words = _read_line(connection).split()

    if len(count_words) > 0 and count_words[0] == 'NO_QUESTION':
        return NO_QUESTION
    elif len(count_words) != 2 or count_words[0] != 'CHOICE_COUNT':
        raise PollingProtocolError()

    try:
        choice_count = int(count_words[1])
    except ValueError:
        raise PollingProtocolError()

    choices = []

    for i in range(choice_count):
        choice_line = _read_line(connection)
        choice_words = choice_line.split()

        if choice_words[0] != 'CHOICE' or len(choice_words) < 3:
            raise PollingProtocolError()

        choice_id = choice_words[1]
        choice_text = choice_line[(8 + len(choice_id)):]

        choices.append(PollingChoice(choice_id, choice_text))

    return choices



def vote(connection: PollingConnection, question_id: str, choice_id: str) \
        -> VOTED or ALREADY_VOTED or NO_QUESTION or NO_CHOICE:
    '''
    Votes on a question via the Polling server.  Returns one of four
    values: VOTED, ALREADY_VOTED, NO_QUESTION, or NO_CHOICE.
    '''

    _write_line(connection, 'POLLING_VOTE {} {}'.format(question_id, choice_id))

    response = _read_line(connection)

    if response == 'VOTED':
        return VOTED
    elif response == 'ALREADY_VOTED':
        return ALREADY_VOTED
    elif response.startswith('NO_QUESTION '):
        return NO_QUESTION
    elif response.startswith('NO_CHOICE '):
        return NO_CHOICE
    else:
        raise PollingProtocolError()



def results(connection: PollingConnection, question_id: str) \
        -> [PollingResult] or NO_QUESTION:
    '''
    Asks the Polling server for a list of results associated with a
    question.  Returns a list of PollingResult objects that describes
    them.  If the question does not exist, returns NO_QUESTION instead.
    '''

    _write_line(connection, 'POLLING_RESULTS {}'.format(question_id))

    count_words = _read_line(connection).split()

    if len(count_words) > 0 and count_words[0] == 'NO_QUESTION':
        return NO_QUESTION
    elif count_words[0] != 'RESULT_COUNT' or len(count_words) != 2:
        raise PollingProtocolError()

    try:
        result_count = int(count_words[1])
    except ValueError:
        raise PollingProtocolError()

    results = []

    for i in range(result_count):
        result_line = _read_line(connection)
        result_words = result_line.split()

        if result_words[0] != 'RESULT' or len(result_words) < 3:
            raise PollingProtocolError()

        result_id = result_words[1]

        try:
            vote_count = int(result_words[2])
        except ValueError:
            raise PollingProtocolError()
        
        result_text = result_line[(10 + len(result_id)):]

        results.append(PollingResult(result_id, vote_count, result_text))

    return results
    


def goodbye(connection: PollingConnection) -> None:
    'Exchanges goodbye messages with the server'

    _write_line(connection, 'POLLING_GOODBYE')
    _expect_line(connection, 'GOODBYE')



def close(connection: PollingConnection) -> None:
    'Closes the connection to the Polling server'

    # To close the connection, we'll need to close the two pseudo-file
    # objects and the socket object.
    connection.input.close()
    connection.output.close()
    connection.socket.close()




# These are "private functions", by which I mean these are functions
# that are only intended to be used within this module.  They're
# hidden implementation details, used only to make writing other functions
# in this module easier.  By starting their names with an underscore,
# we're making clear to users of this module that these functions are
# intended to be private -- this convention is typical in Python programs,
# so if we name things beginning with underscores, it's a strong hint to
# knowledgeable Python programmers that our intent is for these things
# only to be used where they're defined (in this case, only within the
# polling.py module).



def _read_line(connection: PollingConnection) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''

    # The [:-1] uses the slice notation to remove the last character
    # from the string.  Since we know that readline() will always
    # return a line of text with a '\n' character on the end of it,
    # the slicing here will ensure that these will always be stripped
    # out, so we'll never have to deal with this detail elsewhere.
    line = connection.input.readline()[:-1]

    if _SHOW_DEBUG_TRACE:
        print('RCVD: ' + line)

    return line



def _expect_line(connection: PollingConnection, expected: str) -> None:
    '''
    Reads a line of text sent from the server, expecting it to contain
    a particular text.  If the line of text received is different, this
    function raises an exception; otherwise, the function has no effect.
    '''

    line = _read_line(connection)

    if line != expected:
        raise PollingProtocolError()



def _write_line(connection: PollingConnection, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence, and ensures that it is sent immediately.
    '''
    connection.output.write(line + '\r\n')
    connection.output.flush()

    if _SHOW_DEBUG_TRACE:
        print('SENT: ' + line)
