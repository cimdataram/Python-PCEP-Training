import os
import sys
import info #own module
import random

# predefine current session
current_session = ''
# DEFINE SESSION PATH AND DIR ####################################
# get name of current path and folder
current_path = os.path.dirname(os.path.abspath(__file__))
# get absolute path of session folder
session_path = current_path+'\sessions'
# get relative path of session folder
path = 'sessions\\'
# get content of session folder
session_dir = os.listdir(session_path)
# Create list of all session files from folder
sessions = []
for file in session_dir: # loop through dir content
    #if file.find('session_') != -1: # only show session files
    sessions.append(file) # throw file into list


# CREATE NEW SESSION FILE #####################################
def _new_session():
    if len(sessions) >= 99:
        print('Maximum session files reached. Please delete a session before creating a new one')
        input('Please press enter to resume ...')
        os.system('cls')
    else:
        global current_session
        # predefine triggers
        overwrite = ''
        err_cnt = 1
        file_name = ''
        file_cnt = 1
        # loop as long as filename invalid and user has not confirmed to overwrite file
        while err_cnt > 0 or file_cnt > 0:
            msg_filename = 'Please type a name for the session ...\n(only letters, numbers, underscore(_), and dash(-) allowed)...'
            msg_file_error = ''
            print(msg_filename)
            file_name = input()
            err_cnt = 0
            # empty filenames not allowed
            if file_name == '':
                err_cnt = 1
            for char in file_name: # loop each char of time string
                # only letters, numbers, underscores and dashes allowed
                if char.isalpha() == False and char.isnumeric() == False and char != '_' and char != '-':
                    err_cnt += 1
                    print(err_cnt)
            # error alert if filename invalid
            if err_cnt > 0:
                os.system('cls')
                print('Error: Please only used allowed chars.')
            else:
                file_cnt = 0
                file_text = file_name+'.py'
                # check if filename already exists in dir
                if file_text in sessions:
                    file_cnt += 1
                    os.system('cls')
                    overwrite = ''
                    print('File already exists')
                    # loop as long as user does not confirm to overwrite or not to overwrite
                    while overwrite != 'y' and overwrite != 'n':
                        print('Are you sure you want to overwrite existing session? y/n')
                        overwrite = input()
                        # break inner and outer loop if user confirms tooverwrite file
                    if overwrite == 'y':
                        os.system('cls')
                        file_cnt = 0
                        break
                    # repeat outer loop if user does not confirm to overwrite file
                    elif overwrite == 'n':
                        file_cnt = 1
                        os.system('cls')
                        break
                    # repeat inner loop if user makes invalid input
                    else:
                        os.system('cls')
                os.system('cls')
        
        if overwrite != 'n':
            # concatenate new session file name
            new_session = file_name+'.py'
            # read lines from main question catalogue
            with open('qa.py', "r") as qa:
                lines = qa.readlines()
            #write data from catalogue to new session file
            with open(path+new_session, "w") as new_sess:   
                for line in lines:
                    new_sess.write(line)
                                     
            # define reference for current session
            sessions.append(new_session)
            current_session = path+new_session

            os.system('cls')          
             
        if overwrite == 'y':
            print('Session has successfully been overwritten.')
            if visit == '':
                input('Press enter to continue ...')    
            else:
                input('Press enter to resume ...')
                os.system('cls')
                
        elif overwrite == 'n':
            input('Press enter to resume ...')
            os.system('cls')
        else:
            print('Session has successfully been created.')
            if visit == '':
                input('Press enter to continue ...')    
            else:     
                input('Press enter to resume ...')
                os.system('cls')
            

        return current_session

os.system('cls')
# WELCOME NOTE ######################################################
if sessions == []: # if session dir empty  
    visit = '' # no partial msg on 1st visit
else:
    visit = 'b a c k   ' # partial msg on non-1st visits
print((f'W e l c o m e   {visit}t o   P y t h o n   P C E P   T r a i n i n g   :-)').upper(), end='\n\n')
print('This is an interactive training software will to help you succeed your exam!')
print()
input('Please press enter to continue ...')
os.system('cls')


def _session_fin(s):
    s = 'sessions\\'+s
    unempty_submods = 0
    with open(s, "r") as qa:
        lines = qa.readlines() 
        for line in lines:
            if '], [' in line:
                unempty_submods += 1
            if 'h1'in line.strip(' '):
                unempty_submods += 1
            if '\'], ]' in line:
                unempty_submods += 1                
    return unempty_submods
                        

# PROGRAMM MAIN LOOP
while True:
    # BASIC NAVIGATION ####################
    nav = ''
    def _basnav():
        global current_session
        current_session = ''
        while True:
            print('Please select an option ...')
            print('__________________________________________________________')
            nav_ = ['Show programm information', 'Start learning', 'Create new session', 'Delete a session']
            for c, n in enumerate(nav_):
                print('')
                print(c, n)               
            try:
                nav = int(input())
                if int(nav) >= len(nav_):
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    break             
            except:
                os.system('cls')
                continue            
        nav = int(nav)
        os.system('cls')
        # NAVIGATION BASIC LOOP #########################################
        # SHOW INFO IF SELECTED    
        if nav == 0: 
            nav = ''
            info.info_() # show programm infos
            os.system('cls')
            
        # SECTION: OPEN SESSION AND START LEARNING IF 1 SELECTED
        if nav == 1:
            # If no sesscion existt, user must create a session first
            while sessions == []: # if session dir empty 
                current_session = _new_session()
            os.system('cls')
            # predefine session selection to start loop       
            sel_sess = 999
            while sel_sess >= len(sessions):
                while True:
                    sess_msg = 'Please select a session file you want to open ...'
                    print(sess_msg)
                    print('__________________________________________________________')
                    # list session files and allocate numbers for user selection
                    for n, s in enumerate(sessions):
                        unempty_submods = _session_fin(s)
                        if unempty_submods == 0:
                            print(n, s, end='')
                            print('   => FINISHED')
                        else:
                            print(n, s)
                    try:
                        sel_sess = int(input())
                        break
                    except:
                        os.system('cls')
                        continue
                    if sel_sess >= len(sessions):
                        os.system('cls')   
                    else:
                        break
                
                os.system('cls')                       
            # Define selected session as current session
            current_session = path+sessions[int(sel_sess)]  
            os.system('cls')  
                
        # SECTION: CREATE NEW SESSION IF 2 SELECTED
        elif nav == 2: 
            current_session = _new_session()
         
        elif nav == 3:
        # SECTION: DELETE SESSION IF 3 SELECTED
            if sessions == []:
                print('No session file available yet. Please create a session first.')
                input('Please press enter to resume ...')
                os.system('cls')
            else:
                # predefine session selection to start loop 
                sel_sess = 999
                while sel_sess >= len(sessions):
                    while True:
                        sess_msg = 'Please select a session file you want to delete ...'
                        print(sess_msg)
                        # list session files and allocate numbers for user selection
                        for n, s in enumerate(sessions):
                            unempty_submods = _session_fin(s)
                            if unempty_submods == 0:
                                print(n, s, end='')
                                print('   => FINISHED')
                            else:
                                print(n, s) 
                        try:
                            sel_sess = int(input())
                            break
                        except:
                            os.system('cls')
                            continue
                        if sel_sess >= len(sessions):
                            os.system('cls')   
                        else:
                            break
                    os.system('cls')
                
                delete_session = path+sessions[int(sel_sess)]
                del_conf = ''
                # validity check loop of user input
                while del_conf != 'y' and del_conf != 'n':  
                    #if delete_session == current_session:
                    #    print('The file you want to delete is the current session.\n The programm will restart if you delete it.')
                    print('Are you sure you want to delete the session? y/n')
                    del_conf = input()
                    os.system('cls')
                if del_conf == 'y':
                    # delete session file
                    os.remove(delete_session)
                    # remove deleted session from selectable sessions
                    sessions.pop(sel_sess)
                    print('Session has successfully been deleted.')
                    input('Press enter to resume')  
                    os.system('cls')                
                elif del_conf == 'n':
                    os.system('cls')
                
                
        # Return session path und nav selection from basic navigation loop           
        return current_session, nav
    # as long as 'start learning has not been selected loop basic navigation'
    while nav != 1:
        current_session, nav = _basnav()
            
    # predefine lists of finished modules and submodules     
    fin_mods = []
    fin_mod = []
    fin_sub = []

    # add 'finished' to '0 all modules' if all submodules of all modules are empty
    def _finmods():
        cnt_finmods = 0
        for i in range(1, len(mod)):
            h1_ = 'mod_'+str(i)
            h1 = globals()['mod_'+str(i)] 
            # Loop through hierarchy level 2
            for j in range(1, len(h1)):
                h2_ = 'mod_'+str(i)+'_'+str(j)
                h2 = globals()[h2_]
                if h2 != []:
                    cnt_finmods += 1        
        return cnt_finmods

        
    # add 'finished' if submod is empty
    def _finsub(a_ = '', b_ = ''):
        if a_ == 0:
            print('\n')
        elif b_ != '':
            b_sub = 'mod_'+str(b_)+'_'+str(a_)
            b_sub_ = globals()[b_sub]
            if b_sub_ == []:
                print('   => FINISHED', end=' ')
                return a_
            else:
                print('   => ', len(b_sub_), 'Questions left', '\n')
     
    # add 'finished' if all sobmodules of particular module are empty
    def _finmod(a_):
        if a_ == 0:
            cnt_finmods = _finmods()
            if cnt_finmods == 0:
                print('   => FINISHED', end=' ')
            else:
                print('\n')      
        elif a_ != 0:
            a_cnt = 0
            a_mod = 'mod_'+str(a_)
            a_mod_ = globals()[a_mod]
            for i in range(1, len(a_mod_)):
                a_sub = 'mod_'+str(a_)+'_'+str(i)
                a_sub_ = globals()[a_sub]
                if a_sub_ != []:
                    a_cnt = 1
            if a_cnt == 0:
                print('   => FINISHED', end=' ')
                return a_
            else:
                y_cnt = 0
                for x in a_mod_:
                    _a_sub = 'mod_'+str(a_)+'_'+str(x)
                    _a_sub_ = globals()[_a_sub]
                    for y in _a_sub_:
                        y_cnt += 1
                print('   => ', y_cnt-1, 'Questions left', '\n')
        else:
            print('')

    ### MODULAUFLISTUNG UND PRÜFUNG DER USER AUSWAHL 
    def hier(lst, b = ''):
        cnt_finmods = _finmods()
        if cnt_finmods == 0:
            print('You have fully completed this session. But you can start a new one :-)')
            input('Press enter to resume to main menu ...')
            os.system('cls')
            return 'jump_to_nav'
        else:
            # start input control loop
            status = 'invalid'
            while status == 'invalid':
                if sel_text != '':
                    print('###', sel_text)
                print(msg)
                print('__________________________________________________________')
                while True:
                    # print selection options  
                    for i in lst:
                        if b !='':
                            # print sub // add 'finished' if finished // create list of finished ids
                            print(i, lst[i], end='')
                            fin = _finsub(a_ = i, b_ = b)
                            if fin != None:
                                fin_sub.append(fin)
                                print('\n')
                        else:
                            # print mod // add 'finished' if finished // create list of finished ids
                            print(i, lst[i], end='')
                            fin = _finmod(a_ = i)
                            if fin != None:
                                fin_mod.append(fin)
                                print('\n')
                    # check input for ValueError
                    try:
                        num = int(input())
                        break
                    except ValueError:
                        os.system('cls')
                        if sel_text != '':
                            print('###', sel_text)
                        print(msg)
                        print('__________________________________________________________')

                # has one of the options been picked?            
                if b !='':
                    if int(num) in lst.keys():
                        if int(num) not in fin_sub:
                            status = 'valid'
                        else:
                            os.system('cls')
                            sub_alert = 'Selected sub module already finished!'
                            print(sub_alert, end='\n\n')
                            input('Please press enter to resume ...')
                            os.system('cls')
                    else:
                        os.system('cls')
                else:
                    if int(num) in lst.keys():
                        if int(num) not in fin_mod:
                            status = 'valid'
                        else:
                            os.system('cls')
                            mod_alert = 'Selected module already finished!'
                            print(mod_alert, end='\n\n')
                            input('Please press enter to resume ...')
                            os.system('cls')
                    else:
                        os.system('cls')
                        
            os.system('cls')       
            return num

    # open session
    exec(open(current_session).read())


    def delete_question(question_id):
        # WRITE TO SAME FILE (KEEP READABLE FORMAT) AND OMIT TARGET QUESTION #########
        easy = ''
        del_cnt_ = 0
        # ask user if current question should be deleted (yes easy = deletion)
        while easy != 'y' and easy != 'n':
            easy = input('easy? (y/n)')
        # executute deletion process if user inputs 'y'
        if easy == 'y':
            del_cnt_ = 1
            dele = str(question_id)
            # use write mode to access current session file
            with open(current_session, "w+") as fout:     
                line = 'mod = '+str(mod)+'\n\n'
                fout.write(line)
                # Loop through hierarchy level 1
                for i in range(0, len(mod)):
                    h1_ = 'mod_'+str(i)
                    h1 = globals()['mod_'+str(i)]
                    line = str(h1_)+' = '+str(h1)+'\n'
                    fout.write(line)
                    # Loop through hierarchy level 2
                    for j in range(0, len(h1)):
                        h2_ = 'mod_'+str(i)+'_'+str(j)
                        h2 = globals()[h2_]
                        line = str(h2_)+' = [' #+' = '+str(h2)+'\n'
                        fout.write(line)
                        # Loop through questions
                        for k in range(len(h2)):
                            # omit target question
                            if question_id != h2[k]:
                                line = str(h2[k])+', '
                                fout.write(line)
                        line = ']\n'
                        fout.write(line)
                    line = '\n'
                    fout.write(line)
                              
        else:
            del_cnt_ = 0
               
        return del_cnt_
                            
            
    # CONVERT SESSION FILE TEXT INTO FORMAT THAT CODE CAN SUCCESSFULLY READ #################################
    with open(current_session, "w+") as fout:     
        line = 'mod = '+str(mod)+'\n\n'
        fout.write(line)
        for i in range(0, len(mod)):
            h1_ = 'mod_'+str(i)
            h1 = globals()['mod_'+str(i)]
            line = str(h1_)+' = '+str(h1)+'\n'
            fout.write(line)
            for j in range(0, len(h1)):
                h2_ = 'mod_'+str(i)+'_'+str(j)
                h2 = globals()[h2_]
                line = str(h2_)+' = ['
                fout.write(line)
                for k in range(len(h2)): 
                    line = str(h2[k])+', '
                    fout.write(line)
                line = ']\n'
                fout.write(line)
            line = '\n'
            fout.write(line)  


    # back to menu callable as command
    def _menu():
        conf = ''
        os.system('cls')
        while conf != 'y' and conf != 'n':
            print('Are you sure you want to interrupt your learning unit? y/n')
            print('Don\'t worry, progress has already saved.')
            conf = input()
            os.system('cls')
        if conf == 'y':
            return 'break'
        else:
            return True
        
    # programm end callable as command
    def _end():
        os.system('cls')
        sys.exit()
           
    # programm info callable as command
    def _info():
        os.system('cls')
        info.info_()
        os.system('cls')
        
    # command list callable as command
    def _com():
        os.system('cls')
        info._com()
        os.system('cls')
     
    # Redistribution to particular non-breakable commands
    def _nonbreak_commands(comm):
        comm_ = ['_info', '_com']
        for item in comm_: # loop through commands
            if comm == item:
                item = globals()[item] #dynamic name
                item() # invoke function
                return True
        else:
            return ''
    
    # Redistribution to particular breakable commands
    def _break_commands(comm):
        comm_ = ['_end', '_menu']
        for item in comm_: # loop through commands
            if comm == item:
                item = globals()[item] #dynamic name
                return_val = item() # invoke function
                return return_val
        else:
            return ''
    
    # Basic Command Listener and Distribution to breakable and non breakable distributor
    def _commands(comm):
        nonbreak_ = ['_info', '_com']
        break_ = ['_end', '_menu']
        if comm in nonbreak_:
            _nonbreak_commands(comm)
            return True
        elif comm in break_:
            return_val = _break_commands(comm)
            return return_val
        else:
            return False
        
           
    ### USER AUSWAHL ERSTE HIERARCHIESTUFE
    sel_text = ''
    msg = 'Please select a module you would like to learn (type number): '
    num_ = hier(mod)
    # if session completed, start next iteration of main menu loop
    if num_ == 'jump_to_nav':
        continue
    _mod_ = 'mod_'+str(num_)
    mod_ = globals()[_mod_]
    sel_text = mod[num_].upper()

    ### USER AUSWAHL ZWEITE HIERARCHIESTUFE
    if num_ != 0:
        msg = 'Please select a sub module you want to learn:'
        subnum_ = hier(mod_, b = num_)
        _submod_ = 'mod_'+str(num_)+'_'+str(subnum_)
        submod_ = globals()[_submod_]
        sub_sel_text = mod_[subnum_].upper()
        
    ### USER SELECTION OF LEARNING ORDER
    msg = 'Would like to answer (s)orted or (r)andom questions?'
    while True:
        print(msg)
        # check input for ValueError
        select_order = input()     
        if select_order == 's' or select_order == 'r':
            os.system('cls')
            break
        else:
            continue


    ### SORTED LEARNING 
    if select_order == 's':
        check_comm = ''
        # If all Modules have been chosen loop through all Q&As
        if num_ == 0:
            # Loop through hierarchy level 0 
            for i in range(1, len(mod)):
                h1 = globals()['mod_'+str(i)]    
                # Loop through hierarchy level 1
                os.system('cls')
                # Loop through hierarchy level 2
                for j in range(1, len(h1)):
                    h2 = globals()['mod_'+str(i)+'_'+str(j)]  
                    os.system('cls')
                    # Loop through questions
                    for k in range(len(h2)):
                        # Question    
                        if check_comm == 'break':
                            break                       
                        question = h2[k][1]
                        check_comm = True
                        while check_comm == True:
                            check_comm_ = input(question+'\n')
                            check_comm = _commands(check_comm_)
                        if check_comm == 'break':
                                continue
                        # Answer 
                        answer = h2[k][2]
                        check_comm = True
                        while check_comm == True:
                            check_comm_ = input(answer+'\n')
                            check_comm = _commands(check_comm_)
                        if check_comm == 'break':
                            continue
                        delete_question(h2[k])
                        exec(open(current_session).read()) 
                        print('\n')
                        os.system('cls')                   
   
        # If a main module has been chosen
        else:
            i = num_
            # Address selected module
            h1 = globals()['mod_'+str(num_)]
            os.system('cls')
            # if all submodules have been selected
            if subnum_ == 0:
                # Loop through hierarchy level 2
                for j in range(1, len(h1)):
                    h2 = globals()['mod_'+str(i)+'_'+str(j)]
                    os.system('cls')
                # Loop through questions
                    for k in range(len(h2)):
                        # Question    
                        if check_comm == 'break':
                            break   
                        question = h2[k][1]
                        check_comm = True
                        while check_comm == True:
                            check_comm_ = input(question+'\n')
                            check_comm = _commands(check_comm_)
                        if check_comm == 'break':
                                continue
                            
                        # Answer 
                        answer = h2[k][2]
                        check_comm = True
                        while check_comm == True:
                            check_comm_ = input(answer+'\n')
                            check_comm = _commands(check_comm_)
                        if check_comm == 'break':
                            continue
                        delete_question(h2[k])
                        exec(open(current_session).read()) 
                        print('\n')
                        os.system('cls')
            
                                
            else:
            # If a sub module hase been chosen 
                h1 = globals()['mod_'+str(num_)]
                h2 = globals()['mod_'+str(num_)+'_'+str(subnum_)]
                os.system('cls')
                # Loop through questions
                for k in range(len(h2)):
                    # Question    
                    if check_comm == 'break':
                        break   
                    question = h2[k][1]
                    check_comm = True
                    while check_comm == True:
                        check_comm_ = input(question+'\n')
                        check_comm = _commands(check_comm_)
                    if check_comm == 'break':
                            continue
                        
                    # Answer 
                    answer = h2[k][2]
                    check_comm = True
                    while check_comm == True:
                        check_comm_ = input(answer+'\n')
                        check_comm = _commands(check_comm_)
                    if check_comm == 'break':
                        continue
                    delete_question(h2[k])
                    exec(open(current_session).read()) 
                    print('\n')
                    os.system('cls')
        
                     
    ### RANDOM LEARNING                              
    elif select_order == 'r':
        def rand_q(unpicked, h2_names):
            global check_comm
            check_comm = ''
            del_cnt_ = 0
            del_cnt = 0
            # loop through all random questions
            while unpicked != []:
                # pick a random question from unpicked array
                pick = random.choice(unpicked)
                # get index from random picked question
                pick_index = unpicked.index(pick)
                curr_mod = h2_names[pick_index]

                # Question
                if check_comm == 'break':
                    break 
                question = pick[1]
                check_comm = True
                while check_comm == True:
                    check_comm_ = input(question+'\n')
                    check_comm = _commands(check_comm_)
                if check_comm == 'break':
                        continue
                  
                # Answer
                if check_comm == 'break':
                    break 
                answer = pick[2]
                check_comm = True
                while check_comm == True:
                    check_comm_ = input(answer+'\n')
                    check_comm = _commands(check_comm_)
                if check_comm == 'break':
                    continue
                
                # get index for tb deleted elem from executed data
                orig_ind = [x for x in range(len(curr_mod)) if curr_mod[x] == pick]
                # delete elem from executed data
                curr_mod.pop(orig_ind[0])
                # delete elem from session file
                del_cnt_ = delete_question(pick)
                # execute updated session file
                exec(open(current_session).read()) 
                # delete picked from unpicked and mod names
                unpicked.pop(pick_index)
                h2_names.pop(pick_index)
                os.system('cls')
                    
            # Secure emptying temporary lists
            while len(unpicked) > 0 : unpicked.pop()
            while len(h2_names) > 0 : h2_names.pop()
                   
        # predefine arrays to be filled in random learning
        unpicked = []
        h2_names = []
        # If all Modules have been chosen loop through all Q&As
        if num_ == 0:
            # Loop through hierarchy level 1 
            for i in range(1, len(mod)):
                h1 = globals()['mod_'+str(i)]          
                # Loop through hierarchy level 2         
                for j in range(1, len(h1)):
                    h2_ = 'mod_'+str(i)+'_'+str(j)
                    h2 = globals()[h2_]
                    # Loop through questions
                    for k in range(len(h2)):
                        q_a = h2[k]
                        unpicked.append(q_a)
                        h2_names.append(h2)
            # start random learning             
            rand_q(unpicked, h2_names)

        else:
            # If one module has been chosen loop through all sub modules
            i = num_
            # Address selected module
            h1 = globals()['mod_'+str(num_)]
            # if all submodules have been selected
            if subnum_ == 0:
                # Loop through hierarchy level 2
                for j in range(1, len(h1)):
                    h2_ = 'mod_'+str(i)+'_'+str(j)
                    h2 = globals()[h2_]
                # Loop through questions
                    for k in range(len(h2)):
                        q_a = h2[k]
                        unpicked.append(q_a)
                        h2_names.append(h2)
                # start random learning         
                rand_q(unpicked, h2_names)
                
            # If one sub module has been chosen loop through q&as
            else:
            # If a sub module hase been chosen 
                h1 = globals()['mod_'+str(num_)]
                h2_ = 'mod_'+str(num_)+'_'+str(subnum_)
                h2 = globals()[h2_]
                # Loop through questions
                for k in range(len(h2)):
                        q_a = h2[k]
                        unpicked.append(q_a)
                        h2_names.append(h2)
                # start random learning  
                rand_q(unpicked, h2_names)


    # Show if session has been finished and/ or resume to main menu
    cnt_finmods = _finmods()
    
    if check_comm == 'break':
        pass
    elif cnt_finmods == 0:
        print('=> CONGRATULATIONS YOU HAVE COMPLETELY FINISHED THIS SESSION :-)')
        input('Press enter to resume to main menu ...')
        os.system('cls')
    else:
        input('You went through your selected learning unit.\nPress enter to resume to main menu ...')
        os.system('cls')
