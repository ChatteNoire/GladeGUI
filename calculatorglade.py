import sys
try:
	import pygtk
	pygtk.require('2.0')
except:
	pass
try:
	import gtk
	import gtk.glade
except:
	print('GTK not available')
	sys.exit(1)

class Calculator:
	def __init__(self):
		self.gladefile = "calculator.glade"
		self.wTree = gtk.glade.XML(self.gladefile)
		dic = {
			"on_window_calculator_destroy" :self.quit,
			"on_close_clicked" : self.quit,
			"on_CE_clicked" : self.displayCE,
			"on_Clear_clicked" : self.displayClr,
			"on_Modulus_clicked" : self.displayMod,
			"on_Seven_clicked" : self.displaySeven,
			"on_Eight_clicked" : self.displayEight,
			"on_Nine_clicked"  : self.displayNine,
			"on_Divide_clicked" : self.displayDiv,
			"on_Four_clicked" : self.displayFour,
			"on_Five_clicked" : self.displayFive,
			"on_Six_clicked" : self.displaySix,
			"on_Multiply_clicked" : self.displayMultiply,
			"on_One_clicked" : self.displayOne,
			"on_Two_clicked" : self.displayTwo,
			"on_Three_clicked" : self.displayThree,
			"on_Minus_clicked" : self.displayMinus,
			"on_Zero_clicked" : self.displayZero,
			"on_Dot_clicked" : self.displayDot,
			"on_Equal_clicked" : self.displayEqual,
			"on_Add_clicked" : self.displayAdd,
			}
		self.wTree.signal_autoconnect(dic)
		self.window = self.wTree.get_widget("window_calculator")
		self.window.show()

	def displayOperand(self,operand):
		self.wTree.get_widget("displayText").insert_text(operand,position=20)

	def compute(self,operator):
		if operator == 'Clr':
			self.wTree.get_widget("displayText").set_text("")
		if operator == 'CE':
			self.wTree.get_widget("displayText").set_text("0")	
		if operator == "+":
			self.flag = 1
			self.firstOperand = self.wTree.get_widget("displayText").get_text()
			self.wTree.get_widget("displayText").set_text("")
		if operator == '-':
			self.flag = 2
			self.firstOperand = self.wTree.get_widget("displayText").get_text()
			self.wTree.get_widget("displayText").set_text("")
		if operator == '*':
			self.flag = 3
			self.firstOperand = self.wTree.get_widget("displayText").get_text()
			self.wTree.get_widget("displayText").set_text("")
		if operator == '/':
			self.flag = 4
			self.firstOperand = self.wTree.get_widget("displayText").get_text()
			self.wTree.get_widget("displayText").set_text("")
		if operator == '%':
			self.flag = 5
			self.firstOperand = self.wTree.get_widget("displayText").get_text()
			self.wTree.get_widget("displayText").set_text("")
		if operator == '=':
			self.secondOperand = self.wTree.get_widget("displayText").get_text()
			sum1 = float(self.firstOperand)
			sum2 = float(self.secondOperand)
			if self.flag == 1:
				result = sum1 + sum2
			if self.flag == 2:
				result = sum1 - sum2
			if self.flag == 3:
				result = sum1 * sum2
			if self.flag == 4:
				if sum2 == 0.0:
					try:
						result = sum1 / sum2
					except:						
						result = "Math operation error"
				else:
					result = sum1 / sum2
			if self.flag == 5:
				sum1 = int(sum1)
				sum2 = int(sum2)
				result = sum1 % sum2
			self.wTree.get_widget("displayText").set_text(str(result))
	
	def displayClr(self,widget):
		self.compute("Clr")

	def displayCE(self,widget):
		self.compute("CE")	

	def displaySeven(self,widget):
		self.displayOperand("7")

	def displayEight(self,widget):
		self.displayOperand("8")

	def displayNine(self,widget):
		self.displayOperand("9")
	
	def displayFour(self,widget):
		self.displayOperand("4")

	def displayFive(self,widget):
		self.displayOperand("5")

	def displaySix(self,widget):
		self.displayOperand("6")

	def displayOne(self,widget):
		self.displayOperand("1")

	def displayTwo(self,widget):
		self.displayOperand("2")

	def displayThree(self,widget):
		self.displayOperand("3")

	def displayZero(self,widget):
		self.displayOperand("0")

	def displayDot(self,widget):
		self.displayOperand(".")	

	def displayMod(self,widget):
		self.compute("%")	
	
	def displayDiv(self,widget):
		self.compute("/")	

	def displayMultiply(self,widget):
		self.compute("*")
	
	def displayMinus(self,widget):
		self.compute("-")
	
	def displayEqual(self,widget):
		self.compute("=")

	def displayAdd(self,widget):
		self.compute("+")

	def quit(self,widget):
		sys.exit(0)

if __name__ == "__main__":	
	cal = Calculator()
	gtk.main()
	
	
