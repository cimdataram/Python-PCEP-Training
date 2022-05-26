def _com():
    print(
    '''
    Commands *
    
    While doing your session you can always type the following commands:
        _com = show all commands
        _info =  show programm infos
        _menu = jump to main menu
        _end = leave the programm
        
    * Don't forget to type an underscore before the statement of the command as trigger
        
    '''             
    )
    
    resume = 'Press enter to resume ...'
    input(resume) 


def info_():
    print(
    '''
    INFO ABOUT THIS LEARNING SOFTWARE

    You can choose if you want to learn a certain (sub)module or all questions
    You can choose if you want the questions to be asked module-sorted or randomly
    '''
    )
    
    input('Press enter to read more ...')
    print(
    '''
    After each question you will be asked if was it easy"
    If you answer 'yes' the questions will be deleted from the session file.
    If you answer 'no' this question will remain in your session file.
    
    And all questions from the catalogue will be asked when you start learning
    The first time you want to start learning you will be asked to create a session file
    '''
    )
    
    input('Press enter to read more ...')
    print(
    '''

    After starting your first session you can load this session anytime
    Then you will only be asked the remaining questions from the session file

    You can of course create and start a new session anytime
    When you start a new session all questions will be available again

    All of your sessions are saved and you can open them anytime
    You can also delete sessions manually
    '''
    )
    
    input('Press enter to read more ...')
    print(
    '''
    When you finished a (sub)module you can see it in the navigation.
    It is recommended to complete at least 2 sessions with all questions.
    One sorted and one random.
    Those questions you find difficult shall be object for frequent repetition during the sessions by not deleting them
    '''
    )

    input('Press enter to read commands ...')
    _com()
    
    
    
    

    
