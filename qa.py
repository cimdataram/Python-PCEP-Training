### Q&A DATA PER SUB MODULE


mod_1_0 = [[],]

mod_1_1 = [
[
'What can a computer without programming language understand?',
'Simple maths and simple commands [i.e. division, save, plus, minus, multiply].'
], 
[
'What have compilers and interpreters in common?',
'They transform programming language into machine language.'
],
[
'What is the computers native language called?',
'Machine language.'
],
[
'What is the instruction list [IL]?',
'A list of commands a computer knows without programming language.'
],
[
'What are the elements of a programming language\'s correctness?',
'alphabetically[chars], lexically[words], syntactically[rules], semantically[sense]'
],
[
'Name at least 5 aspects of a compiler being different from an interpreter.',

'> * Faster in executing the code [once compiled].\n'
'> Transformation into machine language on modifying saving code.\n'
'> Storing code by using machine language.\n'
'> Code must be compiled for each hardware it has to work with.\n'
'> Code is more like to remain secret.\n'
'> The compiling itself is often more time consuming then the interpreting.\n'
],
[
'Name at least 5 aspects of an interpreter being different from an compiler.',
'''
> * Slower in executing code [to be interpreted each time running the code].
> Transformation into machine language on running the code.
> Storing code without using machine language.
> Can run on hardware with different machine languages.
> Code is less likely to remain secret.
> End-user needs same interpreter as developer.'''
],
[
'How are interpreted languages also called?',
'script languages.'
],
[
'Is Python an interpreter language?',
'''
Yes. However working with importing modules of Python
there may also compiling occur (i.e. pycache folder)
'''
],
[
'Who created Python?',
'Guido van Rossum.'
],
[
'Please give at least 10 words to describe Python:',
'''
widely used, open source, object oriented, high-level programming language,
dynamic sematics, (interpreted) script language, uses plaine english,
relatively easy and intuitive'
'''
],
[
'Please mention at least 3 disadvantages of Python:',
'more difficult to debug, speed limits, weak for extreme performance (drivers) / engines],\nnot suitable for mobile apps (yet)'
],
[
'Please mention two rivals of Python and what makes them different from Python:',
'Perl (more conservative) // Ruby (more creative)'
],
[
'Please mention at least 3 IT-sectors Python is commonly used for:',
'''
web services // cloud storage // social media // open-source games //
scientific calculations // 3D CAD/CAM // Eenterprise applications //
image applications // mobile applications // office applications // bots //
desktop GUI\'s
'''
],
[
'Please mention at least 3 popular applications, websites or games Python has ben used for (in parts):',
'Spotify, Uber, Guitar-Hero, Pinterest, BuzzFeed, BitTorrent, '
],
[
'What is Python2 and what is it\'s current state?',
'Older version of original python // no new modifications only new bug fixes // \nstill used by a large community'
],
[
'What is Python3 and what is it\'s current state?',
'current version // regular Python3-compatible updates // \nrecommended for starting new projects'
],
[
'How are Python2 and Python3 are related?',
'not compatible [neither backwards nor upwards] // different syntax // \nnot the same programming language'
],
[
'What does PSF stand for in assictiation with Python?',
'Python Software Foundation'
],
[
'What does the Python Software Foundation do?',
'Community that aims to develop, improve, expand, and popularize Python \nand its environment.'
],
[
'Please mention 3 thoughts about the "CPython":',
'This course focusses on CPython // Python was written with C Language // Python can be ported / migrated to all sytems than run or compile C language.'
],
[
'What does Cython do?',
'automatically translates the Python code [clean and clear, but not too swift] \ninto "C" code  [complicated and talkative, but agile]'
],
[
'What is Jython?',
'Python written in Java instead of C // Jython can communicate with existing \nJava infrastructure // current Jython implementation follows Python2 standards'
],
[
'What is PyPy?',
'Python environment written in Python-like language named RPython,  \nsubset of Python translated into C and then executed separately,\nPyPy is compatible with the Python3 language.'
],
[
'What is Vyper?',
'subset of Python\n Also a plugin required to compile Vyper smart contracts for EVM (Ethereum Virtual Machine)'
],
[
'What is a debugger and what does it do?',
'A debugger is part if an IDE. It lets u launch code step by step. It is easier to find mistakes in the code or in the codes logic logic with it.'
],
]



mod_1_2 = [
[
'Which operating system has Python3 already installed?',
'Linux has Python3 already installed // open terminal/console and possibility to write python3'
],
[
'What is required to work with Python?',
'An editor (support in writing code) // console (launch entire code and stop on errors) // debugger (launch code step-by-step and inspect in the moment of execution)'
],
[
'What does IDLE mean?',
'IDLE is an acronym for Integrated Development and Learning Extension.'
],
[
'What are the quotation marks in Pythion called to use for defining Strings?',
'neutral quotes // straight quotes // dumb quotes.'
],
[
'What are parenthesis used for in Python?',
'To end functions (on definition and invocation), and possibly write parameters or arguments into the paranthesis.'
],
[
'What does EOF mean and when does it happen?',
'end-of-file // parsing errors // uncomplete code syntax'
],
[
'What does traceback mean in the shell?',
'Path that the code traverses through different parts of the program.'
],
[
'What does "location of the error" mean in the shell?',
'Name of the file,  line number and module name containing the error.\n(Note: the number may be misleading, as Python usually shows the place,\ where it first notices the effects of the error, not necessarily the error itself.)'
],
[
'What is a script in Python?',
'Text file that contains instructions  which make up a python program.'
],
[
'What do you call a command line interpreter,\n that lets you interact with the operating system and execute  Python commands and scripts.',
'Console // Shell.'
],
[
'What is machine code?.',
'Low level programming language with machine code instructions.\n Consisting of binary digits/bits that computer reads and understands.'
],
[
'What is a source file?',
'File containing written high level programming language.'
],
]

mod_2_0 = [[],]

mod_2_1 = [
[
'Where do Python functions come from?',
'built-in // modules // self-written'
],
[
'Where do Python modules come from?',
'some come with python // some must be installed'
],
[
'What is always required to define or invoke a function?',
'parantheis'
],
[
'What is function invocation?',
'It calls a function'
],
[
'What is legalty of a function in Python?',
'Functions that are allowed to use in Python'
],
[
'In which order does execute a function?',
'1) legalty 2) check number of arguments allowed 3) passing arguments into the function \n4) execution of code within function 5) return result'
],
[
'How many instructions does Python allow within one line?',
'Python requires that there cannot be more than one instruction in a line. \nBut it allows one instruction to spread across more than one line' 
],
[
'In which order does Python execute instructions in general?',
'In the same order in which they have been placed.'
],
[
'What is the outut of the following code? \nprint("\")',
'Syntax Error'
],
[
'What is the outut of the following code? \nprint("\\")',
'\\'
],
[
'How must arguements be seperated?',
'by commas'
],
[
'What are keyword arguments?',
'Arguments of a function. They have a predefined name that can be assigned with values. \n They can make the function work in a alternative way.'
],
[
'Of which elements does a keyword argument consist?',
'keyword, equal sign and value in quotes'
],
[
'Where are keword argumemnts placed?',
'At the last position within the parathesis of a function invocation'
],
[
'What is the default value of the "end" keyword argument in the print function and why?',
'\\n (to create automatic line break after printed content)'
],
[
'What does the "sep" keyword argumnent do in the print function?',
'The value you put into sep="value" will be used to seperate all arguments of the print function'
],
[
'What is the default value of the "sep" keyword argument of the print function?',
'space'
],
[
'What type of function is the print() function?',
'built-in function'
],
[
'What differs built-in-functions from other functions?',
'They don\'t have to be installed, imported or manually created.'
],
[
'What is another (more common) wording for function invocation?',
'function call.'
],
[
'Are Python strings are delimited with double quotes or single quotes?',
'Both is possible.'
],
[
'What is an instruction?',
'a command to perform a specific task when executed.'
],
[
'What are positional arguments?',
'Arguments whose meaning is dictated by their position.'
],
[
'What differs keyword arguments from positional arguments?',
'Keyword arguments are the ones whose meaning is not dictated by their position, but by a special word (keyword) used to identify them.'
],
]


mod_2_2 = [
[
'What is a literal?',
'A literal is data whose values are determined by the literal itself. \n Literals can have different data types such as string, boolean, integer, float etc. \n They are based on the idea of non-changing values (literally the value :-) \nYou use literals to encode data and to put them into your code.\n In other words: Literals are notations for representing some fixed values in code, e.g. numbers or strings.'
],
[
'What is the binary system?',
'Computers use the binary system for storing numbers (0 and 1), to perform operations upon them.'
],
[
'Which numeric data type has fractions?',
'float'
],
[
'What a numeric type?',
'The characteristic of the numeric value which determines its kind, range, and application.'
],
[
'How does Python store literals in the memory',
'If you encode a literal and place it inside Python code, the form of the literal determines the representation (type)\n so called duck typing.'
],
[
'Which numeric value has this literal? 11_111_111',
'11111111 (only works in Python Version >= 3.6)'
],
[
'Which unary operator is redundant, but not forbidden?',
'+'
],
[
'Which are values called that bgein with 0o and what is their range per char?',
'octal values, char range 8 (0 - 7)'
],
[
'Which are values called that bgein with 0x and what is their range per char?',
'hexadecimal values, char range 10 (0 - 9)'
],
[
'What is another (mathematical) wording for floating-point-numbers?',
'non-empty decimal fraction'
],
[
'What happens if you omit the zero of a floating-point-number?',
'nothing, it is the same as if you don\'t omit the zero'
],
[
'How can you write 3 x 10^8 in Python?',
'3E8'
],
[
'What is the E respreseting if you write i.e. 4E8',
'exponent'
],
[
'What does the letter E equal to in Python when you put it between two numbers?',
'...times ten to the power of...'
],
[
'What is the base number when you write i.e. 5E12',
'5 (base number is always in front of the E)'
],
[
'What is the exponent number when you write i.e. 5E12',
'12 (exponent number is always after the E)'
],
[
'How to write 6.62607 x 10^-34 in Python?',
'6.62607E-34'
],
[
'What will Python put out on print(0.000000000001)?',
'1e-12'
],
[
'What will Python put out on print(0.0000000135)?',
'1.35e-08'
],
[
'Why is it important to know that i.e. 0.0000000135 equals 1.35e-08?',
'Python always chooses the more economical form of the number\'s presentation, \nand you should take this into consideration when creating literals.'
],
[
'What are strings used for?',
'processing text'
],
[
'Please show 3 ways to escape Quotes within Quotes!',
'" ' ' "  OR  ' " " '  OR " \' \' "'
],
[
'How are empty strings processed by Python?',
'An empty string is still a string (a string with no chars between quotes)'
],
[
'What can you display with Boolean values?',
'truthfulness: True OR False'
],
[
'From whom got the boolean value its name?',
'George Boole (1815-1864) the author of the fundamental work, The Laws of Thought'
],
[
'Which numbers are representative for True and False?',
'True: 1 and False: 0'
],
[
'Which numbers are are represented in machine langauge?',
'Computers only know 0 and 1.'
],
[
'What is the output of the following code and why? print(true)',
'NameError:, Boolean values are case-sensitive.'
],
[
'Why is  print(True > False)  == True and  print(True < False) == False?',
'Because if True is larger then False, there is no False left as only one of these values can exist at the same time \n (this might change with quantum computers).'
],
[
'Write a one-line of code in Thonny, using the print() function. Expected Output:\n"I\'m" \n""learing""\n"""Python"""',
'''print('"I\\'m"\\n""learing""\\n"""Python"""')\nOR\nprint("\\"I'm\\"\\n\\"\\"learing\\"\\"\\n\\"\\"\\"Python\\"\\"\\""\nOR\nprint("\\"I\\'m\\"\\n\\"\\"learing\\"\\"\\n\\"\\"\\"Python\\"\\"\\"")'''
],
[
'Of which elements is a binary system made?',
'0 and 1'
],
[
'What is the common abbreviation of integer?',
'int'
],
[
'What are integers?',
'numbers without fractional component'
],
[
'What is the common abbreviation of floating-point-numbers?',
'float'
],
[
'What are floats?',
'numbers with fractional component'
],
[
'In which direction do you read hexadecimal binary numbers?',
'from rights to left (small numbers to high numbers)'
],
[
'How do you calculate binary numbers?',
'Each Bit has a boolean value to see if the allocated number is true or false.\nMax Numbers will be powered from left to right starting with 1\nAll true numbers will be summed up.'
],
[
'Please write the value of each bit for the result 255?',
'128    64    32    16    8     4     2     1'
],
[
'Please write the value of each bit for the result 16?',
'0      0      0    16    0     0     0     0'
],
[
'Please write the value of each bit for the result 37?',
'0      0     32     0    0     4     0     1'
],
[
'Please write the value of each bit for the result 224?',
'128   64     32     0    0     0     0     0'
],
[
'What is the decimal value of the following binary number? 1010?',
'10  (= 8 + 0 + 2 + 0)'
],
[
'What is the decimal value of the following binary number? 0110?',
'6 (= 0 + 4 +2 + 0)'
],
[
'What is the decimal value of the following binary number? 1001?',
'9 (= 8 + 0 + 0 + 1)'
],
[
'What is the decimal value of the following binary number? 01011010?',
'90 (= 0 + 64 + 0 + 16 + 8 + 0 + 2 + 0)'
],
[
'What is the decimal value of the following binary number? 11110000?',
'240 (= 128 + 64 + 32 + 16 + 0 + 0 + 0 + 0)'
],
[
'What is the decimal value of the following binary number? 00001111?',
'15 (= 0 + 0 + 0 + 0 + 8 + 4 + 2 + 1)'
],
[
'Of which characters does the hexadecimal system contain?',
'decimal numbers and six extra letters (a - f).'
],
]



mod_2_3 = [
[
'Which data type is the result of a multiplication?',
'integer. If at least one float ist used in the multiplication the result is float'
], 
[
'Mention 7 arithmetic Operators in Python!',
'+ -, *, /, //, %, **'
],
[
'What are expression',
'data and operators when connected together'
],
[
'What is the ** Operator?',
'exponentiation (power) operator'
],
[
'What is a dividend and what is a divisor?',
'In a divison the value in front of the slash is the dividend, the value behind the slash, the divisor.'
],
[
'Which data type is always the result of a regular division',
'float'
],
[
'What does the // operator do?',
'Division with result as integer, provided both arguments are integer as well.\nFloat numbers of the result are always rounded down meaning rounded to the lower integer (numbers behind floating point get cut).\nNegative Results are also rounded to the higher value or in other words the lower integer number, as if the minus would be ignored.'
],
[
'What is another wording for integer division?',
'floor division'
],
[
'What is the quotient',
'non-float number result after division (or result of a floor division)'
],
[
'What is the result of print(4.0 / 2)?',
'2.0'
],
[
'What is the result of print(4 / 2)?',
'2.0'
],
[
'What is the result of print(4 // 2)?',
'2'
],
[
'What is the result of print(4.0 // 2)?',
'2.0'
],
[
'What is the result of print(4 // 3)?',
'1'
],
[
'What is the result of print(3 // 4)?',
'0'
],
[
'Which operator is used for the Modulo it in Python?',
'% (remainder)'
],
[
'Which data type is always the result of a Modulo calculation?',
'integer (unless, a floating number was used in the division)'
],
[
'What does the Modulo do?',
'Result of dividend and divisor = remainder (modulo).\nThe result of the operator is a remainder left after the integer division.\nModulo results in integer as long as there is no float used as argument).'
],
[
'Which operator is used for the Modulo it in Python?',
'% (remainder)'
],
[
'What is the result of print(7 % 2)?',
'1'
],
[
'What is the result of print(17 % 3)?',
'2'
],
[
'What is the result of print(3 % 4)?',
'3'
],
[
'What unique ability has the minus operator?',
'It can change the sign of a number // It can make numbers negative'
],
[
'What are the values before and after the minus sign called?',
'minuend (before minus) //  subtrahend (after minus)'
],
[
'What is the difference between an unary and a binary operator?',
'A binary operation needs at least two numbers (one before and one after the operator). \nAn unary operation has only one number (after the operator) and just defines if a number is positive or negative.'
],
[
'What do you have to be aware of when you calculate combining multiplication or division with addition or subtraction?',
'Multiplications or divisions precede (are of higher priority than) additions or subtractions.'
],
[
'What is the phenomenon called that causes some operators to act before others',
'Hierarchy of priorities'
],
[
'How does Python process a calculation when there is no hierarchy of priorities in it?',
'by left-sided binding (from left to right)'
],
[
'What is the result of print(9 / 2 % 2) and why?',
'0.5  (4.5 / 2 remainder 0.5, no priority, but left-sided binding).'
],
[
'What is the result of print(10 + 2 / 2)?',
'11.0 (division before addition, float because of division).'
],
[
'What is the result of print(10 - 2 * 3)?',
'4 (multiplication before subtraction, no float).'
],
[
'What is the result of print(10 - 3 % 2)?',
'9 (modulo before subtraction, modulo results in integer as there is no float used as argument).'
],
[
'What is the result of print(10 - 3 % 4.0)?',
'7.0 (modulo before subtraction, results is float as result of modulo is float, cause float was used in one divisor).'
],
[
'What is the result of print(10 - 4 // 5)?',
'10 (modulo before subtraction, result of floor division is zero).'
],
[
'What is the result of print(14 % 3 + 1 * 2 - 1)?',
'3 (multiplication and modulo before addition and subtraction).'
],
[
'What is the result of print(14 % 4 + 8 / 4 - 1)?',
'3.0 (division before addition and subtraction, float because of regular division).'
],
[
'Which operators use ride-sided binding?',
'exponentiation **'
],
[
'What is right sided binding?',
'When code is executed from right to left'
],
[
'How would you explain in words how the following code is executed?: print(2**3)',
'The exponent 3 is to be applied onto 2.'
],
[
'How would you explain in words how the following code is executed?: print(4**3**2)',
'The exponent 2 is to be applied onto 3. Then the exponent of 9 is to be applied onto 4.'
],
[
'What is the result of print(3**2**2)?',
'81, right-sided binding of exponentials, 3**(2**2)'
],
[
'What is the result of print(2**2**3)?',
'265, right-sided binding of exponentials, 2**(2**3)'
],
[
'What is the result of print(15 % 4 + 8 // 4 - 1)?',
'4 (multiplication before addition and subtraction, no float because of floor division)'
],
[
'What is the result of print(14 // 3.0 + 3 ** 2 ** 2)?',
'85.0 ((right-sided binding of exponentials, division before addition, float because float is used as divisor)'
],
[
'What is the result of print(13 // 4 - 3 ** 1 ** -1)?',
'0.0 (right-sided binding of exponentials, division before addition, float because negative exponentials are expenential divisions)'
],
[
'What is the result of print(2 ** -2)?',
'0.25, same as 1 / (2*2)'
],
[
'What is the result of print(2 ** -3)?',
'0.125, same as 1 / (2*2*2)'
],
[
'What is the result of print(1 ** -1)?',
'1.0, same as 1 / (1*1)'
],
[
'What is the result of print(4 ** -2)?',
'1.0, same as 1 / (1*1)'
],
[
'What is the result of print(5 ** -2))?',
'0.04, same as 1 / (5*5)'
],
[
'Set the paranthesis of following the calculation in a way that it matches with the natural Python Priority:,\n13 // 4 - 3 ** 1 ** -1 * 2 + 4 - 3',
'((13 // 4) - ((3 ** (1 ** -1)) * 2)) + 4 - 3\n equals 3 - 6.0 + 1'
],
[
'Please explain what operators are?',
'Operators are special symbols or keywords which are able to operate on the values and perform (mathematical) operations. '
],
[
'What is the difference between an operator and an operand?',
'An operand is a number to be calculated by the operator, whereas an operator is used to calculate numbers.'
],
[
'Which operators have the highest priority in Python?',
'unary operators of power numbers and powered numbers'
],
[
'Which operators have the second highest priority in Python?',
'power operators'
],
[
'Which operators have the third highest priority in Python?',
'unary operators of non-power and non-powered numbers'
],
]





mod_2_4 = [
[
'What is a variables?',
'A variable is a named location reserve to store values in the memory.\nA variable is created or initialized automatically when you assign a value to it for the first time.'
],
[
'What is the main usage of variables?',
'store values in the cache'
],
[
'What is a another word for a variable relating to its usage?',
'container'
],
[
'What does every Python variable have?',
'a name and a value'
],
[
'What are the rules to define the name of a varible?',
'''Each variable must have a unique name (identifier). May only use upper-case, lower-case letters, digits, and the character _ (underscore)\nMust begin with a letter or underscore, whereby underscore is also considered as letter\nIs subject to case sensitivty\nMay not equal to a reserved keywords of python or imported/installedpythons modules\nMay not contain any announcing chars or syntax chars such as ' " \ % . ( )[]{}=!<> etc\nbecause these would interrupt defining the ariable name and create parsing errors or syntax errors'''
],
[
'Give some abstract examples of what is forbidden in setting a variable name in Python?',
'using only a  keyword such as (None, True, False, in, and, as etc)\nstarting with a number\ncontaining spaces\ncontaining Python Syntax such as quotes (if not escaped) double points: etc'
],
[
'What can you put inside a variable?',
'Anything, as long as you consider the rules related to the content you want to put in the container or pass to the container.'
],
[
'When comes a variable to existence?',
'when assigning a value to it.'
],
[
'How is the datatype of a variable recognised by Python?',
'By duck typing. You don\'t have to set the datatype manually as python automatically recognised\nthe datatype by anaylising the content of the variable each time it is called.'
],
[
'What is duck typing How does it work?',
'The datatype is recognised by a values format. The data type must not be manually defined.'
],
[
'What has to be done before using variable',
'the variable itself must be defined'
],
[
'What will be the output of the following code?\nif a == 0:\n    print(\'Hello\')',
'NameError: name \'a\' is not defined'
],
[
'Which usage has the equal sign in relation to variables?',
'assignment operator'
],
[
'What does the equal sign as assignment operator do?',
'It assigns the value of its right argument to the left, while the right argument may be an arbitrarily complex expression'
],
[
'How to calculate a square root in Python?',
'The exponent has to be 0.5, e.g. 25 ** 0.5 = 5.0'
],
[
'Please write the follinng assignment with short cut operator: x = x + 5',
'x += 5'
],
[
'Please write the follinng assignment with short cut operator: x = x * 2',
'x *= 5'
],
[
'Please write the follinng assignment with short cut operator: x = x - 2',
'x -= 5'
],
[
'Please write the follinng assignment with short cut operator: x = x / 2',
'x /= 5'
],
[
'Please write the follinng assignment with short cut operator: x = x % 2',
'x %= 5'
],
[
'Please write the follinng assignment with short cut operator: x = x // 2',
'x //= 5'
],
[
'Please write the follinng assignment with short cut operator: x = x ** 2',
'x **= 5'
],
[
'What does "Python is a dynamically-typed language" mean, in respect of variables?',
'you don\'t need to declare variables in the script, because they come to live by assigning a value to it'
],
[
'What is another wording for shortcut operators?',
'compound assignment operators'
],
[
'Which of the following variable names is illegal in Python and why?\nmy_var // m // 101 // averylongvariablename // m101 // m 101 // Del // del',
'illegal is: 101 (starts with a number)// m 101 (contains a space) // del (is a keyword)'
],
[
'Which of the following variable names is illegal in Python and why?\n_var  //  V  //  \'a  //  \'a  //  \a  // _  //  __ //  ___  //  ',
'\'a (syntax error because quote) // \'a  (escpaing only works within strings)  //  \a  (escpaing only works within strings)'
],
[
'Which of the following variable names is illegal in Python and why?\ner#1%  //  range  //  import  /  Import  //  .trans  //  .keyword  //  randint',
'er#1% (parser error EOF, #annouces comment) // import  (it is a keyword) // .trans (syntax error because it begins with a point)\nNote: range works as variable, as it is only recognised as a function if it is written with paranthesis range().\nSo without paranthesis "range" is not a keyword (this counts for other functions as well).\nSame counts for attributes / methods (e.g randint).\nMethods are only recognised as methods if it is written with a point after the object e.g.(random.randint)'
],
[
'Which of the following variable names is illegal in Python and why?\nhello1  //  hello!  //  hello.1  // hello(1) //  hello_1  //  _hello1  // _hello-1',
'hello!  (contains syntax char !)  // hello(1) (contains syntax chars() )  // _hello-1 (contains syntax char - )'
],
]



mod_2_5 = [
[
'What are the utilities of comments in code',
'explain code to humans //  maintain overview  //  plan code structure from a macro point of view before writing the code  itself and fill blocks afterwards\ninfo about the code author  //  mark a piece of code that currently isn\'t needed'
],
[
'What is a comment inside code?',
'A remark inserted into the program, which is omitted at runtime, is called a comment.\nIt has to be done in a way that won\'t force Python to interpret it as part of the code.'
],
[
'Which char is used to announce a one liner comment?',
'#'
],
[
'How to set a block as a comment?',
'Three neutral quotes or three double quotes before and after the target block\n\'\'\' content\'\'\'   OR   \"\"\"content\"\"\"'
],
[
'What is the shortcut to mark one line or text block as a comment in Python?',
'Mostly CRTL / (in windows) or CMD / (in MAC), but not in each IDE / IDLE\nNote: You have to mark the line or block before using the shortcut.'
],
[
'What is the Python shortcut to indent a line or block to the right and to the left?',
'TAB (to the right)  //  Shift TAB (to the left)\nNote: You have to mark the line or block before using the shortcut'
],
[
'How to create line breaks without using \n',
'You can use multi-lined triple quoted comments as content of a variable without having to code line breaks with \n'
],
[
'What is recommended regarding defining variable names?',
'give variables self-commenting names (i.e. length or width instead of myvar1).'
],
]

mod_2_6 = [
[
'What is the prompt string?',
'It can be used as argument inside the input() function to output a message on asking the user for an input'
],
[
'What is the main difference between the print() function and the input() function?',
'print() sends data to the console. input() gets data from the console.'
],
[
'What is the main usage of the input() function?',
'Receive data the user types while the programm is running'
],
[
'What makes the input() function unique compared to other functions?',
'It pauses continuation of the code and waits for a user input.\nIt makes the code interactive.'
],
[
'What is a programm called that does not receive data from the user?',
'deaf programm'
],
[
'What can the input function process?',
'keyboard typing, voice, images etc'
],
[
'What is to be done to save the data the user sends into the input() function?',
'store the input data into a variable'
],
[
'Which data type is always the result of the input() function?',
'String (even if you type a number). So if you need another datatype from the input() function it must be converted.'
],
[
'What is the main usage of the int() function?',
'Convert numeric strings into the integer data type.'
],
[
'What is the main usage of the float() function?',
'Convert numeric strings into the floating number data type.'
],
[
'What is an arithmetic operator?',
'An operator that performs mathematic calculations of two numeric values.'
],
[
'What is a comparison operation?',
'An operator to define conditions. For example to decide about if certain lines or blocks of the code will be executed.'
],
[
'What is a concatenation operator?',
'Concatenation operators are used to merge Strings.\nConcatenation only workls with strings, and not other datatypes.'
],
[
'What is a replication operator?',
'It is used to repeat a string x times (e.g. \'John\' * 3 gives the result \'JohnJohnJohn\'). It only works with strings.'
],
[
'How to convert a numeric datatype into a numeric string?',
'Using the str() function on a numeric data type (e.g. str(5) or str(7.0))'
],
[
'The most important difference between integer and floating-point-numbers is?',
'They are stored differently in the computer memory.'
],
[
'What is the output of the following code?\nz = y = x = 1\nprint(z, y, x, sep="*")',
'1*1*1'
],
[
'What is the output of the following code?\nx = input(2)\ny = input(4)\nprint(x + y)',
'24 (because it concatenated from two strings)'
],
[
'What is the output of the following code?\nprint(2 // 4 = 0)',
'SyntaxError: keyword can\'t be an expression'
],
[
'What is the output of the following code?\nprint(2 // 4)',
'0, because it is an integer division'
],
[
'What is the output of the following code?\nprint(4%0)',
'ZeroDivisionError'
],
[
'How many values can the print function output?',
'only one (one String)'
],
[
'How many arguments can the print() function take?',
'five arguments by default, but more is possible'
],
[
'Keyword parameter meaning is determindes by?:',
'its\' arguments name specified along with its value'
],
[
'What is the output of the following code?\nx = \'As a programmer my attention to details is \'+str(10/10.)\nprint(x)',
'As a programmer my attention to details is 1.0'
],
[
'What is the output of the following code?\nx = 37 + 2 // 3 + 5 % 2 - 1.\nprint(x)',
'37.0'
],
[
'What is the output of the following code?\nx = str(37 + 2 // 3 + 5 % 2 - 1.)\nprint(x)',
'37.0'
],
]



mod_3_0 = [[],]


mod_3_1 = [
[
'How many answers can a programm provide and which ones?',
'two, True and False'
],
[
'What is an equality operator and what does it do?',
'It checks if two values are the same'
],
[
'What is the output of the following code?\nif \'1\' == 1:\n    print(True)',
'no output'
],
[
'What is the output of the following code?\nif 1.0 == 1:\n    print(True)',
'True'
],
[
'What is the output of the following code?\nif \'1\' == str(1):\n    print(True)',
'True'
],
[
'What is the output of the following code?\nif str(1) == str(1.0):\n    print(True)',
'no output'
],
[
'What is the output of the following code?\nif str(float(1)) == str(1.0):\n    print(True)',
'True'
],
[
'How are equality operators binded and what does it mean?',
'left-side-binded. It compares firstly the left argument with the right argument.'
],
[
'Is the following statement true or false? 3 = 3 ',
'no answer, because = is an assignment operator not an equality operator.'
],
[
'Is the following statement true or false? 3 == 3 ',
'True'
],
[
'Is the following statement true or false? var == 3',
'NameError, as we have not defined the variable before'
],
[
'Do assignment operators or comparison operators have a higher priority and why?',
'Assignment operators have a higher priority, because the results of calculations must be considered in an comparison.'
],
[
'Please give two examples of non-strtict comparison operators:',
'<=  >='
],
[
'Please give two examples of strtict comparison operators:',
'<   >'
],
[
'Do equality comparison operators or strict and non-strict comparison operators have a higher priority and why?',
'non-strict and strict comparision operators have ahigher priority'
],
[
'Do non-strict or strict comparison operators have higher priority?',
'neither, they have the same priority as long as we exclude left-sided-binding priority.'
],

[
'Bring the following operators into the right order of priority. And put into parantheis those operators of same priority:\n**, - binary, ==, <, - unary, //, ==, %, *, + binary, + unary, /, >, =>,  !=, <=',
'(+ unary, - unary) (**) (*, /, //, %) (+ binary, - binary) (<, <=, >, >=) (==, !=)'
],

[
'Is the the following statement true or false?: 2**-(1**-1) == 2**(-1)**-1',
'True, because unary operators have highest priority and because of right-sided binding.'
],

[
'Is the the following statement true or false?: 2**-1**-1 == 2**(-1**-1)',
'True, because unary operators have highest priority and because of right-sided binding.'
],
[
'What will be the output of the following code ? print(50 > 100)',
'False'
],
[
'What will be the output of the following code ? print(100 > 100)',
'False'
],
[
'What will be the output of the following code ? print(100 >= 100)',
'True'
],
[
'What will be the output of the following code ? print(100 != 100)',
'False'
],
[
'What is an expression?',
'A question or an answer with the value of true or false.'
],
[
'What is indentation and how can you do it in Python?',
'It is fix part of syntax in relation with particular code elements.\nTo be done by horizontal distance between different lines or blocks within code.\nOne indentation is defined by one tabulator. \ Alternatively with Spaces (if you use spaces, four spaces are recommended, \nbecause on higher complexity of code another number of spaces can lead to indentation errors, \nespecially if you do not keep up the same system of indentation.)'
],
[
'What is an indented statement?',
'An indentation followed by code to be executed or not executed, depending on the code before the indentation.)'
],
[
'Which strict syntax order or has a conditional statement?',
'if     at least one space      expression     colon\n for example if 1 == 1:'
],
[
'What are nested conditions?',
'(indented) conditional statements within other conditional statements.'
],
[
'What is a cascade in respect of conditions?',
'subsequent if-elif-(else) statements.'
],
[
'What is the output of this function? print(max(\'abc\', \'xyz\'))',
'xyz'
],
[
'What is the output of this function? print(min(\'abc\', \'xyz\'))',
'abc'
],
[
'What is the output of this function? print(\'abc\' < \'xyz\')',
'True'
],
[
'What is the output of this function? print(\'abc\' > \'xyz\')',
'False'
],
[
'What is the output of the following code and why?\nr, t, u = 3, 6, 9\nprint(t)',
'6 because of positional assignment. '
],
[
'''
What is the output of the following code and  why?\nr, t, u = 3, 6, 9\nu, t, r = t, u, r\nprint(u, t, r, sep=””)
''',
'693 because of positional assignment and new assignment of values.'
],
[
'What is the output of the following code?\nx, y, z = 1, 2, 3\nx, y, z = z, y, x\nprint(x, y, z, sep=””)',
'321 because of positional assignment and new assignment of values.'
],
[
'What is the output of the following code?\nx, y, z = 1, 2, 3\nz, y, x = y, z, x\nprint(z, y, x, sep=””)',
'231 because of positional assignment and new assignment of values.'
],
[
'What is the output of the following code?\nx, y, z = 1, 2, 3\nz, y, x = y, z, x\nprint(y, z, x, sep="")',
'321 because of positional assignment and new assignment of values, and because result is printed in different order.'
],
[
'''
Whats is the output of the following code and why??
x = 7 
if x != 7: 
    print(x != 7, end =' ') 
if x >= 7: 
    print(x >= 7, end =' ') 
if x < 7: 
    print(x < 7, end =' ')  
else: 
    print(':-)', end =' ')
''',
'''
True :-)

first condition is not met , so no execution of print()
second condition is True and condition in print() results in True
third condition is not met, so no execution of print()
but else of third is met and result of print() is :-)
'''
],
[
'''
Whats is the output of the following code and why?
x = 17 
if x == 17: 
    print(x <= 15, end=" ") 
if x > 7: 
    print(x >= 15, end=" ") 
if x == 17.0: 
    print(x != 17.0, end=" ")
if x != 17.: 
    print(x == 17, end=" ")
else: 
    print(':-)', end="")
''',
'''
False True False :-)

first condition is met, and result of print() is False
second condition is met, and result of print() is True
third condition is met (no strict comparison, value of int and float is same) 
and result of print() is False (no strict comparison, value of int and float is same)
fourth condition is not met, so no execution of print()
but else of fourth condition is met and result of print is :-)
'''
],
[
'''
Whats is the output of the following code?
x = "1" 
if x == 1: 
    print("one") 
elif x == "1": 
if int(x) > 1: 
    print("two") 
elif int(x) < 1: 
    print("three") 
else: 
    print("four") 
if int(x) == 1: 
    print("five") 
else: 
    print("six") 
''',
'''
four five
'''
],
[
'''
Whats is the output of the following code?
x = 1 
y = 1.0 
z = "1" 
if x == y: 
    print("one") 
if y == int(z): 
    print("two") 
elif x == y: 
    print("three") 
else: 
    print("four")  
''',
'''
one two
'''
],
[
'What does the max() function do?',
'It returns the maximum value of the given arguments.\nStrings and numbers work. For strings the alphabetical order will be used to allocate a quantisation to the letters,\nwhereby lettersof later alphabetical order  have higher values that earlier letters.\ne.g. a < z and z > a\nThis also works with the strict comparison operators < >'
],
[
'''
What is pseudo code?
''',
'''
It is not completed programming language , which is not fully executable, 
but it is an abtract way (e.g. algorythm) to describe the problems to be solved by the programm. 
For example: Instead of execututing branches of conditional statements, 
we only note the conditions and only type text into its branches the print() function 
or type a comment what the execution would do if we would fully coded it. 
This way we can build up a programm step by step with structural levels of logic. 
This way we will usually do less mistakes on our way to finalising a programm.
'''
],
[
'What is a branch in respect of conditional statements?',
'The code content to be executed'
],
[
'How is the else-statement used?',
'never without previous if-statement  // as last branch of a cascade // optional // \nwith a colon right next to the else  // without else it is possible that none of the branches is executed'
],
]





mod_3_2 = [
[
'What is another wording for endless loop?',
'infinity loop '
],
[
'ow can you avoid an endless loop in a while loop?',
'The value referred to the while statament has to be modified in the instructions\nto fulfuill the target set in the conditionen expression at a time.'
],
[
'When are while loops prefered against for loops?',
'When you do not know how many times a loop should be executued.'
],
[
'When are for loops preferable against while loops?',
'When a loop should be executed an exact number of times.'
],
[
'What is a control variable?',
'Any variable after the for keyword is the control variable. '
],
[
'What does the in keyword word in a for loop do?',
'it introduces/announces a syntax element describing the range of possible values being assigned to the control variable.'
],
[
'Which range of numbers would range(178) create?',
'0 to 177'
],
[
'What is the nth element?',
'''
The last element of an array or a range of values, 
that ends one step before its numeric order value, 
if the first element of the same array or range starts 
with a numeric order of zero and not of 1. 
Therefore the nth element is often called n-1.
'''
],
[
'Which practical use has the pass keyword?',
'''
The body of function or loops require instructions. 
But if you want to fill these instructions later but run your code before to test it, 
you can skip the body with the pass keyword. 
So if you write pseudocode or partial pseudocode it can be used as placeholder.
Short: It is a placeholder for empty bodies of functions or loops that require instructions. 
(e.g. in pseudocode)
'''
],
[
'Which range of numbers would range(2, 19) create?',
'2 to 18'
],
[
'Which data type is accepted by the range() function?',
'Only integers'
],
[
'Which range of numbers would range(2, 20, 2) create?',
'2 to 18 with a step-width of 2, so 2 4 6 8 10 ... etc'
],
[
'Which range of numbers would range(2, 21, 2) create?',
'2 to 20 with a step-width of 2, so 2 4 6 8 10 ... etc'
],
[
'Which range of numbers would range(0, 15, 7) create?',
'0 to 14 with a step-width of 7, so 0  7  14 '
],
[
'Which range of numbers would range(1, 21, 7) create?',
'1 to 8 with a step-width of 7, so 1 8'
],
[
'Which range of numbers would range(0, 22, 7) create?',
'0 to 21 with a step-width of 7, so 0  7  14  21'
],
[
'Which range of numbers would range(22, 0, -7) create?',
'22 to 1 with a step-width of 7, so 22  15  8  1'
],
[
'Which range of numbers would range(21, 7, -7) create?',
'21 to 14 with a step-width of 7, so 21  14 '
],
[
'Which range of numbers would range(21, 6, -7) create?',
'21 to 7 with a step-width of 7, so 21  14   7'
],
[
'Which range of numbers would range(1, 1) create?',
'no range'
],
[
'''
What is the output of the following code?
power = 1
for expo in range(4):
    power *= 2
print("2 to the power of", expo, "is", power)
''',
'2 to the power of 3 is 16'
],
[
'What does  time.sleep(1) do?',
'It makes the pgrogramm wait 1 second before continuing.'
],
[
'What is another word for syntactic candy?',
'syntactic sugar'
],
[
'What is the purpose of syntactic candy?',
'''
It doesn't improve the language's expressive power, but only simplify the developer's work. 
For example it can shorten the code or make the code more clear to third persons or make the code more standardised, 
avoids obsoltete ccolaculating processes etc.
'''
],
[
'What is does the keyword break do?',
'''
break exits the loop immediately, and unconditionally ends the loop's operation; 
the program begins to execute the nearest instruction after the loop's body; 
'''
],
[
'What is does the keyword continue do?',
'''
continue - behaves as if the program has suddenly reached the end of the body; 
the next turn is started and the condition expression is tested immediately.
'''
],
[
'Does the for loop and while loop has an else statement as option?',
'Yes. If used the else is always executed once (at the end of the loop)'
],
[
'''
What is the output of the following code?
for i in "info@hello.io":
    if i == "@":
        break
    print(i, end='')
''',
'info'
],
[
'''
What is the output of the following code?
for digit in "01603100610":
    if digit == "0":
        print('x', end='')
    else:
        print(digit, end='')
''',
'x16x31xx61x'
],
[
'''
What is the output of the following code?
n = 3
while n > 0:
    print(n + 1, end=' ')
    n -= 1
else:
    print(n, end=' ')
''',
'4 3 2 0'
],
[
'''
What is the output of the following code?
n = range(4)
for num in n:
    print(num - 1, end=' ')
else:
    print(num, end=' ')
''',
'-1 0 1 2 3'
],
[
'''
What is the output of the following code?
for i in range(0, 6, 3):
    print(i, end=' ')
''',
'0 3'
],
[
'What is an algorithm?',
'a precise rule (or set of rules) or finite sequence specifying how to solve some problem.\n(must not be completed code)'
],
]


mod_3_3 = [
[
'What does conjunction mean in the decisioning logic?',
'A connection of conditions.'
],
[
'Please mention all logical operators and if they are binary or unary:',
'and (binary), or(binary), not (unary)'
],
[
'What can you say about the priority of logical operators?',
'The priority of logical operators is lower than those of the comparison operators and arithmetical operators.'
],
[
'Which logical operator is a disconjuction operator?',
'or'
],
[
'What is the not operator?',
'unary operator performing a logical negation'
],
[
'How is the priority between and, or not (use comparison operator to describe the priority)',
'and = not > or'
],
[
'Write the following code without using the word \'not\' so that it means the same: print(not (var <= 0))',
'print(var > 0)'
],
[
'What is the not operator?',
'unary operator performing a logical negation'
],
[
'Write the following code without using the word \'not\' so that it means the same: print(not (var == 0))',
'print(var != 0)'
],
[
'Fill the following sentence with the correct word:\nThe negation of a conjunction is the _________ of the negations.',
'disjunction'
],
[
'Fill the following sentence with the correct word:\nThe negation of a disjunction is the _________ of the negations.',
'conjunction'
],
[
'Please write the follwing sentence as code example:\nThe negation of a conjunction is the disjunction of the negations.',
'not (a and b) == (not a) or (not b)'
],
[
'Please write the follwing sentence as code example:\nThe negation of a disjunction is the conjunction of the negations.',
'not (a or b) == (not a) and (not b)'
],
[
'What does it mean when all the bits are reset?',
'False / zero '
],
[
'What does it mean when at least one bit is set?',
'True / not zero'
],
[
'What is a bitwise operator?',
'They are used to manipulate single bits of data. They deal with every single bit seperately.'
],
[
'What is the xor operator and what is its sign in Python?',
'^ only one of two arguments is allowed to be true for a conjunction to result in true.'
],
[
'Mention all 4 Bitwise Operators their sign and their meaning in Python:',
'& and, | or, ~ not, ^ xor (not to confuse with logical operators)'
],
[
'What is the written word in natural language for these signs &, |, ~, ^',
'ampersand, bar, tilde, caret'
],
[
'Which of the bitwise operators is unary?',
'only ~ the others are binary'
],
[
'What are the abbreviated forms of the bitwise operators to assign a new value to a variable?',
'&=, |=, =^'
],
[
'Which datatype may arguments of bitwise operators have?',
'only integer'
],
[
'What is the main difference between logical operators and bitwise operators?',
'The logical operators do not penetrate into the bit level of its argument.\nThey\'re only interested in the final integer value.'
],
[
'Which bit-value and numeric value does x get?\ni = 1001\nj = 1010\nx = i & j',
'1000 (8)'
],

[
'Which bit-value and numeric value does x get?\ni = 1101\j = 1011\nx = i & j',
'1001 (9)'
],
[
'Which bit-value and numeric value does x get?\ni = 1001\nj = 1010\nx = i | j',
'1011 (11)'
],
[
'Which bit-value and numeric value does x get?\ni = 1001\nj = 1010\nx = i ^ j',
'0011 (3)'
],
[
'Which numeric value and bit-value does x get?\ni = 6\nj = 7\nx = i & j',
'6 (0110)'
],
[
'''
Which numeric value and bit-value will x get?
i = 9
j = 3
x = i | j
''',
'11 (1011)'
],
[
'Which numeric value and bit-valudoes x get?\ni = 4\nj = 9\nx = i ^ j',
'13 (1101)'
],
[
'Explain bitmask:',
'A sequence of zeros and ones, whose task is to grab the value or to change the selected bits.'
],
[
'Which task order is to be fulfilled if you have to change one single bit.',
'''
1. check the state of the target bit.
2. Reset the target bit.
3. Set the target bit.
4. Negate the target bit.
'''
],
[
'Which mathematical operation corresponds to shift a bit one step to the left?',
'multipling by 2'
],
[
'Which mathematical operation corresponds to shift a bit one step to the right?',
'divinding by 2'
],
[
'Which mathematical operation corresponds to shift a bit two steps to the left?',
'multipling by 2 to the power of 2'
],
[
'Which mathematical operation corresponds to shift a bit fours step to the right?',
'divinding by 2 to the power of 4'
],
[
'What re Pythons signs for shift operators',
'<< (left shift), >> (right shift)'
],
[
'Are shift operators binary or unary?',
'binary'
],
[
'In a shift operation what does the left and right argument mean?',
'Left argument are the bits to be shifted. Right argument is the shift size in steps.\n(The operators itself only define the shift direction)'
],
[
'What is the arithemtical equivalent to this shift operation? x >>= 2',
'x =// (2 ** 2)'
],
[
'What is the arithemtical equivalent to this shift operation? x <<= 3',
'x =* 2 ** 2'
],
[
'What is the arithemtical equivalent to this shift operation? x >>= 4',
'x =// 2 ** 4'
],
[
'What is the arithemtical equivalent to this shift operation? x <<= 1',
'x =* (2 ** 1)'
],
[
'What is the result of this shift operation? 24 >>= 2',
'6'
],
[
'What is the result of this shift operation? 2 <<= 3',
'16'
],
[
'What is the result of this shift operation? 128 >>= 4',
'8'
],
[
'What is the result of this shift operation? 9 <<= 1',
'18'
],
[
'''
What is the output of the following snippet and why?
x = 1
y = 0
z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
''',
'''
False, because both arguments around AND are False, but the argument right to OR is not False, so it is True.
Therefore one of the OR-arguments is True. But in the print() function the True is negated, so final output is False.
'''
],
[
'''
x = 4
y = 1

a = x & y
b = x | y
c = ~x 
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
''',
'''
a = 0
b = 5
c = -5 
d = 1
e = 1
f = 16
'''
],
[
'How are the priorities of all operators in Python?',
'''
1  ~, +, - (unary)
2  **
3  *, /, //, %
4  +, - (binary)
5  <<, >>
6  <, <=, >, >=
7  ==, !=
8  &
9  |
10  =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=
'''
],
[
'What type of number is a number that begins with 0b?',
'binary number'
],
[
'What type of number is a number that begins with 0o?',
'octal number'
],
[
'What type of number is a number that begins with 0x?',
'hexadecimal number'
],
[
'How are the first to characters (i.e. 0b, 0o or 0x) to be read?',
'''
They are not part of the number itself,
they just announce what type of number is following after it.
'''
],

[
'''
What is the output of the following code?
a = 0b1111
print(a)
''',
'15'
],
[
'''
What is the output of the following code?
a = 0b1100101
print(a)
''',
'101'
],
[
'''
What is the output of the following code?
a = 0b001100
print(a)
''',
'12'
],
[
'''
What is the output of the following code?
a = 0b001100
print(a)
''',
'12'
],
[
'''
What does hexadecimal mean?
''',
'''
Hexa stands for six and decimal for ten. So the terminus hexadeximal is used
to describe that the base value of the hexadecimal system is 16.
'''
],
[
'''
How do you read hexadecimal numbers?
''',
'''
From right to left
The right number has a potenz of number*16**0
The second right number has a potenz of number*16**1
The third right number has a potenz of number*16**2
and so forth
These different positions have to be summed up to get the decimal number
'''
],
[
'''
How can you calculate a decimal number into a hexadecimal number?
''',
'''
Divide the target number through the first possible 16 pozenz (i.e. 4096) 
and allocate the result of the floor division to the 16 potenz position
The take the remaining value (modulo) and divide this value through the next smaller 16 potenz (i.e. 256)
and allocate the result the floor division to the 16 potenz position
And so forth until there is no remaining value.
For example 731:
731 // 256 = 2 = 2 (modulo 219)
219 // 16 = 13 = d (modulo 11)
11 // 1 = 11 = b
result = 0x2db
'''
],
[
'''
Which letters can be used in the hexadecimal system
and which numbers do they represent?
''',
'a = 10, b = 11, c = 12, d = 13, e = 14, f = 15'
],
[
'''
What is the output of the following code?
a = 0x1b
print(a)
''',
'27 (16 + 11)'
],
[
'''
What is the output of the following code?
a = 0x2c
print(a)
''',
'27 (32 + 12)'
],
[
'''
What is the output of the following code?
a = 0x111
print(a)
''',
'273 (256 + 16 + 1)'
],
[
'''
What is the output of the following code?
a = 0x1ae
print(a)
''',
'430 (256 + 160 + 14)'
],
[
'''
What is the output of the following code?
a = 0x0001f
print(a)
''',
'31 (16 + 15)'
],
[
'''
What is the output of the following code?
a = 12
print(hex(a))
''',
'0xc'
],
[
'''
What is the output of the following code?
a = 500
print(hex(a))
''',
'''
0x1f4 (1 and 15 and 4) or more precise (256/256 and 240/16 and 4)
or even more precise:
500 // 256 = 1 = 1
500 % 256 = 244
244 // 16 = 15 = f
244 % 16 = 4
4 // 1 = 4 = 4
'''
],
[
'''
What is the output of the following code?
a = 170
print(hex(a))
''',
'0xaa (10 and 10) or more precise (160/16 and 10)'
],
[
'How many days does a regular year have as hexadecimal number?',
'0x16d'
],
[
'What does octal mean?',
'It means a based on eight.'
],
[
'In which range of numbers does the octal number system work?',
'0 - 7'
],
[
'Does the octal number system work with letters too?',
'No. Only numbers.'
],
[
'''
How do you read octal numbers?
''',
'''
From right to Left.
The first right number has a value of number*8 **0
The second right number has a value of number*8**1
The third right number has a value of number*8**2
And so forth
These different positions have to be summed up to get the decimal number
'''
],
[
'''
How can you calculate a decimal number into a octal number?
''',
'''
Divide the target number through the first possible 8 pozenz (i.e. 512) 
and allocate the result of the floor division to the 8 potenz position
The take the remaining value (modulo) and divide this value through the next smaller 16 potenz (i.e. 64)
and allocate the result the floor division to the 8 potenz position
And so forth until there is no remaining value.
For example 731:
731 // 512 = 1 (modulo 219)
219 // 64 = 3 (modulo 27)
27 // 8 = 3 (modulo 3)
3 // 1 = 3
result = 0o1333
'''
],
[
'''
What is the output of the following code?
a = 0o541
print(a)
''',
'353 (320 + 4 + 1)'
],
[
'''
What is the output of the following code?
a = 0o123
print(a)
''',
'83 (64 + 16 + 3)'
],
[
'''
What is the output of the following code?
a = 0o222
print(a)
''',
'146 (128 + 16 + 2)'
],
[
'''
What is the output of the following code?
a = 0o01030
print(a)
''',
'536 (0 + 512 + 0 + 24 + 0)'
],
[
'''
What is the output of the following code?
a = 43
print(oct(a))
''',
'0o53 (40//8 and 3//1)'
],
[
'''
What is the output of the following code?
a = 199
print(oct(a))
''',
'0o307 (192//64 and 7//8 and 7//1)'
],
[
'''
What is the output of the following code?
a = 614
print(oct(a))
''',
'0o1146 (512//512 and 64//64 and 32//8 and 6//1)'
],
[
'''
What is the output of the following code?
a = oct(714)
print(a)
''',
'''
TypeError: unsupported operand type(s) for >>=: \'str\' and \'int\'
(because octal numbers are strings)
'''
],
[
'''
What is the output of the following code?
a = hex(13)
print(a)
''',
'''
TypeError: unsupported operand type(s) for >>=: \'str\' and \'int\'
(because hexadecimal numbers are strings)
'''
],
[
'''
What is the output of the following code?
a = int(hex(26))
print(a)

''',
'''
ValueError: invalid literal for int() with base 10: \'0x1a\'
because only numeric strings can be converted to a number with the int() function
if you do not set n argument for the base value
'''
],
[
'''
What is the output of the following code?
a = hex(26)
a = int(a, 16)
print(a)

''',
'''
26 (because the argument for the base value has been set to 16 for hexadecimal)
'''
],
[
'''
What is the output of the following code?
a = hex(17)
a = int(a, 16)
a >>= 2
print(a)

''',
'''
4
'''
],
[
'''
What is the output of the following code?
a = oct(37)
a = int(a, 8)
a >>= 3
print(a)

''',
'''
4
'''
],
[
'''
What is the output of the following code?
a = 11
a <<= 2
print(a)

''',
'''
44
'''
],
[
'''
What is the output of the following code?
a = oct(23)
a = int(a, 8)
a <<= 1
print(a)

''',
'''
46
'''
],
[
'''
What is the output of the following code?
a = hex(26)
a = bin(a)
print(a)

''',
'''
TypeError: 'str' object cannot be interpreted as an integer
'''
],
[
'''
How can you output the following code as integer number?
a = 0x39

''',
'''
print(a)
'''
],
[
'''
How can you output the following code as integer number?
a = hex(57)
''',
'''
print(int(a, 16))
'''
],
[
'''
How can you output the following code as integer number?
a = oct(38)
''',
'''
print(int(a, 8))
'''
],
[
'''
How can you output the following code as octal number?
a = hex(101)
''',
'''
print(oct(int(a, 16)))
'''
],
]




mod_3_4 = [
[
'What are multi-value-variables called?',
'arrays'
],
[
'What does multi-value-variable mean in respect of lists?',
'a list is a collection of elements, but each element is a scalar.'
],
[
'What type of data may lists contain at the same time?',
'any type: int, float, string, bool etc'
],
[
'With which index number does an array ALWAYS start?',
'0'
],
[
'Please change the value of the first list element to 23:\nnumbers = [10, 5, 7, 2, 1]',
'numbers[0] = 23'
],
[
'Please change the value of the third list element to 711:\nnumbers = [23, 5, 7, 2, 1]',
'numbers[2] = 711'
],
[
'Please print the fourth element of the list:\nnumbers = [23, 5, 711, 2, 1]',
'print(numbers[3])'
],
[
'Please show how many elements are in the list by using one line of code:\nnumbers = [23, 5, 711, 2, 1]',
'print(len(numbers))'
],
[
'Please delete the  fourth element of the list. And what will be the new indizies after deletion?\nnumbers = [23, 5, 711, 2, 1]',
'del number[3]\n0 1 2 3'
],
[
'What happenes to the indidzies of a list when you delete an element which is not the last element using the del command?',
'All indizies higher that the deleted one will get decrement its number by -1.'
],
[
'Are negative indizies legal or illegal?',
'legal'
],
[
'What negative index has the last element of a list?',
'[-1]'
],
[
'What negative index has the first element of a list with 7 elements?',
'[-7]'
],
[
'What is aonther word for a variable that can store only one value at the same time?',
'scalar'
],
[
'What is the result of the following code?\nx = 2 // 4 = 0',
'0'
],
[
'What is the result of the following code?\nx = -2 // 4',
'-1 because the next lower integer number to 0.5 is -1'
],
[
'What is a method and what can it do?',
'''
A method is a specific kind of function. It gets data, it may create new data and it (generally) produces a result.
It is also able to change the state of a selected entity. A method is owned by the data it works for.
'''
],
[
'What is the main difference between a method and a function?',
'A method is owned by the data it works for, while a function is owned by the whole code.'
],
[
'Which syntactic element does a method require?',
'dot after the entity and parantheis after the method\nentity.method()\nHere the entitity is the data which owns the method.'
],
[
'What does the append method do?',
'It adds a new element to an array at the end of the array.\narray.append(value)'
],
[
'What does the insert method do?',
'It can add a new element at any place in the array.\narray.insert(location, value)'
],

[
'''
Which index will number 134 have after applying the insert method onto the array and why?
numbers = [111, 7, 2, 134, 1]
numbers.insert(2, 222)
''',
'4, because all indizies >= the inserted index will be incremented by +1'
],
[
'Please create a list array with the content [1,2,3,4,5,6,7]\nusing only three lines of code including and  a loop:',
'''
list = []
for i in range(7):
    list.append(i + 1)
'''
],
[
'Please create a list array with the content [7, 6, 5, 4, 3, 2, 1] \nusing only three lines of code including and a loop:',
'''
list = []
for i in range(7):
	list.insert(0, i + 1)
'''
],
[
'What is bad practice in programming?',
'Code written not wrong, but not good, for example:\ntoo long, confusing variable names or function names, redundancies, no commenting, etc.'
],
[
'Sum up the values of the following array within one line of code without using a loop:\nmy_list = [10, 1, 8, 3, 5]',
'total = sum(my_list)'
],
[
'Sum up the values of the following array within two lines of code using a loop:\nmy_list = [10, 1, 8, 3, 5]',
'''
for i in range(len(my_list)):
    total += my_list[i]
'''
],
[
'''
Please swap the values of the following 2 variables within one line of code:
x = 1
y = 2
''',
'x, y = y, x'
],
[
'''
Please swap the values of the following array using a loop within 2 lines of code
Note: first element should get value of last element and vice versa
and send element should get element of second last element and vice versa and so forth:
list = []
for r in range(100):
    list.append(r)
''',
'''
length = len(list)
for i in range(len(list) // 2):
    list[i], list[-i-1] = list[-i-1], list[i]
'''
],
[
'''
Please swap the values of the following array without using a loop within one line of code:
Note: first element should get value of last element and vice versa
and send element should get element of second last element and vice versa and so forth:
list = [5, 11, 2, 23, 1, 31]
''',
'list.reverse()'
],
[
'''
Please sort the following list in an ascending order within one line of code:
list = ['Z', 'G', 'X', 'E', 'S', 'B']
''',
'list.sort()'
],
[
'''
Please sort the following list in an descending order within one line of code:
list = ['Z', 'G', 'X', 'E', 'S', 'B']
''',
'list.sort(reverse=True)'
],
[
'Please describe waht a list is is Python:',
'List is a type of data that can store multiple objects as an ordered and mutable collection.\nLists can be indexed and updated, nested, deleted, iterated.'
],
[
'''
What is the output of the following snippet?
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
''',
'[6, 2, 3, 4, 5, 1]'
],
[
'''
What is the output of the following snippet?
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
''',
'[1, 3, 6, 10, 15]'
],
[
'''
What happens when you run the following snippet?
lst = []
del lst
print(lst)
''',
'NameError: name \'lst\' is not defined'
],
[
'3_4_7',
'3_4_7'
],
[
'''
What is the output of the following snippet?
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
''',
'''
[2, 3]
3
'''
],
]





mod_3_5 = [
[
'How do sorting algorhythms work?',
'They compare the adjacent elements, and keep on swapping them until none is smaller than the previous\n(or none previous is higher than the current one).'
],
[
'''
What is the output of the following code?
list = [8, 10, 6, 2, 4]
a = True
while a:
    a = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            a = True
            list[i], list[i + 1] = list[i + 1], list[i]
print(list)
''',
'[2, 4, 6, 8, 10]'
],
[
'''
Please sort the following array in a descending order within one line of code:
list = [8, 10, 6, 2, 4]
''',
'list.sort(reverse = True)'
],
[
'''
a = "A"
b = "B"
c = "C"
d = " "
lst = [a, b, c, d]
lst.reverse()
print(lst)
''',
'['', \'C\', \'B\', \'A\']'
],
[
'How is the Python character sorting hierarchy structured roughly?',
'''
Special chars, then numbers, then capital letters, then letters,
then other certain special chars like |, ~, §,
and then other letters of non english alphabets like ß, ó, à etc
'''
],
[
'''
What will be the output of the following code?
a = '3Txó§~%'
b = []
for i in a:
    b.append(i)
b.sort()
print(b)
''',
'''
['%', '3', 'T', 'x', '~', '§', 'ó']
'''
],
[
'''
What will be the output of the following code?
a = '4Uv!|+$'
b = []
for i in a:
    b.append(i)
b.sort()
print(b)
''',
'''
['!', '$', '+', '4', 'U', 'v', '|']
'''
],
[
'''
What will be the output of the following code?
a = 'Zu9Gp7'
b = []
for i in a:
    b.append(i)
b.sort()
print(b)
''',
'''
['7', '9', 'G', 'Z', 'p', 'u']
'''
],
[
'''
What will be the output of the following code?
a = str(hex(15))
b = []
for i in a:
    b.append(i)
b.sort()
print(b)
''',
'''
['0', 'f', 'x']
'''
],
[
'''
What will be the output of the following code?
a = str(hex(197))
b = []
for i in a:
    b.append(i)
b.sort()
print(b)
''',
'''
['0', '5', 'c', 'x']
'''
],
[
'''
What will be the output of the following code?
a = 1
b = '2'
c = [1, 2]
print(a+b+c)
''',
'''
TypeError: unsupported operand type(s) for +: 'int' and 'str'
because you cannot sum up strings with intergeers without using a work around
'''
],
[
'''
What will be the output of the following code?
a = 1
b = '2'
print(a+b)
''',
'''
TypeError: unsupported operand type(s) for +: 'int' and 'str'
because you cannot sum up strings with intergers without using a work around
'''
],
[
'''
What will be the output of the following code?
a = 1
b = 2
print(a+b)
''',
'''
3
'''
],
[
'''
What will be the output of the following code?
a = '1'
b = '2'
print(a+b)
''',
'''
12
'''
],
[
'''
a = 1
b = '2'
print(str(a)+int(b))
''',
'''
TypeError: can only concatenate str (not "int") to str
'''
],
[
'''
a = 1
b = '2'
print(a, b, sep='')
''',
'''
12
'''
],
[
'''
a = 1
b = '2'
print(str(a), int(b), sep='')
''',
'''
12
'''
],
]



mod_3_6 = [
[
'''
What is the ouptutof th following code?
list_1 = [1]
list_2 = list_1
list_1[0] = 7
print(list_2)
''',
'7'
],
[
'What is the name of a list in respect of its storage?',
'It is the name of a memory location where the list is stored.'
],
[
'What is the name of a variable in respect of its storage?',
'It is the name of its content.'
],
[
'''
Which statement is true assigning lists without using a slice?
a) Assigning one list to another stores only the name of the list, and does not copy its contents.
b) Storing the name of a list creates a reference and is not copying the content of the list.
c) The content remains stored unique in the original list.
d) Modifying one of the lists affects the other list, and vice versa.
e) Actually both lists can be considered as the same, and both lists be controlled through both names.
f) Python allocates the same id for to lists for storage.
''',
'All statements are true. REMEMBER: NO SLICE = REFERENCE!!!'
],
[
'''
Which statement is true assigning lists by using a slice?
a) Assigning one list to another copies the contents of the lists.
b) This does not create a reference and both lists are indepened from each other.
c) After copying the content is stored 2 times, each ycopy in another list.
d) If you change the content of one list this will not affect the other list, and vice versa.
e) Python allocates different id for to lists for storage.
''',
'All statements are true. REMEMBER SLICE = COPY!!!'
],
[
'What is a slice?',
'A slice is an element of Python syntax that allows you\nto make a brand new copy of the content of a list, or content parts of a list.'
],
[
'What does a slice do?',
'When assigning a list, a slice copies the list\'s contents, not the list\'s name.\nTherefore it is NOT A REFERNCE to the content, but a COPY of the Content!!!'
],
[
'When do you use a slice?',
'If you want to store list content in a container to keep it independed from future changes of the assigned list content.'
],
[
'How would you assign all content from list_a to list_b using a slice?',
'list_b = list_a[:]'
],
[
'How would you assign the first three data sets from list_a to list_b using a slice?',
'list_b = list_a[:3]'
],
[
'How would you assign the last three data sets from list_a to list_b using a slice?',
'list_b = list_a[-3:]'
],
[
'Is the end element of a slive inclusive or exclusive?',
'An element with an index equal to end is the first element,\nwhich does not take part in the slicing.\nThis means the used end index is exclusive!!'
],
[
'What is the output of a slice if the start index is >= the end index.',
'An empty list.'
],
[
'Which index does the last element of a slice always have?',
'-1'
],
[
'What is always the first index of a slice?',
'0'
],
[
'What happens if you omit start and end of a slice?',
'The entire list will be copied.'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 17, 2]
new_list = my_list[-1:-1]
print(new_list)
''',
'[]'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 17, 2]
new_list = my_list[-5:1]
print(new_list)
''',
'[10]'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 17, 2]
new_list = my_list[-3:4]
print(new_list)
''',
'[6, 17]'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 17, 2]
new_list = my_list[3:]
print(new_list)
''',
'[17, 2]'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 17, 2]
new_list = my_list[:]
print(new_list)
''',
'[10, 8, 6, 17, 2]'
],
[
'What does the del keyword do if you use a slice?',
'The del instruction will delete list elements including content and index.\nIndizies higher than the deleted one, will be decremented by -1'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 4, 2]
del my_list[:2]
print(my_list)
''',
'[6, 4, 2]'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 4, 2]
del my_list[-2:4]
print(my_list)
''',
'[10, 8, 6, 2]'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 4, 2]
del my_list[:3]
print(my_list[1])
''',
'2'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 4, 2]
del my_list[2:3]
print(my_list[2])
''',
'4'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 4, 2]
del my_list[:-4]
print(my_list)
''',
'[8, 6, 4, 2]'
],
[
'''
What is the output of the following snippet?
my_list = [10, 8, 6, 4, 2]
del my_list[:-4]
print(my_list[3])
''',
'2'
],
[
'What do the in and not in keywords do?',
'They check if a value is in or not in a list.'
],
[
'''
What is the output of the following snippet?
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
''',
'False'
],
[
'''
What is the output of the following snippet?
my_list = [0, 3, 12, 8, 2]
print(5 not in my_list)
''',
'True'
],
[
'''
What is the output of the following snippet?
my_list = [0, 3, 12, 8, 2]
print(12 in my_list)
''',
'True'
],
[
'''
What is the output of the following snippet?
my_list = [0, 3, 12, 8, 2]
print(12 in my_list and 3 in my_list)
''',
'True'
],
[
'''
What is the output of the following snippet?
my_list = [0, 3, 12, 8, 2]
print(12 in my_list and 5 in my_list)
''',
'False'
],
[
'''
What is the output of the following snippet?
my_list = [0, 3, 12, 8, 2]
print(12 in my_list or 5 in my_list)
''',
'True'
],
[
'''
my_list = [0, 3, 12, 8, 2]
print(55 or 5 in my_list)
''',
'55, because 55 is no conditional argument'
],
[
'''
What is the output of the following code?

my_list = [17, 3, 11, 5, 1, 9, 7, 55, 13]
a = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > a:
        a = my_list[i]
print(a)
''',
'55'
],
[
'''
Find the largest value in the list using one line of code:
my_list = [17, 3, 11, 5, 1, 9, 7, 55, 13]
''',
'print(max(my_list))'
],
[
'''
What is the output of the following snippet?
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)
''',
'4'
],
[
'''
What is the outut of the following code?

list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
aux = []
for i in list:
    if i not in list[i:-1]:
        aux.append(i)
list = aux[:]
print(list)
''',
'9'
],
[
'''
What is the outut of the following code?

list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
aux = []
for i, j in enumerate(list):
    if j not in list[i+1:-1]:
        aux.append(j)
list = aux[:]
print(list)
''',
'[1, 4, 6, 2, 9]'
],
[
'''
What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[0]

print(list_3)
''',
'[\'C\'], because we did not copy the content with a slice'
],
[
'''
What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
''',
'[\'B\', \'C\']'
],
[
'''
What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
''',
'[]'
],
[
'''
What is the output of the following snippet?
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
''',
'[\'A\', \'B\', \'C\']'
],
[
'''
Insert in or not in instead of ??? so that the code outputs the expected result.
my_list = [1, 2, "in", True, "ABC"]

print(1 ??? my_list)  # target output True
print("A" ??? my_list)  # target output True
print(3 ??? my_list)  # target output True
print(False ??? my_list)  # target output False
''',
'''
print(1 in my_list)
print("A" not in my_list)
print(3 not in my_list)
print(False in my_list)
'''
],
]



mod_3_7 = [
[
'What is a list comprehension in Python?',
'''
A list, but created on-the-fly during program execution, and is not described statically.
EXAMPLES:
row = [data for i in range(x)]
squares = [x ** 2 for x in range(10)]
odds = [x for x in squares if x % 2 != 0 
'''
],
[
'What are two-dimnesional arrays?',
'arrays within arrays for example lists in lists or tuples in lists'
],
[
'What is the algebraic analogy to a two-dimansional array?',
'matrix'
],
[
'What would be an example of a two-dimensional 3x3 array to be written within one line of code?',
'array = [[1 for i in range(3)] for j in range(3)]'
],
[
'Which parts of a loop creates which dimension of a two dimensional array?',
'The inner part creates a row (1st dimension), and the outer part builds a list of rows (2nd dimension).'
],
[
'How can you find an element of a two-dimenesional array?',
'''
You have to use two coordinates:
a vertical one (row index)
and a horizontal one (column index).
'''
],
[
'How to change the value of an element of a two-dimenesional array? ',
'''
You have to use two indzies and assign a value, for example:
array = [[1 for i in range(3)] for j in range(3)] 
array[1][2] = 6
'''
],
[
'''
What is the output of the following snippet?
array = [[1 for i in range(3)] for j in range(3)] 
array[1][2] = 6
print(array)
''',
'[[1, 1, 1], [1, 1, 6], [1, 1, 1]]'
],
[
'''
What is the output of the following snippet?
array = [[1 for i in range(3)] for j in range(3)] 
array[2][0] = 6
print(array)
''',
'[[1, 1, 1], [1, 1, 1], [6, 1, 1]]'
],
[
'''
What is the output of the following snippet?
array = [[1 for i in range(3)] for j in range(3)] 
array[0][1] = 6
print(array)
''',
'[[1, 6, 1], [1, 1, 1], [1, 1, 1]]'
],
[
'Create a two-dimensional array with 77 rows and 38 columns within one line of code,\nwhereby the content of each element should be 1:',
'array = [[1 for row in range(77)] for col in range(38)]'
],
[
'Create a three-dimensional 2x2x2 array to be written within one line of code,\nwhereby the content of each element should be 1:',
'array = [[[1 for r in range(2)] for f in range(2)] for t in range(2)]'
],
[
'Type a three-dimesional array only using square brackets without content:',
'[[][]] [[][]]'
],
[
'''
What is the output of the following snippet?
array = [[[1 for r in range(2)] for f in range(2)] for t in range(2)]
array[0][1][1] = 6
print(array)
''',
'[[[1, 1], [1, 6]], [[1, 1], [1, 1]]]'
],
[
'''
What is the output of the following snippet?
array = [[[1 for r in range(2)] for f in range(2)] for t in range(2)]
array[1][0][0] = 6
print(array)
''',
'[[1, 1][1, 1]] [[6, 1][1, 1]]'
],
[
'''
What is the output of the following snippet?
array = [[[1 for r in range(2)] for f in range(3)] for t in range(2)]
array[1][2][0] = 6
print(array)
''',
'[[1, 1][1, 1][1, 1]][[1, 1][1, 1][6, 1]]'
],
[
'''
What is the output of the following snippet?
array = [[[1 for r in range(3)] for f in range(2)] for t in range(2)]
array[0][1][2] = 6
print(array)
''',
'[[1, 1, 1][1, 1, 6]][[1, 1, 1][1, 1, 1]]'
],
[
'What does the first bracket stand for?\narray[][][]',
'The outer array block'
],
[
'What does the last bracket alwaysstand for?\narray[][][]',
'The inner array block'
],
[
'An operator able to check whether two values are not equal is coded as:',
'!='
],
[
'''
How many asterisks will the following snippet send to the console?
i = 2
while i <= 0:
    print("*")
    i -= 2
''',
'No asterisks'
],
[
'''
How many starts will the following snippet send to the console?
i = 2
while i >= 0:
    print("*")
    i -= 2
''',
'two'
],
[
'''
How many hashes will the following snippet send to the console?
for i in range(-1, 1):
    print("#")
''',
'two'
],
[
'''
What value will be assigned to the x variable?
z = 10
y = 0
x = z > y or z == y
''',
'True'
],
[
'''
What is the output of the following code?
list = [3, 1, -1]
list[-1] = list[-2]
print(list)
''',
'[3, 1, 1]'
],
[
'''
What happens to the length of the list after execution of the following code?
vals = [0, 1, 2]
vals[0], vals[1] = vals[1], vals[2]
''',
'Nothing, the length remains the same, only the values change.'
],
[
'''
Is nums or vals longer or are they same length?
nums = []
vals = nums
vals.append(1)
''',
'same length, as vals is referred to nums'
],
[
'''
Is nums or vals longer or are they same length?
nums = []
vals = nums[:]
vals.append(1)
''',
'vals is longer als vals is an own list not referred to nums'
],
[
'''
How many elements does list contain?
list = [0 for i in range(1, 3)]
''',
'two'
],
[
'''
What is the output of the following snippet?
list = [0, 1, 2, 3]
x = 1
for elem in list:
    x *= elem
print(x)
''',
'''
0, because after the first loop x becomes 0
and in the coming loops each value will be multiplied with 0
'''
],
[
'''
What is the output of the following code?
list = [3, 1, -2]
print(list[list[-1]])
''',
'1'
],
[
'''
What is the output of the following code?
var = 0
while var < 6
    var += 1
    if var % 2 == 0:
        continue
    print(var, end='')
''',
'SyntaxError, because the colon is missing at the end of the while statement'
],
[
'''
What is the output of the following code?
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print(var, end='')
''',
'135'
],
[
'''
What is the output of the following snippet?
list = [1, 2, 3]
for v in range(len(list)):
    list.insert(1, list[v])
print(list)
''',
'[1, 1, 1, 1, 2, 3]'
],
[
'''
What is the output of the following snippet?
for i in range(3):
    print(i, end='')
''',
'012'
],
[
'''
What is the output of the following snippet?
list = [1, 2, 3]
for v in range(len(list)):
    list.insert(1, v)
print(list)
''',
'[1, 2, 1, 0, 2, 3]'
],
[
'''
What is the output of the following snippet?
list = [1, 2, 3]
for v in range(len(list)):
    list.insert(v, v)
print(list)
''',
'[0, 1, 2, 1, 2, 3]'
],
[
'''
How many starts will the following nippet send to the console?
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")
''',
'one'
],
[
'''
What is the output of the following snippet?
list_1 = [1,2,3]
list_2 = []
for v in list_1:
	list_2.insert(0, v)
print(list_2)
''',
'[3, 2, 1]'
],
[
'''
What is the output of the following code?
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(sum(vals))
''',
'4'
],
[
'''
Will the list extend or reverse or not change or shorten??
cals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
''',
'reverse'
],
[
'''
What is the output of the following snippet?
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c + d + e)
''',
'2'
],
[
'If you use the range() function and don\'t give a start value: \n At which value will the range start?',
'0'
],
[
'If you use the insert() method and type in 0 as position to insert to: \n At which position will the the value be inserted?',
'first'
],
[
'If you use the insert() method and type in 1 as position to insert to: \n At which position will the the value be inserted?',
'second'
],
[
'What does the id() function do?',
'It show the id number of the stored object allocated by Python to its\' cache.'
],
[
'''
What is the output of the following snippet?
def func():
    global lst
    lst = [4, 5, 6]
lst = [1, 2, 3]
func()
print(lst)
''',
'[4, 5, 6]'
],
[
'''
What is the output of the following snippet?
def func():
    lst
    lst = [4, 5, 6]
lst = [1, 2, 3]
func()
print(lst)
''',
'[1, 2, 3]'
],
[
'''
What is the output of the following snippet?
def func(lst):
    lst = [4, 5, 6]
lst = [1, 2, 3]
func(lst)
print(lst)
''',
'[1, 2, 3]'
],
[
'''
What is the output of the following snippet?
def func(lst):
    lst = [4, 5, 6]
    return lst
lst = [1, 2, 3]
lst = func(lst)
print(lst)
''',
'[4, 5, 6]'
],
[
'What happens if you pass list to a function and assign a new list to it',
'The list will be consiered as local variable (it is a shadowed copy not a reference)'
],
[
'What happens if you pass or use a list to / in a function and change the value of an element?',
'The list will handled as reference and the alue of the element changes globally'
],
[
'''
What is the output of the following snippet?
def func(lst):
    lst[0] = 11
lst = [1, 2, 3]
func(lst)
print(lst)
''',
'[11, 2, 3]'
],
[
'''
What is the output of the following snippet?
def func():
    lst[0] = 11
lst = [1, 2, 3]
func()
print(lst)
''',
'[11, 2, 3]'
],
[
'What happens if you add to a dict a element with a key that already exists?',
'The existing key will be overwritten'
],
[
'''
What is the output of the following snippet?
d = {1:1, 1:1, 2:2, 3:3}
print(d)
''',
'{1: 1, 2: 2, 3: 3}'
],
[
'''
What is the output of the following code?
nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(vals)
print(nums)
''',
'''
[1, 3]
[1, 3]
'''
],
[
'''
What is the output of the following code?
nums = [1, 2, 3]
vals = nums
del vals[-1:-2]
print(vals)
print(nums)
''',
'''
[1, 2, 3]
[1, 2, 3]
'''
],
[
'''
What is the comparison operation to check if two values are the same?
''',
'''
==

'''
],
[
'''
What is the output of the following code?
my_list = [3, 1, -2]
print(my_list[my_list[-1]])
''',
'''
1
'''
],
[
'''
How many starts will th following code output?
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print('*')
''',
'''
one 
because the loop is stopped due to break after module
resultsing 0 for the first time
'''
],
[
'''
How many elements does my_list contain?
my_list = [i for i in range(-1, 2)]
''',
'''
three (-1, 0 and 1, )
2 is excluded
'''
],
[
'''
What is the output of the following code?
lst1 = [1, 2, 3]
lst2 = []
for v in lst1:
    lst2.insert(0, v)
print(lst2)
''',
'''
[3, 2, 1] because the next higher number will always be placed as new first element
'''
],
[
'''
What is the output of the following code?
lst = [1, 2, 3, 4]
print(lst[-3:-2])
''',
'''
[2] because only one element will be printed
(the third last one, as the second last one is excluded)
'''
],
[
'''
What is the output of the following code?
lst = [1, 2, 3]
for v in range(len(lst)):
    lst.insert(1, lst[v])
print(lst)
''',
'''
[1, 1, 1, 1, 2, 3]
because each new element will be placed as second element, 
but the element to be placed is always the last second element 
and therefore the one that has been placed last
'''
],
[
'''
How many hashed will the following snippe send to the console?
var = 1
while var < 10:
    print('#')
    var <<= 1
''',
'''
four (because the binary number gets left shifted 3 times,
therefore the the loop stops once var gets the value of 8)
'''
],
[
'''
How many starts will the following code send to the console?
i = 0
while i <= 3:
    i += 2
    print('*')
''',
'''
two
'''
],
[
'''
What is the output of the following code?
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c+d+e)
''',
'''
2 because c is 0 and d is 1 and e is 1
'''
],
[
'''
What is the output of the following code?
t = [[3-1 for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)
''',
'''
6
because t is a two dimensional list: [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
so it 3 + 2 + 1
'''
],
[
'''
How many hashes will the following snippet send to the console?
for i in range(1):
    print('#')
else:
    print('#')
''',
'''
two because the else statement is always triggered after the loop ends.
'''
],
[
'''
What is the output of the following code?
lst = [[1, 2, 3, 4] for i in range(2)]
print(lst[2][0])
''',
'''
error because in the outer dimesnion of the two-dimensional list
there is no index of 2, only 0 and 1
'''
],
[
'''
What value will be assigned to the x variable?
z = 10
y = 0
x = y < z and z > y or y > z and z < y
''',
'''
True
'''
],
[
'''
What is the output of the following code?
vals = [1, 2, 3]
vals.insert(0, 1)
del vals[1]
print(sum(vals))
''',
'''
6
because 1 will be inserted as first value of the list resulting in [1, 1, 1, 2] 
and the second value has been deleted resulting in [1, 2, 3]
'''
],
[
'''
What is the output of the following code?
x = 1
x = x == x
print(x)
''',
'''
True, because x == x is True
'''
],
[
'''
Which of the following sentences are true in regard of the following code?
nums = [1, 2, 3]
vals = nums[-1:-2]

a) nums and vals are of the same length
b) nums is longer than vals
c) vals is longer than nums
d) nums and vals are two different lists
''',
'''
b, d
d because it is no reference, vals is a new list
b because none of the elements of nums is copied into vals
'''
],
[
'''
Which of the following sentences are true in regard of the following code?
nums = [1, 2, 3]
vals = nums[0:2]

a) nums and vals are of the same length
b) nums is longer than vals
c) vals is longer than nums
d) nums and vals are two different lists
''',
'''
b, d
d because it is no reference, vals is a new list
b because the last element is excluded on copying the elements
'''
],
[
'''
Which of the following sentences are true in regard of the following code?
nums = [1, 2, 3]
vals = nums[0:3]

a) nums and vals are of the same length
b) nums is longer than vals
c) vals is longer than nums
d) nums and vals are two different lists
''',
'''
a, d
d because it is no reference, vals is a new list
a because all elements of nums get copied into vals
'''
],
[
'''
Which of the following sentences are true in regard of the following code?
nums = [1, 2, 3]
vals = nums[0:6]

a) an error will occur
b) nums and vals are of the same length
c) nums and vals are the same list
d) nums and vals are two different lists
''',
'''
b, d
d because it is no reference, vals is a new list
b because all elements of nums get copied into vals
'''
],
[
'''
How many hashes will the following code send to the console?
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print('#')
''',
'''
three
'''
],
]


mod_4_0 = [[],]

mod_4_1 = [
[
'What is a function?',
'A function is a block of code that performs a specific task when the function is called (invoked).'
],
[
'What is the purpose of functions?',
'make your code reusable, better organized, and more readable. Also for usage in OOP.'
],
[
'When does it make sense to write an own function?',
'''
If a particular fragment of the code would begin to appear more than once.
To isolate code (problems) to make the entire proigramm easier to read (decomposition).
Sharing the worka and sharing the responsibility among many developers.
To be implemented packed together in different modules.
'''
],
[
'Where do functions come from?',
'''
from Python itself (built-in)
preinstalled modules (to be imported)
user-defined (code)
'''
],
[
'Which keyword uses Python to announce defining a function?',
'def'
],
[
'Which syntax must a function have?',
'''
At least paranthesis directly after the function name (without space inbetween)
And at least colon after the paranthesis
A function needs at least one nested and indented instruction.
def functionnmame():
'''
],
[
'How can you use a function?',
'It must be invoced (called) to use it'
],
[
'''
What happens if you define a function like this: def hello() 
and afterwards you assign a value to hello like this: hello = 1
''',
'hello is not a function anymore and can not be called anymore. hello is now a variable (overwritten)'
],
[
'What happens when you try to invoke a function before you define it?',
'NameError'
],
[
'What happens if you try to pass a parameter to a function on calling, that cannot take a parameter in its definition?',
'TypeError'
],
[
'''
What will happen when you run the code below?
def hi():
    print("hi")
hi(5)
''',
'TypeError'
],
[
'''
Which statement about functions is true?
Parameters exist only inside functions in which they have been defined.
Assigning a value to the parameter is done at the time of the function's invocation.
''',
'Both'
],
[
'''
Complete the sentences:
parameters live _______ functions
arguments exist _______ functions
''',
'''
inside
outside
'''
],
[
'''
Which statement is true?
a) You cannot pass more arguments to a function, than there are paramenters defined in the function?
b) You cannot pass less arguments to a function, than there are paramenters defined in the function?
a) You can pass more arguments to a function, than there are paramenters defined in the function?
b) You can pass less arguments to a function, than there are paramenters defined in the function?
''',
'a, d (for example, optional parameters)'
],
[
'''
Which statement is true?
It's legal, and possible, to have the argument passed to a function, named the same as a function's parameter.
It's illegal, and impossible, to have a argument passed to a function, named the same as a function's parameter.
An argument passed to a function, must have a different name than the function's parameter.
An argument passed to a function, must have the same name as the function's parameter.
''',
'a'
],
[
'''
It's illegal, and impossible, to have a argument passed to a function, named the same as a function's parameter.
An argument passed to a function, must have a different name than the function's parameter.
An argument passed to a function, must have the same name as the function's parameter.
''',
'a'
],
[
'''
Which statement is true?
a) When you pass an argument to a function and the argument and the parameter have the same name, they have the same value and are the sam entity.
b) When you pass an argument to a function and the argument and the parameter have not the same name, they have the same value, but are not the same entity.
c) When you pass an argument to a function and the argument and the parameter have the same name, they have not the same value, but are the same entity.
d) When you pass an argument to a function and the argument and the parameter have not the same name, they have not the same value, and are not the same entity
''',
'b'
],
[
'How many parameters can a function have?',
'As many as you want.'
],
[
'What is shadowing?',
'If passed argument and parameter have the same name, they are still other entities.'
],
[
'What is positional parameter passing and what are positional arguments?',
'It means that argeuments will be taken by a function in the order they have been passed, independed of the parameter names.'
],
[
'What is keyword argumemnt passing?',
'''
Its is assigning the argument to the desired parameter name already on invoocation and passing both information to the function,
whereby the name of the parameter has to be defined in the functions paranthesis or an error will occur.
'''
],
]





mod_4_2 = [
[
'''
What will be the output of the following snippet?
def func(a, b):
    print(a, b)
func(b = "a", a = "b")
''',
'b a'
],
[
'''
What will be the output of the following snippet?
def func(a, b):
    print(b, a)
func(a = "a", b = "b")
''',
'b a'
],
[
'''
What will be the output of the following snippet?
def func(a, b):
    print(a, b)
func("a", "b")
''',
'a b'
],
[
'''
What will be the output of the following snippet?
def func(a, b):
    print(a, b)
func("b", "a")
''',
'b a'
],
[
'''
What will be the output of the following snippet?
def func(a = 'b', b = 'a'):
    print(a, b)
func('a', a = 'a')
''',
'TypeError: func() got multiple values for argument \'a\''
],
[
'''
def func(a = 'b', b = 'a'):
    print(a, b)
func(a = 'a', 'a')
''',
'SyntaxError: positional argument follows keyword argument'
],
[
'''
def func(a = 'b', b):
    print(a, b)
func(a = 'a', 'a')
''',
'SyntaxError: non-default argument follows default argument'
],
[
'''
def func(a, b = 'a'):
    print(a, b)
func('b', b = 'a')
''',
'b a'
],
[
'What do you have to take into account if you mix positional arguments and keyword arguments?',
'Positional arguments have to be passed before keyword arguments,\nso keyword arguments have to be passed last.'
],
[
'''
What will be the output of the following snippet?
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(b = 5, a = 6, 11)
''',
'Syntax error, because positional argument follows keyword argument (NOTE: POSITIONAL ARGUMENTS MUST BE FIRST)'
],
[
'''
What will be the output of the following snippet?
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(5, b = 6, c = 11)
''',
'22'
],
[
'How many values can you pass to one parameter at the same time?',
'one'
],
[
'What datatypes or objects can you pass to a function?',
'all (int, float, string, bool, dicts, lists, tuples, functions etc)'
],
[
'''
What will be the output of the following snippet?
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(5, a = 6, b = 11)
''',
'TypeError: because you cannot pass two arguments to one parameter'
],
[
'What do you have to take into account for predefined values or optional parameters?',
'''
Predefined values have to be set last in the order of parameters in the function definition.
NOTE: define normal parameters first and define predefined values last!!!!!!!
'''
],
[
'''
a = 1
b = 2
def func(a=0, b):
    print(a+b)
func(a, b)
''',
'''
SyntaxError: non-default argument follows default argument
Parameters with default values must always be last
'''
],
[
'''
a = 1
b = 2
def func(a, b):
    print(a+b)
func(a = 1, b)
''',
'''
SyntaxError: positional argument follows keyword argument
positional arguments must always be last
'''
],
[
'''
a = 1
b = 2
def func(a, b):
    print(a+b)
func(a, b = 3)
''',
'''
4
'''
],
[
'''
a = 1
b = 2
def func(b):
    print(a+b)
func(a, b = 3)
''',
'''
TypeError: func() got multiple values for argument 'b'
You cannot pass more arguments to a function then it has parameters
'''
],
[
'''
a = 1
b = 2
def func(a, b):
    print(a+b)
func(b = 3)
''',
'''
TypeError: func() missing 1 required positional argument: 'a'
You cannot pass less arguments to a function unless the missing ones have a default value as parameter
'''
],
[
'''
a = 1
b = 2
def func(b, a=1):
    print(a+b)
func(b = 3)
''',
'''
4
'''
],
]





mod_4_3 = [
[
'What happens when you use inside a function the keyword return without an expression?',
'''
Immediate termination of the function's execution and a return to the point of invocation.
No value will be passed by the return keyword if no expression is used.
'''
],
[
'''
Which statement is true?
a) using the return instruction is not obligatory
b) You have to use return in every function.
''',
'a'
],
[
'What happens when you use inside a function the keyword return with an expression?',
'''
Immediate termination of the function's execution and a return to the point of invocation
It will evaluate the expression's value and return it as the function's result.
'''
],
[
'''
What will be the result of the following snippet?
def func(a, b):
    c = a + b
    return c
x = func(1, 2)
print(x)
''',
'3'
],
[
'What is None?',
'''
None is a keyword. It is not a value. It is a state or result an an object can have.
When you try to process None you will get a runtime error, despite of a few exceptions.
'''
],
[
'When can None be used without a runtime error?',
'''
When you just assign it to a variable (or return it as a function's result).
When you compare it with a variable to diagnose its internal state.
'''
],
[
'What does a function return if the keyword return is not used?',
'None'
],
[
'''
Which statement is true?
A list may be a function result.
A list may be sent to a function as an argument.
''',
'both'
],
[
'''
def func(a = 1, b = 2, c = 3):
    print(a+b+c)
func([5, 4, 3])
''',
'TypeError: can only concatenate list (not "int") to list'
],
[
'''
What will be the output of the following snippet?
def list_sum(lst):
    s = 0    
    for elem in lst:
        s += elem
    return s
print(list_sum([5, 4, 3]))
''',
'12'
],
[
'''
What will be the output of the following snippet?
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print(list_sum(7))
''',
'TypeError: \'int\' object is not iterable'
],
[
'''
def lst_fun(n):
    lst = []
    for i in range(0, n):
        lst.insert(ß, i)
    return lst
print(lst_fun(7))
''',
'[6, 5, 4, 3, 2, 1, 0]'
],
[
'''
def lst_fun(n):
    lst = []
    for i in range(0, n):
        lst.insert(i, i)
    return lst
print(lst_fun(7))
''',
'[0, 1, 2, 3, 4, 5, 6]'
],
[
'''
def lst_fun(n):
    lst = []
    for i in range(0, n):
        lst.insert(i, n-i)
    return lst
print(lst_fun(7))
''',
'[7, 6, 5, 4, 3, 2, 1]'
],
[
'''
def lst_fun(n):
    lst = []
    for i in range(0, n):
        lst.insert(i-n, n-i)
    return lst
print(lst_fun(7))
''',
'[4, 3, 5, 2, 6, 1, 7]'
],
[
'''
def lst_fun(n):
    lst = []
    for i in range(0, n):
        lst.insert(n-i, i-n)
    return lst
print(lst_fun(7))
''',
'[-7, -1, -6, -2, -5, -3, -4]'
],
[
'''
What would you need to change in the following code to get this result? [7, 6, 5, 4, 3, 2, 1]
def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(i, i)
    return strange_list
print(strange_list_fun(7))
''',
'strange_list.insert(i, i+1)'
],
[
'''
What is the output of the following snippet?
def hi():
    return
    print("Hi!")
hi()
''',
'None'
],
[
'''
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5), end=', ')
print(is_int(5.0), end=', ')
print(is_int("5"), end=', ')
''',
'True, False, None'
],
[
'''
What is the output of the following snippet?
def _lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
print(_lst(11))
''',
'[0, 2, 4, 6, 8, 10]'
],
[
'''
def _lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num+2)
    return lst
print(_lst(12))
''',
'[2, 4, 6, 8, 10, 12]'
],
[
'What is the start value of the range() fucntion if no start value is given?',
'0'
],
[
'What happens, if you change the conrol variable of a for loop within the loop?',
'The control variable won\'t change the continuation of the loop.\n the value will be reset in the next step of the loop. '
],
[
'''
What is the output of the following snippet?
for i in range(4):
    print(i, end='')
    i += 1
    print(i, end ='')
''',
'01122334'
],
[
'''
for i in range(4):
    i += 1
    print(i, end ='')
    i += i
    print(i, end ='')
''',
'12243648'
],
[
'''
What is the output of the following snippet?
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
''',
'[1, 4, 9, 16, 25]'
],
]




mod_4_4 = [
[
'What is a scope of a name?',
'It is the part of a code where the name is properly recognizable, so the name itself (e.g. variable name)'
],
[
'What is the scope of a function\'s parameter?',
'The function itself, because the parameter is inaccessible outside the function'
],
[
'What does it mean when a variable from outside a function is shadowed inside the function?',
'Its value from outside the function can be addresed from inside the function (but not vice versa)'
],
[
'What is the difference between a variable of same name inside and outside a function?',
''''
The variable inside the function (local variable)shadows the value of the variable outside the function (global variable)..
Once you change variables value inside the function, this does not affect the variable outside the function.
So the two variables are different variables.
'''
],
[
'What is the keyword global?',
'''
It can extend a variable\'s scope to outside of the functions\' body.
If the variable inside the function already exists outside the function, the variable outside will be used inside the fucntion.
You can change the value of the global variable inside and outside of the function.
'''
],
[
'How is the keyword global used regarding syntax and placing?',
'''
global variable1
global variable1, variable2, ...
Inside of a function the global keyword must be used before assigning a value to the variable.
'''
],
[
'Does a change of the parameter value inside the function affect the passed argument to the function?',
'No. To change the argument you have to return a value and assign the function invocation to the arguments variable name.'
],
[
'''
What will be the output of the follwing snippet?
def func(list_1):
    print(list_1, end="")
    print(list_2, end="")
    list_1 = [0, 1]
    print(list_1, end="")
    print(list_2, end="")
list_2 = [2, 3]
func(list_2)
print(list_2, end="")
''',
'[2, 3][2, 3][0, 1][2, 3][2, 3]'
],
[
'''
What will be the output of the follwing snippet?
def func():
    global list_1
    print(list_1, end="")
    print(list_2, end="")
    list_1 = [0, 1]
    print(list_1, end="")
    print(list_2, end="")
list_2 = [2, 3]
func()
print(list_2, end="")
''',
'NameError: name \'list_1\' is not defined'
],
[
'''
What will be the output of the follwing snippet?
def func():
    print(list_1, end="")
    print(list_2, end="")
    list_1 = [0, 1]
    print(list_1, end="")
    print(list_2, end="")
list_1 = [2, 3]
list_2 = [2, 3]
func()
print(list_1, end="")
''',
'UnboundLocalError: local variable \'list_1\' referenced before assignment'
],
[
'''
What will be the output of the follwing snippet?
def func(list_2):
    global list_1
    print(list_1, end="")
    print(list_2, end="")
    list_1 = [0, 1]
    print(list_1, end="")
    print(list_2, end="")
list_1 = [2, 3]
list_2 = [2, 3]
func(list_2)
print(list_1, end="")
''',
'[2, 3][2, 3][0, 1][2, 3][0, 1]'
],
[
'''
What will be the output of the follwing snippet?
def func(list_2, list_1):
    print(list_1, end="")
    print(list_2, end="")
    list_1 = [2, 3]
    print(list_1, end="")
    print(list_2, end="")
list_1 = [0, 1]
list_2 = [2, 3]
func(list_1, list_2)
print(list_1, end="")
''',
'[2, 3][0, 1][2, 3][0, 1][0, 1]'
],
[
'''
What will be the output of the follwing snippet?
def func():
    global x
    x = 2
x= 1
func()
print(x, end="")
''',
'2'
],
[
'''
What will be the output of the follwing snippet?
def func():
    x = 2
    return x
x= 1
func()
print(x, end="")
''',
'1'
],
[
'''
What will be the output of the follwing snippet?
def func():
    x = 2
    return x
x= 1
x = func()
print(x, end="")
''',
'2'
],
[
'''
What will be the output of the follwing snippet?
def func():
    print(x, end="")
    x = 2
x= 1
func()
print(x, end="")
''',
'UnboundLocalError: local variable \'x\' referenced before assignment'
],
[
'''
What will be the output of the follwing snippet?
var = 2
def mult(x):
    return x * var
print(mult(7))
''',
'14'
],
[
'''
What will be the output of the follwing snippet?
def mult(x):
    var = 5
    return x * var
print(mult(7))
''',
'35'
],
[
'''
What will be the output of the follwing snippet?
def mult(x):
    var = 7
    return x * var
var = 3
print(mult(7))
''',
'49, because the value 3 is not passed'
],
[
'''
What will be the output of the follwing snippet?
def adding(x):
    var = 7
    return x + var
print(var)
''',
'NameError, because variable is not defined outside the function but called outside the function.'
],
[
'''
What will be the output of the follwing snippet?
def adding(x):
    global var
    var = 7
    return x + var
print(var)
''',
'NameError: name \'var\' is not defined (var is passed in function call before assigning a value to it)'
],
[
'''
def adding(var):
    global var
    var = 7
    return x + var
var = 1
print(adding(var))
''',
'SyntaxError: name \'var\' is parameter and global (paramters can not be declared as global)'
],
[
'''
def adding(var):
    var = 7
    return var
var = 1
print(adding(var))
''',
'7, because the function return is printed'
],
[
'''
var = 2
def func():
    global var
    var = 5
    return var
print(var)
''',
'2, because function has not been called'
],
[
'''
def mult(x):
    var = 7
    return x * var
var = 3
print(mult(var))
''',
'21'
],
[
'''
What will be the output of the follwing snippet?
var = 2
def func():
    global var
    var = 5
func()
print(var)
''',
'5, because the value of var has been changed globally, '
],
[
'''
What will be the output of the follwing snippet?
def message():
    alt = 1
    print("Hello, World!")
print(alt)
''',
'NameError: name \'alt\' is not defined (because there is no parameter)'
],
[
'''
What will be the output of the follwing snippet?
a = 1
def fun():
    a = 2
    print(a, end="")
fun()
print(a, end="")
''',
'21 (because a are two different variables)'
],
[
'''
What will be the output of the follwing snippet?
a = 1
def fun():
    global a
    a = 2
    print(a, end="")
fun()
a = 3
print(a, end="")
''',
'23 (because the same variable has been printed with different values)'
],
[
'''
What will be the output of the follwing snippet?
a = 1
def fun():
    global a
    a = 2
    print(a, end ="")
a = 3
fun()
print(a, end ="")
''',
'22 (because the same variable has been printed two times without changing its value)'
],
]



mod_4_5 = [
[
'''
What is the output of the following snippet?
def bmi(weight, height):
    return weight / height ** 2
print(bmi(80, 2.0))
''',
'20.0'
],
[
'What does it mean if you use \ outside a String and at the end of a line?',
'''
That Python should continue reading the code of one line on the next line.
This way you can put code of one line in several lines. For example to avoid too long lines.
'''
],
[
'''
What is the output of the following snippet?
def is_a_triangle(a, b, c):
    if a + b <= c or \
    b + c <= a or \
    c + a <= b:
        return False
    else:
        return True
print(is_a_triangle(1, 1, 1))
''',
'True'
],
[
'''
What is the output of the following snippet?
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
print(is_a_triangle(1, 2, 1))
''',
'False'
],
[
'What are factorials?',
'Their result is equal to the product of all natural numbers from one up to its argument.'
],
[
'How to define a fractorial?',
'''
The final number of the arithemical row ending with an exclamation mark.
e.g. 
1! = 1
n! = 1 * 2 * 3 ... * n-1
'''
],
[
'What is recursion?',
'It is (e.g.) a technique where the function invoces itself.'
],
[
'''
What will happen when you attempt to run the following snippet and why?
def factorial(n):
    return n * factorial(n - 1)
print(factorial(4))
''',
'Python raises an exception to stop the endless loop, because the function recurses itself,\nbut has no termination condition.'
],
[
'''
What will happen when you attempt to run the following snippet and why?
def fun(a):
    if a > 5:
        return 3
    else:
        print(a, end=", ")
        return a + fun(a + 1)
fun(1)
''',
'''
1, 2, 3, 4, 5, because the function invokes it self
until the termination conditions is met (recursion)
'''
],
[
'''
def func(b, a = 1):
    if b > 3:
        return b
    else:
        a += 1
        func(a)
    
print(func(1))
''',
'''
RecursionError: maximum recursion depth exceeded in comparison
'''
],
[
'''
def func(b):
    if b > 3:
        return b
    else:
        b += 1
        func(b) 
print(func(1))

''',
'''
None (because when the last function recursion is finsihed there is no return)
'''
],
[
'''
def func(b):
    if b > 3:
        return b
    else:
        b += 1
        return func(b)
print(func(1))
''',
'''
4
'''
],
[
'''
def func(b):
    if b > 2:
        return b
    else:
        b += 1
        return func(b)*func(b)
print(func(1))
''',
'''
81 (because after the recursions of the first func(b) is done
there are two open second func(b) that will be multiplied therefore you have 3*3*3)
'''
],
]



mod_4_6 = [
[
'What are sequence types?',
'''
A sequence type is a type of data in Python which is able to store more than one value.
(or less than one, as a sequence may be empty), 
These values can be sequentially browsed, element by element
(e.g. by the for loop)
'''
],
[
'Which sign is used to seperate arguments of any sequence type?',
'comma'
],
[
'Indicies or keys of any sequence types are always called by which syntax?',
'[]'
],
[
'What is mutable data?',
'Data that can be freely changed during the programm execution. (in situ = in position)'
],
[
'What is immmutable data?',
'Data that can be not be changed during the programm execution. (e.g. Tuples)'
],
[
'What is a tuple?',
'''
A tuple is an immutable sequence type. It can behave like a list,
but it cannot be modified in situ, (with two exceptions).
'You can merge and multiply the amount of elements of tuples.
And you can overwrite entire tuples (not a change to the tuple itself)'
'''
],
[
'There are two ways to create tuples syntactically. Which? Also give two examples:',
'''
With and without parantheis, but its values have to be seperated by commas.
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1, 2, 4, 8
'''
],
[
'Please write a tuple with only one element:',
'tuple = (1,)'
],
[
'''
What is the difference between a and b (despite their name)?
a = 1,
b = 1
''',
'a is a tuple and b is a variable'
],
[
'''
What is the output of the following snippet?
my_tuple = (1, 10, 100, 1000)
print(my_tuple[:-2])
print(my_tuple[-2])
''',
'''
1, 10 (because index -2 is excluded in adressing it as end of the range)
100
'''
],
[
'When you use a slice, is ending element included or excluded?',
'excluded'
],
[
'''
What is the output of the following snippet?
a = (1, 10, 100, 1000)
a.append(10000)
print(a)
''',
'AttributeError: \'tuple\' object has no attribute \'append\''
],
[
'''
What is the output of the following snippet?
a = (1, 10, 100, 1000)
del a[0]
print(a)
''',
'TypeError: \'tuple\' object doesn\'t support item deletion'
],
[
'''
What is the output of the following snippet?
a = [1, 10, 100, 1000]
del a[0:3]
print(a)
''',
'1000'
],
[
'''
What is the output of the following snippet?
a = 1, 10, 100, 1000
a.pop(1)
print(a)
''',
'AttributeError: \'tuple\' object has no attribute \'pop\''
],
[
'''
What is the output of the following snippet?
a = 1, 10, 100, 1000
a = 25
print(a)
''',
'25, because the tuple itself is changed into a variable.'
],
[
'You can not change a tuples values or length, but you can overwrote the entire tuple. Is that true or false?',
'true'
],
[
'''
What is the output of the following snippet?
a, b, c, d = 1, 10, 100, 1000
a = 25
print(a)
''',
'AttributeError: \'int\' object has no attribute \'pop\''
],
[
'''
What is the output of the following snippet?
a = 1, 10, 100, 1000
a = 25,
a[0] = 5
print(a)
''',
'TypeError: \'tuple\' object does not support item assignment'
],
[
'''
What is the output of the following snippet?
a = 1, 10, 100, 1000
a = 25.
a[0] = 5
print(a)
''',
'TypeError: \'float\' object does not support item assignment'
],
[
'''
What is the output of the following snippet?
a = 5.
b = 10,
c = a + b
print(c)
''',
'TypeError: can only concatenate tuple (not "float") to tuple'
],
[
'''
What is the output of the following snippet?
a = 5.
b = int(10,)
c = a + b
print(c)
''',
'15.0'
],
[
'You cannot change tuples, but there are two exceptions. Which?',
'You can merge and multiply the amount of elements of tuples.'
],
[
'''
What will be the output of the following snippet and why?
t1 = 1, 2, 3
t2 = 4, 5, 6
t = t1 + t2
print(t)
''',
'(1, 2, 3, 4, 5, 6) because the tuple has been merged'
],
[
'''
What will be the output of the following snippet and why?
t1 = 1
t = t1 + (2, 3, 4, 5, 6)
print(t)
''',
'''
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
Because t1 is a variable and not a tuple
'''
],
[
'''
What will be the output of the following snippet and why?
t1 = 1,
t = t1 + (2, 3, 4, 5, 6)
print(t)
''',
'(1, 2, 3, 4, 5, 6) because the tuple has been merged'
],
[
'''
What will be the output of the following snippet and why?
t1 = 1, 2, 3
t2 = 2,
t = t1 * t2
print(t)
''',
'''
TypeError: can't multiply sequence by non-int of type 'tuple'
Because t2 is a tuple and you cannot only multiply tuple elements with integers
'''
],
[
'''
What will be the output of the following snippet and why?
t1 = 1, 2, 3
t2 = 2
t = t1 * t2
print(t)
''',
'(1, 2, 3, 1, 2, 3) because the tuple elements have been multiplied.'
],
[
'''
t1 = 1, 2, 3
t2 = 2
t1[1] * t2
t = t1 * t2
print(t)
''',
'(1, 2, 3, 1, 2, 3) because you cannot change a tuples element (entire tuple has been multiplied instead (bad practice))'
],
[
'''
What will be the output of the following snippet?
var = 123
t1 = (1, )
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)
''',
'(2,) (3, 123) (1,)'
],
[
'Is a dictionary a sequence type?',
'No (due its unordered nature)'
],
[
'Write a dictionary with the key \'name\' and the value \'Peter\':',
'dict = {\'name\' : \'Peter\'}'
],
[
'''
What will be the output of the following snippet in Python 3.5?
dict = {"cat": "Katze", "dog": "Hund", "horse": "Pferd"}
print(dict)
''',
'''
Don't try to fulfill this task IF you are using Python Version lower than 3.6, 
because dictionaries don't have orders or they are complety out of expectation below this version.
'''
],
[
'''
What will be the output of the following snippet in Python 3.6?
dict = {"cat": "Katze", "dog": "Hund", "horse": "Pferd"}
print(dict)
''',
'{"cat": "Katze", "dog": "Hund", "horse": "Pferd"}'
],
[
'''
What will be the output of the following snippet?
dict = {"cat": "Katze", "dog": "Hund", "horse": "Pferd"}
dict.sort()
print(dict)
''',
'''
AttributeError: 'dict' object has no attribute 'sort'
Because dicts cannot be sorted by code.
'''
],
[
'''
What will be the output of the following snippet?
dict = {"cat": "Katze", "dog": "Hund", "horse": "Pferd"}
print(dict[1])
''',
'KeyError: 1 (because dicts dont have indicies).'
],
[
'''
What will be the output of the folliwng snippet?
dict = {'1': "Katze", '2': "Hund", "horse": "Pferd"}
print(dict[1])
''',
'''
KeyError: 1
Because there is no integer key named 1, only a string key named '1
'''
],
[
'''
What will be the output of the following snippet?
dict = {1: "Katze", 2: "Hund", "horse": "Pferd"}
print(dict[1])
''',
'Katze'
],
[
'''
What will be the output of the folliwng snippet?
dict = {1: "Katze", 2: "Hund", "Horse": "Pferd"}
print(dict['horse'])
''',
'KeyError: \'horse\' (because keys are case-sensitive)'
],
[
'''
What will be the output of the following snippet?
dict = {1: "Katze", 2: "Hund", "Horse": "Pferd"}
print(dict['cow'])
''',
'KeyError: \'cow\' (because there is no key named \'cow\')'
],
[
'What are hanging idents?',
'Writing each element of an array not into one line of code, but writing one element per line of code.'
],
[
'''
What will be the output of the following snippet?
dictionary = {
    "cat": "chat", 
    "dog": "chien", 
    "horse": "cheval"}
words = ['cat', 'lion', 'horse']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
''',
'''
cat -> chat
lion is not in dictionary
horse -> cheval
'''
],
[
'Can dictionaries be browsed using the for loop?',
'Not directly. But with a little work-around, the .key() method'
],
[
'How for example and why can dictionaries be browsed using iteration?',
'''
using the .key() method as follows
for key in dictionary.keys():
It will create an iterable object out of the keys.
'''
],
[
'What is the .popitem() method used for?',
'''
To delete the last element in a dictionary.
It only works for dictionaries.
'''
],
[
'How can you sort a ditcionary?',
'''
for key in sorted(dictionary.keys()):
It will create an iterable object out of the keys.
'''
],
[
'''
What will be the output of the following snippet and why?
dict = {"a": "A", "b": "B", "c": "C"}
for key in sorted(dict.keys(), reverse = True):
    print(dict[key], end="")
''',
'''
What will be the output of the following snippet an why?
dict = {"a": "A", "b": "B", "c": "C"}
for key in sorted(dict.keys(), reverse = True):
    print(dict[key], end="")
CBA (because the keys have been sorted alphabetically reverse)
'''
],
[
'''
What will be the output of the folliwng snippet and why?
dict = {"a": "C", "b": "A", "c" : "B"}
for key in sorted(dict.keys()):
    print(dict[key], end="")
''',
'CAB (because the keys have been sorted alphabetically)'
],
[
'''
What will be the output of the following snippet and why?
dict = {"c": "A", "b": "C", "a" : "B"}
for key in sorted(dict.keys(), reverse = True):
    print(dict[key], end="")
''',
'ACB (because the keys have been sorted alphabetically reverse)'
],
[
'''
What will be the output of the folliwng snippet an why?
dict = {"a": "A", "b": "B"}
for i in dict.values():
    print(i, end="")
''',
'AB'
],
[
'''
What will be the output of the following snippet?
dict = {"a": "A", "b": "B"}
for i in dict:
    print(i, end="")
''',
'ab'
],
[
'''
What will be the output of the folliwng snippet an why?
dict = {"a": "A", "b": "B"}
for i in dict:
    print(dict[i], end='')
''',
'AB'
],
[
'''
What will be the output of the following snippet an why?
dict = {a: "A", b: "B"}
dict[a] = 'X'
print(dict[a])
''',
'NameError: name \'a\' is not defined (the indicies in the dict are undefined variables)'
],
[
'''
dict = {"a": "A", "b": "B"}
dict[a] = 'X'
print(dict[a])
''',
'NameError: name \'a\' is not defined (calling a key always needs quotes)'
],
[
'''
What will be the output of the following snippet an why?
dict = {"a": "A", "b": "B"}
dict["a"] = 'X'
print(dict["a"])
''',
'X'
],
[
'''
What will be the output of the following snippet an why?
dict = {"a": "A", "b": "B"}
dict.update('c' : 'C')
print(dict['c'])
''',
'SyntaxError (The {} are missing within the update() method)'
],
[
'''
What will be the output of the following snippet an why?
dict = {"a": "A", "b": "B"}
dict.update{'c' : 'C'}
print(dict['c'])
''',
'SyntaxError (The paranthesis of the .update() method are missing)'
],
[
'''
What will be the output of the following snippet and why?
dict = {"a": "A", "b": "B"}
dict.update({'c' : 'C'})
print(dict['c'])
''',
'C'
],
[
'''
What will be the output of the following snippet and why??
dict = {"a": "A", "b": "B"}
dict['c'] = 'C'
print(dict['c'])
''',
'C (because a new elemnt has been created)'
],
[
'''
What will be the output of the following snippet an why?
dict = {"a": "A", "b": "B"}
del dict['b']
print(dict['b'])
KeyError: 'b'
''',
'KeyError: \'b\' (because b has been deleted so there is no such key )'
],
[
'''
What will be the output of the following snippet an why?
dict = {"a": "A", "b": "B", "c" : "C"}
del dict['b']
dict["b"] = "B"
print(dict)
''',
'''
In Versions lower than Python 3.6 you cannot give an answer, as dicts are not ordered
{'a': 'A', 'c': 'C', 'b': 'B'} in Versions higher or equal Python 3.6
'''
],
[
'''
What will be the output of the following snippet an why?
dict = ("A", "B")
dict.popitem()
print(dict)
''',
'AttributeError: \'tuple\' object has no attribute \'popitem\''
],
[
'''
What will be the output of the following snippet an why?
dict = ["A", "B"]
dict.popitem()
print(dict)
''',
'AttributeError: \'list\' object has no attribute \'popitem\''
],
[
'''
What will be the output of the following snippet an why?
dict = {"A", "B"}
dict.popitem()
print(dict)
''',
'AttributeError: \'set\' object has no attribute \'popitem\''
],
[
'''
What will be the output of the following snippet an why?
dict = {"a": "A", "b": "B"}
dict.popitem()
print(dict)
''',
'''
{'a': 'A'} because when using .popitem() the last item in the dict will be deleted.
'''
],
[
'''
What will be the output of the folliwng snippet an why?
dict = {"a": "A", "b": "B"}
dict.popitem("a")
print(dict)
''',
'TypeError: popitem() takes no arguments (1 given)'
],
[
'Can you nest tuples into sets?',
'Yes'
],
[
'Can you nest sets into tuples?',
'Yes'
],
[
'Can you nest tuples into lists?',
'Yes'
],
[
'Can you nest lists into sets?',
'No'
],
[
'Can you nest lists into tuples?',
'Yes'
],
[
'Can you nest tuples into dictionaries?',
'Yes'
],
[
'Can you nest dictionaries into tuples?',
'Yes'
],
[
'Can you nest dictionaries into sets?',
'No'
],
[
'Can you nest dictionaries into lists?',
'Yes'
],
[
'Can you nest sets into sets?',
'No'
],
[
'Can you nest tuples into tuples?',
'Yes'
],
[
'Can you nest lists into lists?',
'Yes'
],
[
'Can you nest dictionaries into dictionaries?',
'Yes'
],
[
'You cannot nest any sequences or dicts into a set: true or false?',
'true with the exception of tuples. So you can nest tuples into sets'
],
[
'''
You can nest any sequence type or dicts into any other sequence type
or dicts unless it is nested into a set: true or false?
''',
'true, but you can next tuples into sets'
],
[
'''
What will be the output of the following snippet an why?
dict = {'a' : 'A', 'b' : (1, 2, 3)}
print(dict['a'], end=", ")
print(dict['b'], end=", ")
''',
'''
A, (1, 2, 3),
Because it is a tuple inside a dictionary
'''
],
[
'''
What will be the output of the following snippet an why?
dict = {'a' : 'A', 'b' : ['1', '2', '3']}
print(dict['a'], end=", ")
print(dict['b'], end=", ")
''',
'''
A, ['1', '2', '3'],
Because it is a list inside a dictionary
'''
],
[
'''
What will be the output of the following snippet an why?
dict = {'a' : 'A', 'b' : {'1', '2', '3'}}
print(dict['a'], end=", ")
print(dict['b'], end=", ")
''',
'''
A, {'3', '1', '2'},  
Because it is a set inside a dictionary
'''
],
[
'''
What will be the output of the following snippet an why?
dict = {'a' : 'A', 'b' : {'a' : '1', 'b' : '2', 'c' : '3'}}
print(dict['a'], end=", ")
print(dict['b'], end=", ")
''',
'''
A, {'a': '1', 'b': '2', 'c': '3'},
Because it is a dictionary inside a dictionary
'''
],
[
'''
What will be the output of the following snippet an why?
dict = {1, 2, {'a' : '3', 'b' : '2', 'c' : '4'}}
print(dict['a'], end=", ")
print(dict['b'], end=", ")

''',
'TypeError: unhashable type: \'dict\' (because you cannot nest a sequence into a set)'
],
[
'''
What will be the output of the following snippet an why?
dict = {1, 2, [3, 4]}
print(dict['a'], end=", ")
print(dict['b'], end=", ")
''',
'TypeError: unhashable type: \'list\' (because you cannot nest a sequence into a set)'
],
[
'''
What will be the output of the following snippet an why?
dict = {1, 2, {3, 4}}
print(dict['a'], end=", ")
print(dict['b'], end=", ")
''',
'TypeError: unhashable type: \'set\' (because you cannot nest a sequence into a set)'
],
[
'What data types can tuples contain? (mention at least 6)',
'int, float, bool, string, tuple, list, dict, set '
],
[
'What data types can sets contain? (mention at least 3)',
'int, float, bool, string'
],
[
'Can you convert other data type into a tuple?',
'Yes, some.'
],
[
'Which data types can be converted into a tuple?',
'strings, lists, sets, ranges and partially dicts (not int, not float, not bool)'
],
[
'How can you convert data into a tuple?',
'using the function tuple() and give the data as argument'
],
[
'''
What will be the output of the following snippet an why?
a = ['a', 'b', 'c']
a = tuple(a)
print(a)
''',
'(\'a\', \'b\', \'c\'), because a list has been converted into a tuple'
],
[
'''
What will be the output of the following snippet an why?
a = 1
a = tuple(a)
print(a)
''',
'''
TypeError: 'int' object is not iterable
because a single integer cannot be converted into a tuple
'''
],
[
'''
What will be the output of the following snippet an why?
a = '1'
a = tuple(a)
print(a)
''',
'(\'1\',), because a string has been converted into a tuple'
],
[
'''
What will be the output of the following snippet an why?
a = range(1, 3)
a = tuple(a)
print(a)
''',
'''
(1, 2), because a range has been converted into a tuple
(last range element excluded)
'''
],
[
'''
What will be the output of the following snippet an why?
a = {'1', '2'}
a = tuple(a)
print(a)
''',
'(\'1\', \'2\'), because a set has been converted into a tuple'
],
[
'''
What will be the output of the following snippet an why?
a = {'a' : '1','b' : '2'}
a = tuple(a)
print(a)
''',
'order not sure, but dict has been converted into a tuple (only keys)'
],
[
'''
What will be the output of the following snippet an why?
a = 1.0
a = tuple(a)
print(a)
''',
'''
TypeError: 'float' object is not iterable
because a single float cannot be converted into a tuple
'''
],
[
'What data types can a list contain? (mention at least 6)',
'int, float, bool, string, tuple, list, dict, set'
],
[
'Can you convert other data type into a list?',
'Yes, some.'
],
[
'Which other data types can you convert into a list?',
'strings, tuples, sets, ranges, partially dicts (not int, not float, not bool)'
],
[
'''
What will be the output of the following snippet an why?
a = 1, 2, 3
a = list(a)
print(a)
''',
'[1, 2, 3] because a tuple has been converted into a list'
],
[
'''
What will be the output of the following snippet an why?
a = {1, 2, 3}
a = list(a)
print(a)
''',
'[1, 2, 3] because a set has been converted into a list'
],
[
'''
What will be the output of the following snippet an why?
a = range(1, 4)
a = list(a)
print(a)
''',
'''
[1, 2, 3] because a range has been converted into a list
(last range element excluded)
'''
],
[
'''
What will be the output of the following snippet an why?
a = 1
a = tuple(a)
print(a)
''',
'''
TypeError: 'int' object is not iterable
because a single int cannot be converted into a list
'''
],
[
'''
What will be the output of the following snippet an why?
a = '1'
a = tuple(a)
print(a)
''',
'[\'1\'], because a string has been converted into a list'
],
[
'''
What will be the output of the following snippet an why?
a = {'a' : 1, 'b' : 2, 'c' : 3}
a = list(a)
print(a)
''',
'''
'order not sure, but dict has been converted into a set (only keys)'
'''
],
[
'''
What will be the output of the following snippet an why?
a = 1.0
a = tuple(a)
print(a)
''',
'''
TypeError: 'float' object is not iterable
because a single float cannot be converted into a list
'''
],
[
'What data types can a set contain? (mention at least 4)',
'int, float, bool, string, tuple'
],
[
'Can you convert other data type into a set?',
'Yes, some.'
],
[
'Which other data types can you convert into a set?',
'strings, lists, tuples, ranges, partially dicts (not int, not float, not bool)'
],
[
'''
What will be the output of the following snippet an why?
a = 1
a = set(a)
print(a)
''',
'''
print(a)
TypeError: 'int' object is not iterable
because a single int cannot be converted into a set
'''
],
[
'''
What will be the output of the following snippet an why?
a = '1'
a = set(a)
print(a)
''',
'{\'1\'}, because a string has been converted into a set'
],
[
'''
What will be the output of the following snippet an why?
a = 1, 2, 3
a = set(a)
print(a)
''',
'{1, 2, 3}, because a tuple has been converted into a set'
],
[
'''
What will be the output of the following snippet an why?
a = {'a' : 1, 'b' : 2, 'c' : 3}
a = set(a)
print(a)
''',
'''
'order not sure, but dict has been converted into a set (only keys)'
'''
],
[
'''
What will be the output of the following snippet an why?
a = [1, 2, 3]
a = set(a)
print(a)
''',
'{1, 2, 3}, becaue a list has been converted into a set'
],
[
'''
Can you convert other data types into a dictionary?
''',
'''
Only if the format is correct, for examples json files
'''
],
[
'''
What will be the output of the following snippet an why?
a = [1, 2, 3]
a = dict(a)
print(a)
''',
'''
TypeError: cannot convert dictionary update sequence element #0 to a sequence
Because you cannot convert a list into a dict
'''
],
[
'''
What will be the output of the following snippet an why?
a = 1, 2, 3
a = dict(a)
print(a)
''',
'''
TypeError: cannot convert dictionary update sequence element #0 to a sequence
Because you cannot convert a tuple into a dict
'''
],
[
'''
What will be the output of the following snippet an why?
a = {1, 2, 3}
a = dict(a)
print(a)
''',
'''
TypeError: cannot convert dictionary update sequence element #0 to a sequence
Because you cannot convert a set into a dict
'''
],
[
'''
What will be the output of the following snippet an why?
a = '1'
a = dict(a)
print(a)
''',
'''
ValueError: dictionary update sequence element #0 has length 1; 2 is required
Because you cannot convert a single string into a dict
'''
],
[
'''
What will be the output of the following snippet an why?
a = 1
a = dict(a)
print(a)
''',
'''
TypeError: 'int' object is not iterable
Because you cannot convert a int string into a dict
'''
],
[
'In which ways can you access an element of a dictionary?',
'using brackets[] or using .get() method'
],
[
'''
What will be the output of the following snippet an why?
a = {'a' : 1, 'b' : 2, 'c' : 3}
print(a.get('b'))
''',
'2'
],
[
'Does the .insert() method work for dictionaries?',
'No'
],
[
'How do you insert new data to a dictionary?',
'using the .update() method or brackets[]'
],
[
'How can you loop through a dictionary?',
'using the .items method or brackets[]'
],
[
'''
What will be the output of the following snippet?
x = {
    "a": "1",
    "b": "2",
    "c": "3"
    }
for key, value in x.items():
    print(key, ":", value, end=", ")
''',
'a : 1, b : 2, c : 3, '
],
[
'''
What will be the output of the following snippet and why?
x = {
    "a": "1",
    "b": "2",
    "c": "3"
    }
for i in x:
    for j in i:
        print(i+' : '+j, end=", ")
''',
'''
a : a, b : b, c : c,
because instead of x[i] there is only i in the second loop head.
This means the reference to the key is missing and the values cannot be displayed,
Therefore only the keys are displayed.
In other words: The value of i is a literal and not an iterable item.
'''
],
[
'''
What will be the output of the following snippet and why?
x = {
    "a": "123",
    "b": "456",
    "c": "789"
    }
for i in x.values():
    for j in i:
        print(j, end=", ")
''',
'''
1, 2, 3, 4, 5, 6, 7, 8, 9,
because in the second loop we are iterating through the strings characters
'''
],
[
'''
What will be the output of the following snippet and why?
x = {
    "a": "1",
    "b": "2",
    "c": "3"
    }
for i in x:
    for j in x[i]:
        print(i+' : '+j, end=", ")
''',
'''a : 1, b : 2, c : 3, 
because this way we output the keys and the values
'''
],
[
'''
What will be the output of the following snippet?
x = {
    "a": "1",
    "b": "2",
    "c": "3"
    }
for i in x:
    for j in x[i]:
        print(x[i], end=", ")
''',
'''
1, 2, 3
because this way we only output the values
'''
],
[
'How to check if a value is inside a dictionary?',
'By looping through the keys and checking with the key word in during each loopstep,\nif the value is in side the current key.'
],
[
'''
What will be the output of the following snippet?
x = {
    "a": "1",
    "b": "2",
    "c": "3"
    }
for i in x:
    if "1" in i:
        print(True)
''',
'''
No result because the dict has no key named '1'
We have only checked the keys not the values.
'''
],
[
'''
What will be the output of the following snippet?
x = {
    "a": "1",
    "b": "2",
    "c": "3"
    }
for i in x:
    if "1" in x[i]:
        print(True)
''',
'True'
],
[
'''
What will be the output of the following snippet?
x = (1, 2, 3)
print(x[2])
''',
'3'
],
[
'How can you unpack a tuple?',
'''
By assigning the tuple to variables, whereby the amount of variables
has to be exactly the same as there are elements in the tuple.
'''
],
[
'''
What will be the output of the following snippet?
x = 1, 2, 3
a, b, c, d = x
print(a * b * c)
''',
'ValueError: not enough values to unpack (expected 4, got 3)'
],
[
'''
What will be the output of the following snippet?
x = 1, 2, 3, 4
a, b, c = x
print(a * b * c)
''',
'ValueError: too many values to unpack (expected 3)'
],
[
'''
What will be the output of the following snippet?
x = 1, 2, 3
a, b, c = x
print(a * b * c)
''',
'6'
],
[
'''
What will be the output of the following snippet?
x = 'c', 'b', 'a'
c, b, a = x
print(a, b, c)
''',
'a b c'
],
[
'''
What will be the output of the following snippet?
x = 'a', 'b', 'c'
c, b, a = x
print(a, b, c)
''',
'c b a'
],
[
'How can you find duplicates in a sequence?',
'''
By using the count() method and using the value value u seacrh for so for example.count(17)
Note: This will find out how many times the number 17 is in the sequence
'''
],
[
'For which data types does the count() method work?',
'tuples, lists, ranges'
],
[
'''
What will be the output of the following snippet?
a = {1, 2, 3, 3, 4, 5, 6, 2, 7, 3, 8, 9}
b = a.count(3)
print(b)
''',
'''
AttributeError: 'set' object has no attribute 'count'
Because counting does not work for sets with the .count() method
'''
],
[
'''
What will be the output of the following snippet?
a = [1, 2, 3, 3, 4, 5, 6, 2, 7, 3, 8, 9]
b = a.count(3)
print(b)
''',
'3, because the number 3 is in the list 3 times'
],
[
'''
What will be the output of the following snippet?
a = range(1, 10)
b = a.count(3)
print(b)
''',
'1, because the number 3 is in the range 1 time'
],
[
'''
What will be the output of the following snippet?
a = range(1, 10)
b = a.count(10)
print(b)
''',
'0, because the number 10 is not in the range (range end excluded)'
],
[
'''
Add 2 lines of code to merge both dictionaries:
a = {'a': '1', 'b': '2'}
b = {'c': '3', 'd': '4'}
c = {}
''',
'''
for item in (a, b):
    c.update(item)
'''
],
[
'''
What will be the output of the following snippet?
a = {'a': '1', 'b': '2'}
b = {'b': '2', 'c': '3'}
c = {}
for item in (a, b):
    c.update(item)
print(c)
''',
'''
{\'a\': \'1\', \'b\': \'2\', \'c\': \'3\'}
because the key 'b' is double, the key 'b' in dict b will be ignored on merging.
'''
],
[
'''
What will be the output of the following snippet?
a = [1, 2]
b = [3, 4]
c = []
for item in (a, b):
    c.update(item)
print(c)
''',
'AttributeError: \'list\' object has no attribute \'update\''
],
[
'''
What will be the output of the following snippet?
a = 1, 2
b = 3, 4
c = ()
for item in (a, b):
    c.update(item)
print(c)
''',
'AttributeError: \'tuple\' object has no attribute \'update\''
],
[
'''
What will be the output of the following snippet and why?
a = 1, 2
b = 3, 4
c = {}
for item in (a, b):
    c.update(item)
print(c)
''',
'''
TypeError: cannot convert dictionary update sequence element #0 to a sequence
It is not possible to merge two one-dimenesional tuples into a dict
'''
],
[
'Can you convert a two-dimensional tuple into a dict?',
'Yes'
],
[
'''
What is the output of the following snippet and why?
tuple = (("a", "1"), ("b", "2"))
dict = dict(tuple)
print(dict)
''',
'''
{\'a\': \'1\', \'b\': \'2\'}
two-dimensional tuple was converted into a tuple
'''
],
[
'''
What will be the output of the following snippet and why?
a = [1, 2]
b = [3, 4]
c = {}
for item in (a, b):
    c.update(item)
print(c)
''',
'''
TypeError: cannot convert dictionary update sequence element #0 to a sequence
It is not possible to merge two lists into a dict.
'''
],
[
'''
What will be the output of the following snippet and why?
a = [1, 2]
b = [3, 4]
c = {}
for item in (a, b):
    c.update(item)
print(c)
''',
'''
TypeError: cannot convert dictionary update sequence element #0 to a sequence
It is not possible to merge two sets into a dict
'''
],
[
'''
What will be the output of the following snippet and why?
a = ["1", "2", "3", "4"],
a = tuple(a)
print(a)
''',
'''
(['1', '2', '3', '4'],)
Because due to the comma after the list, Python considers it as list within a tuple.
It was already a tuple before using the tuple() function
'''
],
[
'''
What will be the output of the following snippet?
a = ["1", "2", "3", "4"]
a = tuple(a)
print(a)
''',
'(\'1\', \'2\', \'3\', \'4\')'
],
[
'''
What will be the output of the following snippet?
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(copy_my_dictionary)
''',
'{\'A\': 1, \'B\': 2}'
],
[
'''
What will be the output of the following snippet?
colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
    }
for col, rgb in colors.items():
    print(col, ":", rgb)
''',
'''
white : (255, 255, 255)
grey : (128, 128, 128)
red : (255, 0, 0)
green : (0, 128, 0)
'''
],
]




mod_4_7 = [
[
'What is a bug?',
'An error in programming code that is not injected by wrong data inputs.'
],
[
'Please type one line of code to check whether the following variable is an integer: a = 1',
'''
if type(a) is int:
OR
if type(a) == int:
'''
],
[
'Why is it preferred in Python to use try and except\ninstead of common preliminary data validation?',
'''
Python works wqith following principles
"It is better to beg for forgiveness than to ask for permission".
"It is better to handle an error when it happens than to try to avoid it"
'''
],
[
'What provision does the try keyword have?',
'''
It expects the except keyword.
Both keywords have a colon after it
The bodies of both keywords have to be indented.
Both keywords require code in their body.
'''
],
[
'What does the try keyword do?',
'''
It tests if the code inside its' body has an error in it.
Any error which occurs here won't terminate program execution
And if it has no error the programm will continue.
You can but you don't have to redirect the programm from here to another location too.
'''
],
[
'What does the except keyword do?',
'''
It detects errors even if the code is syntactically correct.
If the test in the try body had an error the programm jumps into the except body.
The programm cannot get into the except body in any other way.
If except is executed the programm will continue.
You should and it makes sense to redirect the programm from here. 
For example You can ask the user to do a valid input.
'''
],
[
'How can you isolate different error types with try and except?',
'Using more than one except keywords and assigning different error keywords to it.'
],
[
'''
What is the output of the following snippet?
a = 'a'
try:
    int(a) 
    a = 0
    b = 1 / a      
except ValueError:
    print('ValueError') 
except ZeroDivisionError:
    print('ZeroDivisionError') 
''',
'ValueError'
],
[
'''
try:
    a = 0
    int(a) 
    b = 1 / a      
except ValueError:
    print('ValueError') 
except ZeroDivisionError:
    print('ZeroDivisionError') 
''',
'ZeroDivisionError'
],
[
'''
try:
    b = 1 / a      
except ValueError:
    print('ValueError') 
except ZeroDivisionError:
    print('ZeroDivisionError') 
except:
    print('other error')
''',
'other error'
],
[
'What is the default exception?',
'''
It is the expection keyword without specifying an error type.
It reacts to any kind of error, not only to a specific error.
It always must be the last type of exception.
You can also only use this one.
'''
],
[
'What is the ZeroDivisionError keyword?',
'It reacts if there occures an error through dividing a numeric value by zero.'
],
[
'What is the ValueError keyword?',
'''
Assigning the wrong value to an object.
It reacts if there occures an error through a correct data type but a wrong value.
For example when you try to convert a string into a number with int(),
but the string is not a number.
'''
],
[
'What is the TypeError keyword?',
'''
Trying to perform the operation of the wrong type of object.
It reacts if there occures an error through code related incompatibility of different value types such as string, float and int.
In other words: if data types may be inappropriately used in some context
For example you cannot use a float as index. 
Another Example: You cannot Divide an integer by a string, and vice versa.
'''
],
[
'What is the AttributeError keyword?',
'''
It reacts if there occures an error through trying to assign a method that does not exist for the targeted data type.
For example you cannot use the .insert() method on a dictionary.
Another example you cannot use a non-built-in and non-module-imported and non user-defined method onto anything.
a.undefined_function()
'''
],
[
'What is the SyntaxError keyword?',
'''
It reacts if there occures an error through violating Python's grammar.
It maybe a missing or wrong colon, parathesis, bracket, indentation, comma, quote, operator etc.
This error is not recommended to be handles through try and except,
as the code should be always entirely syntacically correct.
'''
],
[
'What is the NameError keyword?',
'''
It reacts if there occures an error through not defining a variable or function.
For example if you try to print a variable that has not been defined
or only defined locally and you want to print it globally.
'''
],
[
'What is the main difference between a TypeError and NameError?',
'TypeError means error in the data type and NameErrors occur due to undefined names of variables or functions.'
],
[
'What is the main difference between a ValueError and TypeError?',
'TypeError means error in the data type and ValueError right datatype but wrong value.'
],
[
'Why is it a must to test also without your code and don\'t only rely on try and error?',
'''
If you don't know a mistake you don't always know how to handle an exception corretcly.
Challenging your code id important to have a secure and user friendly result.
And it will save you a lot of time searching for bugs or other errors,
later when you maybe have not seen the code for a longer time.
The more intense and you test your code and the more you lead testing your code
ad absurdum, the more solid and secure your code will become.
'''
],
[
'What is a Hackathon?',
'''
It is the call from a project to the public to intendedly hack their programm
to find out if there are errors left.
Winners of Hackathons often receive valuable rewards as they can save the project
in advance a lot of damage created by unethical hackers or bugs.
'''
],
[
'Which parts of the code require most attention to testing it?',
'execution paths'
],
[
'What is an execution path?',
'''
Each part of code that has commands in it. 
For example every command that writes data into a data base or that
creates output for the user ort input b the user.
Generally it includes every action that lets your programm interact with other entities.
For example conditions of if, while, for etc are NO executions paths.
But commands that trigger properties, methods and functions ARE execution paths
'''
],
[
'Mention at least five examples for execution paths:',
'print(), input(), .insert(), .upgrade(), .pop() del, and many more'
],
[
'''
Why is testing so important for programming languages
that are subject to interpretation and parsing?
''',
'''
Not all elements of the code are executed if some execution paths are conditioned.
For bugs that are not triggered you may won't receive an error alert.
'''
],
[
'What is a debugger?',
'''
A debugger is a specialized piece of software that can control how your program is executed.
Using the debugger, you can execute your code line-by-line.
'''
],
[
'What does a debugger show above the code? ',
'The (sub-)results of the code.'
],
[
'Mention at least three tasks you can do with a debugger:',
'''
inspect the states of varibales, change the variables values on demand,
conditionally stop programm execution,
'''
],
[
'What is interactive debugging?',
'Debugging that needs the developers interaction to perform it.'
],
[
'What is print debugging?',
'''
One of the oldest debugging techniques.
Insert several additional print() invocations inside your code
to inspect the sub-results.
This way you can check if the sub-results match with the expectations
and localise problems
'''
],
[
'What are helpful ways to debug your code?',
'''
Ask another developer to look over your code.
Try rubber duck debugging.
Try to isolate the problem. 
Analyze changes you have made since your code worked the
last time without problems.
Take a break. Be optimistic and even happy that you find a problem
as solving it improves your code and trains you to avoid it next time.
Try to send different input data and data types through your code.
Try to inspect the mathematical dimensions of your results
by putting in very high and very low numbers.
Test your programm on different hardware and operating systems.
'''
],
[
'What is rubber duck debugging?',
'Articulating a problem in spoken or written natural language.'
],
[
'What is unit testing?',
'''
Equip your code with an interface that can be used by an automated testing environment
Having a list of various input data to be tried.
Running a test system separately from the main software.
'''
],
[
'''
What does the following code do?
While True:
    try:
    num = int(input())
    break
    except:
        print('alert')
''',
'It asks the user for input until the user has not typed a numeric value.'
],
[
'With which word does every function definition start?',
'True'
],
[
'Is a function invocation to be placed beneath or above its function definition?',
'beneath'
],
[
'Is a function parameter accessible inside or outside the function or both?',
'only inside'
],
[
'What is position argument passing?',
'A way of passing arguments in which the order of the arguments determines the initial parameters\' values.'
],
[
'''
Which of the following statements are true?
a) The return keyword forces the function's execution to terminate.
b) The return keyword may cause the function to return a value.
c) Each function must have the return keyword in it.
d) The return keyword forces the function to restart its execution
e) Any code in a function after the return keyword will not be executed
''',
'''
a, b, e
'''
],
[
'''
Which of the following statements is true?
A variable defined outside a function:
a) may be read, but not written inside the function
b) may not be accesses in a any way inside th function
c) may be freely accessed inside the fuunction
d) is shadowed inside the function when it is used inside the function locally
''',
'a, d'
],
[
'What happens when you pass a list to a function and change its arguments inside the function and why?',
'''
A refrence is create and therefore changes to the list inside
the function will affect the elements referred to.
'''
],
[
'''
What is the output of the following snippet?
edf, fed, fde, def, dfe = 13, 10, 5, 3, 8
result = edf + fed + fde + def + dfe
print(result)
''',
'Syntax Error, because def is a keyword'
],
[
'''
What is the output of the following snippet?
gift = 'jewelry'
from = 'Peter',
for = 'Jenny'
print(from, 'has', gift, 'for', for)
''',
'Syntax Error, because def is a keyword'
],
[
'''
What is the output of the following snippet?
dist = 4
from = 'Hamburg',
to = 'Berlin'
print('The distance from', from, 'to', to, 'is', dist, 'hours')
''',
'Syntax Error, because def is a keyword'
],
[
'''
What is the output of the following snippet?
a, b, c, d, e = 13, 10, 5, 3, 8
result = sum(a, b, c, d, e)
print(result)
''',
'TypeError: sum expected at most 2 arguments, got 5'
],
[
'''
What is the output of the following snippet?
a = 7,
b = 2
c = a + b
print(len(c))
''',
'TypeError: can only concatenate tuple (not "int") to tuple'
],
[
'''
What is the output of the following snippet?
a = 7,
b = 2,
c = a + b
print(len(c))
''',
'2'
],
[
'''
What is the output of the following snippet when the user enters 0 and why?
a = input()
print(10 / a)
''',
'''
TypeError: unsupported operand type(s) for /: 'int' and 'str'
'''
],
[
'''
What is the output of the following snippet and why?
a = .5 * 5. + 5,
print(a) 
''',
'''
(7.5,),
because 0.5 * 5.0 is 2.5
and because the tuple is created after the two calculations are completed. 
So the plus sign has higher priority than the comma sign due to left-sided-binding
'''
],
[
'''
What is the output of the following snippet and why?
a = 5, + .5 * 5. 
print(a)
''',
'''
(5, 2.5)
because the tuple is created before the two calculations.
So the comma sign has higher priority than the plus sign due to left-sided-binding.
and because 0.5 * 5.0 is 2.5
'''
],
[
'''
What is the output of the following snippet and why?
a = .5 + 5, * 5
print(a)
''',
'''
TypeError: 'int' object is not iterable
*5 is the only value inside the second element of the tuple.
Using the star together with only once arguments tells python
you want to iterate an object (e.g. for unpacking it)
But iterable objects can not be int, str, float etc.
Iterable objects can only be sequences (tuples, sets, lists) and dicts.
'''
],
[
'''
What is the output of the following snippet and why?
a = .5 + 5, + 5. 
print(a)
''',
'''
(5.5, 5.0)
because a tuple with one element is created from the result of the first calculation.
after the comma the next tuple element is added.
Plus plus sign is redundant here.
'''
],
[
'''
What is the output of the following snippet and why?
a = .5 + 5,
a += 5.
print(a)
''',
'''
TypeError: can only concatenate tuple (not "float") to tuple
Because tuples are immutable!
'''
],
[
'''
Which statements are true? 
A function defined in thew following way 
a) may be invoked without any argument
b) must be invoked without any argument
c) may be invoked with exactly one argument
d) must be invoked with exactly one argument
''',
'a, c'
],
[
'''
Which statements are true?
A built-in function is a function which:
a) comes with python and is an integral part ofpython
b) is hidden from programmers
c) has been placed within ur code by anothe rprogrammer
d) has been imported before use
''',
'a'
],
[
'''
Which statements are true?
The fact that tuples belong to sequence types mean that:
a) they can be indexed and sliced like lists
b) they are actually lists
c) they can be extended using the append method
d) they cxan be modified uusing the del instruction
''',
'a'
],
[
'''
What is the output of the following snippet?
def func_1(a):
    return a**a
def func_2(a):
    return func_1(a) * func_1(a)
print(func_2(2))
''',
'16'
],
[
'''
What is the output of the output of the following snippet?
def fun(x)
    x += 1
    return x
x = 2
x = fun(x + 1)
print(x)
''',
'SyntaxError (because the colon is missing in the function definition)'
],
[
'''
What is the output of the output of the following snippet?
def fun(x):
    x += 1
    return x
x = 2
x = fun(x + 1)
print(x)
''',
'4'
],
[
'''
Which statements are true in regard of the following pseudo code?:
try:
    # some code
except:
    # some code
a) if you suspect that a snippet may raise an exception,
you should place it in the try block
b) The code that follows the except statement will be executed
if the code in the try clause runs into annerror
c) The code that follows the try statement will be executed
if the code in the except clause runs into an error
d) if there is a syntax error in code located in the try block, the except branch
will not handle it and a syntax error exception will be raised instead
''',
'a, b'
],
[
'''
Which of the following lines properly starts a function using two parameters,
both with zeroed default values?
a) def fun(a=0, b=0):
b) fun fun(a, b=0):
c) fun fun(a=0, b):
d) def fun(a=b=0):
''',
'a'
],
[
'''
What is the output of the followng snippet?
dict = {'one' : 'two', 'three' : 'one', 'two' : 'three'}
v = dict['one']
for k in range(len(dict)):
    v = dict[v]
print(v)
''',
'two'
],
[
'''
What is the output of the following snippet?
def fun(x, y, z):
    return x + 2 * y + 3 * z
print(fun(0, z=1, y=3))
''',
'9'
],
[
'''
What is the output of the following snippet?
def any():
    print(var + 1, end='')
var = 1
any()
print(var)
''',
'21'
],
[
'''
What is the output of the following snippet?
def fun(x):
    global y
    y = x *x
    return y
fun(2)
print(y)
''',
'4'
],
[
'''
What is the output of the following snippet?
def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))
''',
'4'
],
[
'''
What is the output of the following snippet?
def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)
print(f(3))
''',
'6'
],
[
'''
Which of the following statements are true?
a) The None value can be assigned to variables.
b) The None value can be used as argumnet of arithmentic operators.
c) The None value cannot be used outside functions.
d) The None value can be compared with variables.
''',
'a, d'
],
[
'''
What is the output of the following snippet?
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print[tup]
''',
'TypeError: \'builtin_function_or_method\' object is not subscriptable'
],
[
'''
What is the output of the following snippet?
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
''',
'2'
],
[
'''
What is the output of the following snippet?
def func(a, b):
    return a**a
print(func(2))
''',
'TypeError: func() missing 1 required positional argument: \'b\''
],
[
'''
Which of the following statements are true regarding the following snippet?:
my_tuple[1] = my_tuple[1] + my_tuple[0]
a) It can be executed if and only if the tuple contains at least two elements
b) It is illegal
c) It is fully correct
d) It may be illegal if the tuple contains strings
''',
'b'
],
[
'''
What is the output of the following snippet?
my_list = ['mary', 'had', 'a', 'little', 'lamb']
def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'
print(my_list(my_list))
''',
'TypeError: \'function\' object does not support item deletion'
],
[
'''
Which one of the following lines properky starts a parameterless function definition?
a) def fun():
b) fun function():
c) def fun:
d) function fun():
''',
'a'
],
[
'''
What is the output of the following snippet?
def fun(x):
    if x % 2 = 0:
        return 1
    else:
        return
print(fun(fun(2)) + 1)
''',
'''
SyntaxError
(if condition uses an assignment operator instead of a comparison operator)'
'''
],
[
'''
What is the output of the following snippet?
def fun(x):
	if x % 2 == 0:
		return 1
	else:
		return
print(fun(fun(2)) + 1)
''',
'''
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
'''
],
[
'''
What is the output of the following code?
lst = ['a', 'b', 'c', 'd']
for i in range(len(lst)):
    print(i, end='')
''',
'0123 (because range always begins with 0 as default preference)'
],
[
'''
What is the output of the following code?
d = {}
print(type(d))
''',
'<class \'dict\'>'
],
[
'''
What is the output of the following code?
d = {1, 2}
print(type(d))
''',
'<class \'set\'>'
],
[
'''
dict = {}
my_list = ['a', 'b', 'c']
for i in range(len(my_list) -1):
	dict[i] = (my_list[i])
print(dict)
''',
'{0: \'a\', 1: \'b\'}'
],
[
'''
What code do you need to insert to get the following output: abc
dict = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) -1):
    dict[my_list[i]] = (my_list[i],)
    
for i in sorted(dict.keys()):
    k = dict[i]
    # insert code here

a) print(k["0"], end='')
b) print(k['0'], end='')
c) print(k, end='')
d) print(k[0], end='')
''',
'd'
],
[
'''
What code do you need to insert to get the following output: abc
dict = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) -1):
    dict[my_list[i]] = (my_list[i],)
    
for i in sorted(dict.keys()):
    k = i
	
a) print(k["0"], end='')
b) print(k['0'], end='')
c) print(k, end='')
d) print(k[0], end='')
''',
'c'
],
[
'''
dict = {'a' : 'a', 'b':'b'}
dict.update({'a'})
print(dict)
''',
'ValueError (because there is no value given to the key in the .update() method)'
],
[
'''
dict = {'a' : 'a', 'b':'b'}
dict.update('a':1)
print(dict)
''',
'SyntaxError (because the {} in the .update() method are missing)'
],
[
'''
dict = {'a' : 'a', 'b':'b'}
dict.update({'c':1})
print(dict)
''',
'{\'a\': \'a\', \'b\': \'b\', \'c\': 1}'
],
[
'''
dict = {'a' : 'a', 'b':'b'}
dict.update({'a':1})
print(dict)
''',
'{\'a\': 1, \'b\': \'b\'}'
],
[
'''
dict = {'a' : 'a', 'b':'b'}
dict.insert({'a':1})
print(dict)
''',
'AttributeError: \'dict\' object has no attribute \'insert\''
],
[
'''
What is the output of the following piece of code if the user enter two lines containing 2 and 4 respectively?
x = float(input())
y = float(input())
print(y**(1 / x))
''',
'''
2.0
'''
],
[
'''
How many elements does the lst contain?
lst = [i for i in range(-1, -2)]
''',
'''
zero
'''
],
[
'''
How many elements does the lst contain?
lst = [i for i in range(8, -2)]
''',
'''
zero
'''
],
[
'''
How many elements does the lst contain?
lst = [i for i in range(8, -2, -3)]
''',
'''
4
lst = [8, 5, 2, -1]
'''
],
[
'''
What is the output of the following snippet?
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))
2
''',
'''
2
'''
],
[
'''
What is the output of the following snippet?
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z
print(x, y, z)
''',
'''
1 1 2
'''
],
[
'''
What will be the output of the following snippet?
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(y, b)
''',
'''
0 1
because in the last assignment a and b are the same, so on xor the result is 0
'''
],
[
'''
What is the output of the following snippet?
tup = (1, 2, 3, 4, 5)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
''',
'''
4
because only the element is printed, if only one element of a sequence is adressed
'''
],
[
'''
What will be the output of the following snippet?
def function_1(a):
    return None
def function_2(a):
    return function_1(a) * function_1(a)
print(function_2(2))
''',
'''
TypeError because you cannot calculate with None
'''
],
[
'''
Which of the following ways would be a correct except statement?
a) except: (TypeError, ValueError, ZeroDivisionError)
b) except TypeError, ValueError, ZeroDivisionError:
c) except (TypeError, ValueError, ZeroDivisionError)
d) except: TypeError, ValueError, ZeroDivisionError
e) except (TypeError, ValueError, ZeroDivisionError):
f) except TypeError, ValueError, ZeroDivisionError
''',
'''
e
because if you use more than one error type in one except statement
you have to use paranthesis
'''
],
[
'''
What is the output of the following snippet?
lst = [x *x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(lst))
''',
'''
[0, 1, 4, 9]
because due to using the element value 4
as an index the last element of the list (16) will be deleted
'''
],
[
'''
What is the output of the following snippet?
lst = [x *x for x in range(3)]
def fun(lst):
    del lst[lst[1]]
    return lst
print(fun(lst))
''',
'''
[0, 4]
'''
],
[
'''
What type of error will occur when you try to run this code?
print(Hello, World!)
''',
'''
SyntaxError, because you cannot write non keywords into the code
as without declaring them as string
'''
],
[
'''
What type of error will occur when you try to run this code?
print('hello', 'world', sep=a)
''',
'''
NameError as a is not defined
'''
],
[
'''
What type of error will occur when you try to run this code?
print('hello', 'world', s=a)
''',
'''
Name Error as a is not defined
'''
],
[
'''
What type of error will occur when you try to run this code?
a = 1
print('hello', 'world', s=a)
''',
'''
TypeError: 's' is an invalid keyword argument for print()
'''
],
[
'''
What type of error will occur when you try to run this code?
a = 1
print('hello', 'world', sep=a)
''',
'''
TypeError: sep must be None or a string, not int
'''
],
[
'''
What type of error will occur when you try to run this code?
a = 1
print('hello', 'world', sep=str(a))
''',
'''
hello1world
'''
],
[
'''
What type of error will occur when you try to run this code?
print('hello', 'world').hello()
''',
'''
AttributeError: 'NoneType' object has no attribute 'hello'
'''
],
[
'''
What type of error will occur when you try to run this code?
print('hello'+ 'world')[1]
''',
'''
TypeError: 'NoneType' object is not subscriptable
'''
],
[
'''
What type of error will occur when you try to run this code?
print(1 + '1')
''',
'''
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
],
[
'''
What type of error will occur when you try to run this code?
print('a' + int('a'))
''',
'''
ValueError: invalid literal for int() with base 10: 'a'
'''
],
[
'''
What type of error will the following code result in?
try:
    print(5/0)
    break
except:
    print(1)
except (ValueError, ZeroDivisionError):
    print(2)
''',
'''
Syntax Error becase a break statement was used outside a loop
'''
],
[
'''
In which context can you use the break or continue keywords?
''',
'''
ONLY in loops!
'''
],
[
'''
What type of error will the following code result in?
try:
    print(5/0)
except:
    print(1)
except (ValueError, ZeroDivisionError):
    print(2)
''',
'''
SyntaxError because specific errors for except statements must always
come before unspecific except statements.
'''
],
[
'''
Which statement is true about the following code?
nums = [1, 2, 3]
vals = nums
a) nums and vals are different lists
b) nums has same length as vals
c) vals is longer than nums
d) nums and vals are different names for the same list
''',
'''
b, d
'''
],
[
'''
What is the output of the following piece of code?
print('a', 'b', 'c', sep='sep')
''',
'''
asepbsepc
'''
],
[
'''
What is the output of the following snippet?
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)
for x in dct.keys():
    print(dct[x][1], end='')
''',
'''
21 (because the second elements of the tuples are
addressed by using dct[x][1])
'''
],
[
'''
What is the output of the following snippet?
dct = {'one' : 'two', 'three' : 'one', 'two' : 'three'}
v = dct['three']
for k in range(len(dct)):
    v = dct[v]
print(v)
''',
'''
one (because inside the loop the value of v changes each time)
'''
],
[
'''
What is the output of the following code?
print = 1
print(print)
''',
'''
TypeError: 'int' object is not callable
'''
],
[
'''
What is the output of the following code?
print = 1
a = print + 1
print(a)
''',
'''
TypeError: 'int' object is not callable
'''
],
[
'''
What is the output of the following code?
print = []
del print
a = 1
print(a)
''',
'''
1
'''
],
[
'''
What is the output of the following code?
print = []
del print
a = 1
print(print)
''',
'''
<built-in function print>
'''
],
[
'''
What is the output of the following code?
x = 1 // 5 + 1 / 5
print(x)
''',
'''
0.2
'''
],
[
'''
Which of the following lines correctly invoke the following function?
def fun(a, b, c=0):
	pass
a) fun(b=0, a=0)
b) fun(b=1)
c) fun(1, 2, 3)
d) fun()
''',
'''
a, c
'''
],
[
'''
What is the ourput o the following code?
foo = (1, 2, 3)
a = foo.index(0)
print(a)
''',
'''
ValueError: tuple.index(x): x not in tuple
Because the index() method searches for the indicies via its value
in the methods argument
And the tupke has no value 0 and therefore no value with the index of 0
And it is specifically a ValueError because everything has been written
correctly but a wrong value was used.
'''
],
[
'''
What is the ourput o the following code?
foo = (1, 2, 3)
a = foo.index(1)
print(a)
''',
'''
0
'''
],
[
'''
What is the output of the following code if the user enters 0?
try:
    value = input()
    print(int(value)/len(value))
except ValueError:
    print(1)
except ZeroDivisionError:
    print(2)
except TypeError:
    print(3)
except:
    print(4)
''',
'''
0.0

'''
],
[
'''
How many stars will the following snippet send to the console?
i = 0
while i < i + 2:
    i += 1
    print('*')
else:
    print('*')
''',
'''
infinite (because it is an infinite loop as i never gets smaller then i + 2)
'''
],
[
'''
What is the output of the following snippet?
tup = (1, 2, 3)
tup[1] = tup[2] + tup[0]
print(tup)
''',
'''
TypeError: 'tuple' object does not support item assignment
because a tuple is immutable.

'''
],
[
'''
What is the output of the following snippet?
def fun(a, b):
    return b ** a
print(fun(b=2, 2))
''',
'''
SyntaxError: positional argument follows keyword argument
'''
],
[
'''
What is the output of the following snippet?
def fun(in=2, out=3):
    return in * out
print(fun(out=2))
''',
'''
Syntax Error because in is a keyword and cannot be used as parameter or variable
'''
],
[
'''
What is the output of the following snippet?
def fun(inp=2, out=3)
    return inp * out
print(fun(out=2))
''',
'''
Syntax Error because a colon is missing at the end of the function definition
'''
],
[
'''
What is the output of the following snippet?
def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))
''',
'''
4
'''
],
[
'''
What is the output of the following snippet?
lst = [1, 2]
for v in range(2):
    lst.insert(-1, lst[v])
''',
'''
[1, 1, 1, 2]
because using a negative value as target position inside the .insert() method
will always place the traget value at the first position of the list.
NOTE: the first argument of .insert() it is not an index
but an argumentfor a position.
More over the value 1 will be added to the list as the in the
second loop step the  value added becomes the new value to be added.
'''
],
[
'''
What is the output of the following snippet?
lst = [1, 2]
lst.insert(-8, 9)
print(lst)
''',
'''
[9, 1, 2]
REMEMBER: using the .insert() methos is not like using an index
'''
],
[
'''
What is the output of the following snippet?
lst = [1, 2]
lst.insert(-2, -1)
print(lst)
''',
'''
[-1, 1, 2]
REMEMBER: using the .insert() methos is not like using an index
'''
],
[
'''
What is the output of the following snippet?
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
print(fun(0, 3))
''',
'''
0
because the function gets recursed until y has been decremented to 0
'''
],
[
'''
How many hashed will the following code send to the console?
lst = [[x for x in range(3)] for j in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print('#')
''',
'''
three
because it is a two-dimnesional list with three elements
in each dimension like this
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
and each element of the inner loop only has one value whose modulo is not 0.
This value is 1
And as the outer loop runs 3 times you get 3 hashes
'''
],
[
'''
What is the output of the following snippet?
dd = {'1' : '0', '0' : '1'}
for x in dd.vals():
    print(x, end='')
''',
'''
AttributeError: 'dict' object has no attribute 'vals'
Actually the method .vals() does not exist at all
'''
],
[
'''
What is the output of the following code if the user types 3 and 2 respectively?
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
''',
'''
0
because firtsly x becomes 1 (3%2) (an integer dicsion would result in 1 with remainder of 1)
then x becomes 1 again (1%2) (an integer decision would result in 0 with remainder 1)
then y becomes 0 (2/1) (an integer division would result in 2 without remainder)
'''
],
[
'''
Which statement about the following snippet is true?
nums = [1, 2, 3]
vals = nums
del vals[:]
a) nums and vals have the same length
b) vals is longer than nums
c) nums is longer than vals
d) the snippet will cause a runtime error
''',
'''
a (because vals is a reference to nums (same cache id) and a copy of it)
And by using del vals[:] the entire vals list will be deleted and nums as well.
'''
],
[
'''
What is the output of the following snippet if the user types 3 and 6 respectively?
y = input()
x = input()
print(x + y)
''',
'''
36 (because uncoverted inputs are always strings)
Herethe strings get concatenated using the + inside the print() function
'''
],
]


    
##########   SETUP LEARNING MODULE HIERARCHY
#!!!!!!! SELBST Nummern kann ich mir sparen List reicht !!!!!! #

mod_0 = {}

mod_1 = {
0 : 'All sub modules',
1 : 'Introduction',
2 : 'Downloading and installing'
}

mod_2 = {
0 : 'All sub modules',
1 : 'Hello, world!',
2 : 'Literals',
3 : 'Arithmetic operators and hierarchy of priorities',
4 : 'Variables',
5 : 'Comments',
6 : 'The input[] function and string operators'
}

mod_3 = {
0 : 'All sub modules',
1 : 'Comparison operators and conditional execution',
2 : 'Loops',
3 : 'Logic and bit operations',
4 : 'Lists',
5 : 'Sorting simple lists',
6 : 'List processing',
7 : 'Multidimensional arrays'
}

mod_4 = {
0 : 'All sub modules',
1 : 'Functions',
2 : 'Function parameters and argument passing',
3 : 'Returning results from functions',
4 : 'Functions and scopes',
5 : 'Creating simple functions',
6 : 'Tuples and dictionaries',
7 : 'Exceptions'
}

mod = {
0 : 'All modules',
1 : 'Introduction to Python and computer programming',
2 : 'Data types, variables, basic I/O operations, basic operators',
3 : 'Boolean, conditions, loops, lists, logical and bitwise operations',
4 : 'Functions, tuples, dictionaries, data processing, exceptions'
}


# Append pseudo index to first element of each question
for i in range(1, len(mod)):
    h1 = globals()['mod_'+str(i)]           
    # Loop through hierarchy level 1
    for j in range(1, len(h1)):
        h2 = globals()['mod_'+str(i)+'_'+str(j)]
        # Loop through hierarchy level 2
        for k in range(len(h2)):
            question = h2[k]
            # APPEND IT!
            question.insert(0, k+1)


