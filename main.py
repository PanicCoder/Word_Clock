import datetime as dt
import time
run = True
class Time():
    def __init__(self):
        self.time=None
        self.f_time=[]
        #Formats time to hours, minutes and seconds

    def format_time(self):
        self.f_time=dt.datetime.now().strftime('%H:%M:%S')
        return self.f_time[:-3]

    def get_time(self):
        return self.format_time()

class Format(Time):

    def __init__(self):
        self.t = Time.get_time(self)
        #positions for the needed letters
        self.pos={
            "fünf":[0,7,10],
            "zehn":[1,0,3],
            "zwanzig":[1,4,10],
            "drei":[2,0,3],
            "viertel":[2,4,10],
            "vor":[3,0,2],   
            "nach":[3,7,10],
            "halb":[4,0,3],
            "elf":[4,5,7],
            "fünf2":[4,7,10],
            "ein":[5,0,2],
            "eins":[5,0,3],
            "zwei":[5,7,10],
            "drei2":[6,0,3],
            "vier":[6,7,10],
            "sechs":[7,0,4],
            "acht":[7,7,10],
            "sieben":[8,0,5],
            "zwölf":[8,6,10],
            "zehn2":[9,0,3],
            "neun":[9,3,6],
            "uhr":[9,8,10]
        }
        stunde = str(self.t).split(":")[0]
        self.array_word=["zwölf","eins","zwei","drei2","vier","fünf2","sechs","sieben","acht","neun","zehn2","elf","zwölf","eins","zwei","drei2","vier","fünf2","sechs","sieben","acht","neun","zehn2","elf"]
        self.blueprint_f=[["ein","uhr"]if stunde =="01" or stunde == "13" else [self.array_word[int(stunde)],"uhr",1],
                        ["fünf","nach",self.array_word[int(stunde)],2],
                        ["zehn","nach",self.array_word[int(stunde)],3],
                        ["viertel","nach",self.array_word[int(stunde)],4],
                        ["zwanzig","nach",self.array_word[int(stunde)],5],
                        ["fünf","vor","halb",self.array_word[int(stunde)]if stunde != "23" else "zwölf",6],
                        ["halb",self.array_word[int(stunde)]if stunde != "23" else "zwölf",7],
                        ["fünf","nach","halb",self.array_word[int(stunde)]if stunde != "23" else "zwölf",8],
                        ["zwanzig","vor",self.array_word[int(stunde)]if stunde != "23" else "zwölf",9],
                        ["viertel","vor",self.array_word[int(stunde)]if stunde != "23" else "zwölf",10],
                        ["zehn","vor",self.array_word[int(stunde)]if stunde != "23" else "zwölf",11],  
                        ["fünf","vor",self.array_word[int(stunde)]if stunde != "23" else "zwölf",12],
                        ["ein","uhr"]if stunde =="01" or stunde == "13" else [self.array_word[int(stunde)],"uhr",13],                        
        ]
        self.steps=[57,3,8,13,18,23,28,32,37,42,47,52,57]
        self.f = [[0,0,1], 
                [0,3,5]] 
                
    def try_format(self):
        self.__init__()
        self.t = Time.get_time(self)
        
        #looks through all elements in steps and calls the check_range method for every value
        for a in range(int(len(self.steps)-1)):
            if(self.check_range(int(str(self.t).split(":")[-1]),self.steps[a],self.steps[a+1])):
                var = self.blueprint_f[a]
                for elements in var[:-1]:
                    self.f.append(self.pos[elements])
                return var[-1]

    # check if the num is inbetween the min and max value and return true or false if so
    def check_range(self,num,min,max):
        return num >= min and num <= max

    def get_format(self):
        self.try_format()
        return self.f

class board():
    def __init__(self):
        self.board=[['E', 'S', 'K', 'I','S','T','A','F','Ü','N','F'], 
                    ['Z', 'E', 'H', 'N','Z','W','A','N','Z','I','G'],
                    ['D', 'R', 'E', 'I','V','I','E','R','T','E','L'],
                    ['V', 'O', 'R', 'F','U','N','K','N','A','C','H'],
                    ['H', 'A', 'L', 'B','A','E','L','F','Ü','N','F'],
                    ['E', 'I', 'N', 'S','X','A','M','Z','W','E','I'],
                    ['D', 'R', 'E', 'I','P','M','J','V','I','E','R'],
                    ['S', 'E', 'C', 'H','S','N','L','A','C','H','T'],
                    ['S', 'I', 'E', 'B','E','N','Z','W','Ö','L','F'],
                    ['Z', 'E', 'H', 'N','E','U','N','K','U','H','R'],]

    def draw_the_board(self,to_format):
        last_format=None 
        i=0
        _row=to_format[0][0]
        s_column=to_format[0][1]
        e_column=to_format[0][2]
        #iterates through all rows and colums of the board and checks if its within the formated board -> prints the Char in red Color
        for row in range(len(self.board)):
            if len(self.board[row])==11:
                print()
            for columns in range(len(self.board[row])):
                if row ==_row and columns >=s_column and columns<= e_column:
                        print("\033[91m"+str(self.board[row][columns])+"\033[0;0m", end=" ")
                        if columns != 11:
                            if columns == e_column:
                                if to_format[i][0] == last_format or last_format==None:          
                                    j=0
                                    try:
                                        _row=to_format[i+1][j]
                                        s_column=to_format[i+1][j+1]
                                        e_column=to_format[i+1][j+2]
                                        last_format=to_format[i+1][0]
                                    except IndexError:
                                        pass
                                i+=1        
                else:
                    print(str(self.board[row][columns]), end=" ")
        print()
f=Format()
change = None

#loops the try_fomat() method to see if any change hppend -> calls the board to update the text
def main():
    global change
    if f.try_format()!=change:
        if change!=None:
            print("\n"*100)
        board().draw_the_board(f.get_format())
        change=f.try_format()
    else:
        change=f.try_format()
if __name__=="__main__":
    while run:
        main()
        time.sleep(1)

        