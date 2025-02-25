# polling_ui.py
#
# ICS 32A Fall 2019
# Code Example
#
# This module implements a simple, text-based Polling client, which allows
# the user to interact with our Polling service without being aware of all of
# the underlying details.  It's sort of akin to a smartphone application that
# interacts with Twitter; the user doesn't have to know how Twitter works
# underneath, and yet they can still read and post tweets, and so on.
#
# In Python, our modules are on a level field with the ones in the Python
# Standard Library.  When we've written things in one module and want to use
# them in one of our other modules, we use "import" the same way and we call
# the functions the same way (i.e., by qualifying them with the name of the
# module and a dot).  The only tricky part is setting them up so that
# Python can find them, the simplest solution to which is to put all of
# the modules comprising a program into the same directory.  Note, too,
# that the file is called "polling.py", but we refer to it in a Python
# program as just "polling; this turns out to be important.

import polling



# There are better solutions than embedding these kinds of details in the
# code of a program, but this will do for now.  You will need to change
# this string so that it indicates the machine where the Polling server
# is running.

POLLING_HOST = 'localhost'
POLLING_PORT = 5501



# Note how this function reads a lot like English, since most of what it
# does is to call other functions that have clear names.  This is a
# technique you'll want to use in your programs.

def _run_user_interface() -> None:
    '''
    Runs the console-mode user interface from start to finish.
    '''
    _show_welcome_banner()
    connection = polling.connect(POLLING_HOST, POLLING_PORT)

    try:
        while True:
            username = _ask_for_username()

            response = polling.hello(connection, username)

            if response == polling.NO_USER:
                print('That user does not exist')
            else:
                break

        # Notice how _handle_command returns False only when there are
        # no more commands to be processed.  That gives us the ability
        # to get out of this loop.
        while _handle_command(connection):
            pass

    finally:
        # No matter what, let's make sure we close the Polling connection
        # when we're done with it.
        polling.close(connection)



def _handle_command(connection: polling.PollingConnection) -> bool:
    '''
    Handles a single command from the user, by asking the user what command
    they'd like to execute and then handling it.  Returns True if additional
    commands should be processed after this one, False otherwise.
    '''
    command = input('[V]ote, [R]esults, or [G]oodbye? ').strip().upper()

    if command == 'V':
        _handle_vote_command(connection)
        return True
    elif command == 'R':
        _handle_results_command(connection)
        return True
    elif command == 'G':
        _handle_goodbye_command(connection)
        return False
    else:
        print('Invalid command; try again')
        return True



def _handle_vote_command(connection: polling.PollingConnection) -> None:
    '''
    Allows the user to choose a question, then vote on the one they chose.
    '''

    questions = polling.questions(connection)

    print()
    print('Choose a question to vote on')
    print()
    
    _show_questions(questions)

    print()
    question_id = input('What question would you like to vote on? ').strip()

    for question in questions:
        if question.question_id == question_id:
            choices = polling.choices(connection, question_id)
            _show_choices(choices)

            print()
            choice_id = input('What is your choice? ').strip()

            result = polling.vote(connection, question_id, choice_id)

            if result == polling.VOTED:
                print('Your vote has been noted')
            elif result == polling.ALREADY_VOTED:
                print('You have already voted on this question')
            elif result == polling.NO_QUESTION:
                print('That is not a valid question')
            elif result == polling.NO_CHOICE:
                print('That is not a valid choice')
            
            break

    else:
        print()
        print('That is not one of the questions available')



def _handle_results_command(connection: polling.PollingConnection) -> None:
    '''
    Allows the user to choose a question, then shows its results.
    '''

    questions = polling.questions(connection)

    print()
    print('Choose a question for which to see results')
    print()
    
    _show_questions(questions)

    print()
    question_id = input('For what question would you like to see results? ').strip()

    for question in questions:
        if question.question_id == question_id:
            results = polling.results(connection, question_id)
            _show_results(results)
            break
    else:
        print()
        print('That is not one of the questions available')


def _handle_goodbye_command(connection: polling.PollingConnection) -> None:
    '''
    Handles a Goodbye command by exchanging GOODBYE messages with the server.
    '''
    print('Goodbye!')
    polling.goodbye(connection)



def _show_welcome_banner() -> None:
    '''
    Shows the welcome banner
    '''
    print('Welcome to the Polling client!')
    print()
    print('Please login with your username.')
    print()


def _ask_for_username() -> str:
    '''
    Asks the user to enter a username and returns it as a string.  Continues
    asking repeatedly until the user enters a username that is non-empty, as
    the Polling server requires.
    '''
    while True:
        username = input('Username: ').strip()

        if len(username) > 0:
            return username
        else:
            print('That username is blank; please try again')



def _show_questions(questions: [polling.PollingQuestion]) -> None:
    '''
    Shows all of the questions in the given list.
    '''

    print('QUESTIONS')
    
    for question in questions:
        print('{}: {}'.format(question.question_id, question.question_text))

    print()



def _show_choices(choices: [polling.PollingChoice]) -> None:
    '''
    Shows all of the choices in the given list.
    '''

    print('CHOICES')

    for choice in choices:
        print('{}: {}'.format(choice.choice_id, choice.choice_text))

    print()



def _show_results(results: [polling.PollingResult]) -> None:
    '''
    Shows all of the results in the given list.
    '''

    print('RESULTS')

    total_votes = _count_total_votes(results)

    for result in results:
        id = result.choice_id
        percentage = round(result.vote_count / total_votes * 100, 1)
        text = result.choice_text
        print('{} ({}%): {}'.format(id, percentage, text))

    print()



def _count_total_votes(results: [polling.PollingResult]) -> int:
    '''
    Counts the total number of votes in a list of results
    '''

    total_votes = 0

    for result in results:
        total_votes += result.vote_count

    return total_votes



if __name__ == '__main__':
    _run_user_interface()
