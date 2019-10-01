class myClass:
    
    def __init__(self, nameString):
        self.name = nameString
        self.inputtedString = ""
        #print("init")
        
    def getString(self):
        self.inputtedString = input("Please input a string: ")
        #print(self.inputtedString)
        #return inputtedString
        
    def printString(self):
        print(self.inputtedString.upper())
        #print("lol")


theClass = myClass("gabe")
theClass.getString()
theClass.printString()
