import json



class Note(object):
     
    def __init__(self):
        self.author_name = []
        self.note = []
        self.rating = []
        
    def createNewNote(self):
        print("Create new note")
        self.author_name.append(input("Enter author's name: "))
        self.note.append(input("Enter note: "))
        self.rating.append(input("Enter reting(from 0 to 1): "))
        self.writeToFile()

    def loadFromFile(self):
        ai=0
        ni=0
        ri=0        
        with open('microlibnotes.json') as file:
            allNotes = json.load(file)
            for header, content in allNotes.items():
                if header == "author_name":
                    while ai < len(content):
                        self.author_name.append(content[ai])
                        ai+=1        
                elif header == "note":
                    while ni < len(content):
                        self.note.append(content[ni])
                        ni+=1
                elif header == "rating":
                     while ri < len(content):
                        self.rating.append(content[ri])
                        ri+=1
   

    def printToConsole(self, control ):
        ai=0        
        def printEntry(self):
            print("__________________________________________________")
            print(ai , " | " , self.author_name[ai] , " | rating: " , self.rating[ai], " | ")
            print("__________________________________________________")
            print(self.note[ai])
            print("__________________________________________________\n")
        if control=="avr":
            print("Avarage rating of author's is: " , self.FindAvr())
        while ai < len(self.rating):
            if control == "all":
                printEntry(self)
            elif control=="max":
                if self.rating[ai]==max(self.rating):
                    print("Maximum rating of author's is: " , max(self.rating))
                    printEntry(self)
            elif control=="min":
                if self.rating[ai]==min(self.rating):
                    print("Minimum rating of author's is: " , min(self.rating))
                    printEntry(self)
            elif control=="avr":
                if float(self.rating[ai])>=self.FindAvr()-0.05 and float(self.rating[ai])<=self.FindAvr()+0.05:
                    printEntry(self)
            ai+=1

    def writeToFile(self):
        toJson={ "author_name": self.author_name ,"note": self.note ,"rating": self.rating}
        with open('microlibnotes.json', 'w') as file: 
            json.dump(toJson,file)


    def FindAvr(self):
        ri=0
        avr=0
        while ri < len(self.rating):
            avr+=float(self.rating[ri])
            ri+=1
        return avr/float(len(self.rating))
            
     
   
    


note1=Note()
note1.loadFromFile()

exit=0
while exit==0:
    print("_____MicroLibrary1.0_____")
    print("1 - List all notes; 2 - Create new note; 3 - Find note with lowest rating;")
    print("4 - Find note with higtest rating; 5 - Find avarage rating of existing notes; 0 - Exit")
    ct=int(input())
    print(ct)
    if ct==1:        
        note1.printToConsole("all")
        input("press any key to continue....")
    elif ct==2:
        note1.createNewNote()
        input("press any key to continue....")
    elif ct==3:
        note1.printToConsole("min")
        input("press any key to continue....")
    elif ct==4:
        note1.printToConsole("max")
        input("press any key to continue....")
    elif ct==5:
        note1.printToConsole("avr")
        input("press any key to continue....")
    elif ct==0:
        exit=1



