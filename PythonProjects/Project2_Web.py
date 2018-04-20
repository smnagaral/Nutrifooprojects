import wikipedia
import warnings

warnings.filterwarnings("ignore")

def getInput():
	return input("Enter the periodic element to know its details\n")	

def getInformation(periodicElement):
	try:
		information = wikipedia.summary(periodicElement, sentences=2)
	except:
		print ("Invalid keyword\n")
		periodicElement = getInput()
		information = getInformation(periodicElement)
	return information

def printData(information):
	print(information)

periodicElement = getInput()
information = getInformation(periodicElement)
printData(information)