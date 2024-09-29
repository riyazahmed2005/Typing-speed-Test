import curses
from curses import wrapper 
import time


def screen_begin(stdscr):
    stdscr.clear() # clear the screen
    stdscr.addstr(0,0,"Welcome to the speed typing Test! ") #add the test at row=0,column=0
    stdscr.addstr(1,0,"\nPress any to start!")
    stdscr.refresh()
    stdscr.getkey() # without using the getkey it automatically closed

def check(stdscr,target,current,wpm=0):
    
    stdscr.addstr(target)

    stdscr.addstr(2,0,f"wpm={wpm}")
    
    for i,c in enumerate(current):
        current_char=target[i]
        color=curses.color_pair(1)
        if c!=current_char:
            color=curses.color_pair(2)

        stdscr.addstr(0,i,c,color)

def test_page(stdscr):
    target="hi this is riyaz ahmed speed typing test" #target text to the user to type
    current=[]
    wpm=0 
    st=time.time()
    stdscr.nodelay(True)
    
    
    
    while True:
       
        elapsed=max(time.time()-st,1) 

        wpm=round((len(current)/(elapsed/60))/5)

        stdscr.clear()
        check(stdscr,target,current,wpm)
        if "".join(current)==target:
            stdscr.nodelay(False)
            break
        stdscr.refresh()
        try:
           
            key=stdscr.getkey() 
        except:
           continue
        

        if ord(key)==27:
            break

        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current)>0:
                current.pop()

        elif(len(current)<len(target)):
    
            current.append(key)


def main(stdscr):

    # initilizing the the color
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_WHITE)
   
    screen_begin(stdscr)

   
    while True:
        test_page(stdscr)   
        stdscr.addstr(3,0,"Completed press any key to continue!..")
        ky=stdscr.getkey()
        if ord(ky)==27:
            break
wrapper(main)