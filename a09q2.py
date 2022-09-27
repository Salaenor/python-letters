#---------------
#Shelby Paxton (20654302)
#CS 116 Fall 2017
#Assignment 09, q2
#---------------

#Imports
import check
import math

#Purpose
#fline() returns a list of the first line of each letter from letter.txt minus the '$' character
#Effects:
#-reads from letters.txt
#Contract
#fline: None -> (list of str)
def fline():
    f = open('letters.txt', 'r')
    line = f.readline()
    answer = []
    while line != "":
        answer.append(line.strip('$\n'))
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
    f.close()
    return answer

#Purpose
#sline() returns a list of the second line of each letter from letter.txt minus the '$' character
#Effects:
#-reads from letters.txt
#Contract
#sline: None -> (list of str)

def sline():
    f = open('letters.txt', 'r')
    line = f.readline()
    line = f.readline()
    answer = []
    while line != "":
        answer.append(line.strip('$\n'))
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
    f.close()
    return answer

#Purpose
#tline() returns a list of the third line of each letter from letter.txt minus the '$' character
#Effects:
#-reads from letters.txt
#Contract
#tline: None -> (list of str)
def tline():
    f = open('letters.txt', 'r')
    line = f.readline()
    line = f.readline()
    line = f.readline()
    answer = []
    while line != "":
        answer.append(line.strip('$\n'))
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
    f.close()
    return answer
#Purpose
#f2line() returns a list of the fourth line of each letter from letter.txt minus the '$' character
#Effects:
#-reads from letters.txt
#Contract
#f2line: None -> (list of str)
def f2line():
    f = open('letters.txt', 'r')
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    answer = []
    while line != "":
        answer.append(line.strip('$\n'))
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
    f.close()
    return answer
print(f2line())
#Purpose
#f3line() returns a list of the fifth line of each letter from letter.txt minus the '$' character
#Effects:
#-reads from letters.txt
#Contract
#f3line: None -> (list of str)
def f3line():
    f = open('letters.txt', 'r')
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    line = f.readline()
    answer = []
    while line != "":
        answer.append(line.strip('$\n'))
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
    f.close()
    return answer


#Purpose
#print_art(msg, filename) creates txt file with the name filename that contains msg in it but made from the letters from letter.txt. This function returns nothing
#effects:
#-writes to filename.txt

#Contract
#print_art: str. str -> None

#Examples
# if print_art("eggos", "eggos.txt") then a file called eggos.txt will be produced that says "eggos" in all caps and the letters consist of a number of smaller letters
# if print_art("CAPS", "LOCK.txt") then a file called LOCK.txt will be produced that says "CaPS" in all caps and the letters consist of a number of smaller letters
# if print_art("a", "atxt") then a file called a.txt will be produced that says "a" in all caps and the letters consist of a number of smaller letters

#Body

def print_art(msg, filename):
    f = open(filename, 'w')
    for i in msg.lower():
        if i == " ":
            f.write("    ")
        else:
            f.write(fline()[ord(i)-97])
    f.write('\n')
    for i in msg.lower():
        if i == " ":
            f.write("    ")
        else:
            f.write(sline()[ord(i)-97])
    f.write('\n')
    for i in msg.lower():
        if i == " ":
            f.write("    ")
        else:
            f.write(tline()[ord(i)-97])
    f.write('\n') 
    for i in msg.lower():
        if i == " ":
            f.write("    ")
        else:
            f.write(f2line()[ord(i)-97])
    f.write('\n') 
    for i in msg.lower():
        if i == " ":
            f.write("    ")
        else:
            f.write(f3line()[ord(i)-97])
    f.write('\n')     
    f.close()
print

#Tests
#general test
check.set_file_exact("hello.txt","print_art_1.txt")
check.expect("Q2T1", print_art("helloworld", "hello.txt"), None)
#having a space inbetween words
check.set_file_exact("space.txt","print_art_2.txt")
check.expect("Q2T2", print_art("hello world", "space.txt"), None)
#mixed letter case
check.set_file_exact("egg.txt","print_art_3.txt")
check.expect("Q2T3", print_art("EggO", "egg.txt"), None)
#testing out all lower case letters
check.set_file_exact("alphabetl.txt","print_art_4.txt")

check.expect("Q2T4", print_art("abcdefghijklmnopqrstuvwxyz", "alphabetl.txt"), None)
#testing out all upper case letters
check.set_file_exact("alphabetu.txt","print_art_5.txt")

check.expect("Q2T5", print_art("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "alphabetu.txt"), None)
#testing out white space between letters
check.set_file_exact("caps.txt","print_art_6.txt")

check.expect("Q2T6", print_art("h e l l o  w o r l d", "caps.txt"), None)
#testing out white space before and after a letter
check.set_file_exact("huh.txt","print_art_7.txt")
check.expect("Q2T7", print_art(" d ", "huh.txt"), None)
#testing out having a single letter
check.set_file_exact("single.txt","print_art_8.txt")
check.expect("Q2T8", print_art("e", "single.txt"), None)