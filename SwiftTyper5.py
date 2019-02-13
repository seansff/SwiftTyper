'''
Created by: Aditya Sarode, Aaryaman 'Jam' Vashishtha and Vaibhav Tulsyan (a.k.a xennygrimmato)
'''
#python 2
import time
import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *


from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

curr_directory = os.getcwd()
 
name = tkFileDialog.askopenfilename(initialdir = curr_directory,title = "Select text file",filetypes = [("Text files","*.txt")])
print(name)


try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

userInputWord=""
positionOfCurrentWord=0
endOfCurrentWord=0
currentWordFromPara=""
lineNum = 1.0
currentLine = 0.0
currentCharsByLine = 0.0
incrVertPosBy = 1.0
lineReduce = 2.0

sad = []

with open(name, 'r') as fh:
    for line in fh:
        line = line.rstrip("\n")
        sad.append(line)
        lineNum += 1

paragraph = ' '.join(sad)

words=0
numberOfReds=0
numberOfChars=1
totalChars=len(paragraph)

currentLine = 0
charsPerLine = totalChars/lineNum

print lineNum
print charsPerLine

def stringmatch(a,b):   # A function which will match string a and b and return 1 if both are, else 0
    i=0
    while i<len(a):
        if a[i]!=b[i]:
            return False
        i+=1
    return True

def updatecurrentWordFromPara():            # A function used to store the next word into 
    global positionOfCurrentWord            # currentWordFromPara and update 
    global currentWordFromPara          # positionOfCurrentWord to next word's position
    if positionOfCurrentWord>=len(paragraph):
        return "-1"             # "-1" is returned if end of paragraph is reached
    endOfCurrentWord=positionOfCurrentWord
    while endOfCurrentWord<len(paragraph):
        if paragraph[endOfCurrentWord]==" ":
            break
        endOfCurrentWord+=1
    currentWordFromPara=paragraph[positionOfCurrentWord:endOfCurrentWord+1]
    positionOfCurrentWord=endOfCurrentWord+1


class Example(QWidget):
    
    value=0
    start=0
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    
    def resizeEvent(self,event):
        #                   1366 * 768
        myh=self.mywin.height()
        myw=self.mywin.width()
        self.lbl.setGeometry(QRect((myw*70/1366), (myh*50/768),(myw*800/1366), (myh*450/768)))   
        self.qle.setGeometry(QRect((myw*70/1366),(myh*550/768),(myw*800/1366),(myh*100/768)))
        self.exitlbl.setGeometry(QRect((myw*900/1366),(myh*550/768),(myw*500/1366),(myh*100/768)))
        self.lcdtimer.setGeometry(QRect((myw*900/1366), (myh*100/768), (myw*250/1366),(myh*120/768)))
        self.lcdwpm.setGeometry(QRect((myw*900/1366),(myh*240/768),(myw*250/1366),(myh*120/768)))
        self.lcdaccuracy.setGeometry(QRect((myw*900/1366),(myh*380/768),(myw*250/1366),(myh*120/768)))
        self.wpmlbl.setGeometry(QRect((myw*1155/1366),(myh*240/768),(myw*100/1366),(myh*120/768)))
        self.accuracylbl.setGeometry(QRect((myw*1155/1366),(myh*380/768),(myw*50/1366),(myh*120/768)))

    

    def count(self):

        global tempfloat
        global speed
        self.value = self.value+1
        if self.value%10==0: self.lcdtimer.display((((self.value/600)*1000)+(self.value%600))/10)
        self.lcdwpm.display(600*words/self.value)
    
        speed=600*words/self.value
        tempfloat=100*(numberOfChars-numberOfReds)/numberOfChars
        self.lcdaccuracy.display(int(tempfloat))

    def initUI(self):      
        self.mywin=self.window()
        
        self.value=0
        self.lcdtimer = QLCDNumber(self)
        self.lcdtimer.setGeometry(QRect(700, 120, 250,120))
        self.lcdtimer.setStyleSheet(_fromUtf8("background-color: rgb(201, 183, 255);"))
        self.timer=QTimer()
        self.lcdwpm=QLCDNumber(self)
        self.lcdwpm.setGeometry(QRect(700,260,250,120))
        self.lcdwpm.setStyleSheet(_fromUtf8("background-color: rgb(201, 183, 255);"))
        self.lcdaccuracy=QLCDNumber(self)
        self.lcdaccuracy.setGeometry(QRect(700,400,250,120))
        self.lcdaccuracy.setStyleSheet(_fromUtf8("background-color: rgb(201, 183, 255);"))
        QObject.connect(self.timer, SIGNAL("timeout()"), self.count)
    
        self.lcdtimer.display(self.value)
        
        self.lbl = QTextBrowser(self)

        self.exitlbl=QLabel(self)
        self.exitlbl.setGeometry(QRect(70,365,700,100))

        self.lbl.setGeometry(QRect(70, 50, 724, 300))
        self.lbl.setObjectName(_fromUtf8("lbl"))
        self.lbl.setText("<font size=\"20\">"+paragraph+"</font>")
        self.lbl.setStyleSheet(_fromUtf8("background-color: rgb(201, 183, 255); color: black;"))

        self.qle = QLineEdit(self)
        self.qle.setGeometry(QRect(70,500,724,100))
        self.qle.setStyleSheet(_fromUtf8("font: 18pt \"mry_KacstQurn\";\n""color: #25343B;"
        "background-color: rgb(201, 183, 255);"))
        self.qle.textChanged[str].connect(self.onChanged)
        self.wpmlbl=QLabel(self)
        self.wpmlbl.setGeometry(QRect(1155,260,100,120))
        self.wpmlbl.setText("<font size=\"16\">wpm</font>")
        self.wpmlbl.setStyleSheet(_fromUtf8("background-color: rgb(201, 183, 255);"))
        self.accuracylbl=QLabel(self)
        self.accuracylbl.setGeometry(QRect(1155,400,50,120))
        self.accuracylbl.setText("<font size=\"16\">%</font>")
        self.accuracylbl.setStyleSheet(_fromUtf8("background-color: rgb(201, 183, 255);"))
        self.setGeometry(10, 10, 1365,758)
        self.setStyleSheet(_fromUtf8("background-color: #25343B;")) #25343B
        self.setWindowTitle('SwiftTyper')
        self.show()
    

    def onChanged(self, text): 
        global positionOfCurrentWord
        global words
        global numberOfReds
        global numberOfChars
        global endOfCurrentWord
        global incrVertPosBy
        global lineReduce
        
        userInputWord=text
        if self.start==0:
            self.timeVariable=time.time()
            self.timer.start(100)
            self.start=1
        if stringmatch(userInputWord,currentWordFromPara[:len(userInputWord)]):
            #print "green"
            self.setStyleSheet(_fromUtf8("background-color: #25343B;"))
            numberOfChars+=1

            if words !=0 and lineNum >= 10:
                print "scroll value set to: " 
                #print float( words/lineNum * (lineNum/lineReduce)/(incrVertPosBy/words))
                print float( (numberOfChars/lineNum * words/lineReduce)/lineNum ) 
                self.lbl.verticalScrollBar().setValue((numberOfChars/lineNum * words/lineReduce)/lineNum)

        else:
            #print "red"
            if positionOfCurrentWord<len(paragraph): fill =  "<html><font color ='green' size=\"16\">"+str(paragraph[:positionOfCurrentWord - len(currentWordFromPara)]) + "<font color ='red' size=\"16\">"+str(currentWordFromPara)+"<font color ='black'size=\"16\"><font>" + str(paragraph[positionOfCurrentWord:]) + "</html>"
            else:  fill =  "<html><font color ='green' size=\"16\">"+str(paragraph[:positionOfCurrentWord-1 - len(currentWordFromPara)]) + "<font color ='red' size=\"16\">"+str(currentWordFromPara)+"<font color ='black'size=\"16\"><font>" + str(paragraph[positionOfCurrentWord:]) + "</html>"
            self.lbl.setText(fill)
            numberOfReds+=1
            self.setStyleSheet(_fromUtf8("background-color: rgb(200, 10, 10);"))
            numberOfChars+=1
            
        

        if len(userInputWord)==len(currentWordFromPara):
            if stringmatch(userInputWord,currentWordFromPara):
                self.lbl.setText(QApplication.translate("Dialog", "<html><head/><body><p><font color=\"green\" size=\"16\">"+str(paragraph[:positionOfCurrentWord])+"</font><font size=\"16\">"+str(paragraph[positionOfCurrentWord:])+"</font></p></body></html>", None, QApplication.UnicodeUTF8))
                a=updatecurrentWordFromPara()
                words+=1
                
                
                self.qle.clear()
                if a=="-1":
                    global speed
                    global tempfloat
                    self.timeVariable=time.time()-self.timeVariable
                    print "Your speed is "+str(int(60*words/self.timeVariable))+" words per minute"
                    print "Accuracy="+str(tempfloat)+"%"
                    self.timer.stop()
                    self.exitlbl.setText("<font size=\"15\" color=\"white\">"+str(speed)+" Words per minute</font>")
    

def main():
    
    updatecurrentWordFromPara()
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
