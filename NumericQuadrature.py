import kivy.app
import kivy.uix.label
import kivy.uix.textinput
import kivy.uix.button
import kivy.uix.boxlayout


		
def start_ini(f, a, b, k, tol):
	
		def recursiveTrapezoid(ii, I_old):
			if ii == 1:
				I_new= (f(a)+f(b)) * (b-a)/2.0
			else:
				n=2**ii-2
				h=(b-a)/n
				x=a + h/2.0
				sum=0.0
				for i in range(0, n):
					sum+=f(x)
					x=x+h
				I_new= (I_old + h*sum)/2.0
			return I_new	
	
		I_new=0.0 ; I_old=0.0
		R = 1.e50
		for i in range (k):
			I_new=recursiveTrapezoid(i+1, I_new)
			R=abs(I_old-I_new)
			if R < tol:
				break
			I_old=I_new
		I=I_old

		return I, i+1, R
		

		
def f(x):
	return pow(x, -1)
	
class KivyApp(kivy.app.App):
	
	
	def button_a_press(self, button_pressed):
		self.a=float(self.A.text)
	
	def button_b_press(self, button_pressed):
		self.b=float(self.B.text)
		k=50; tol=0.0001; a=self.a; b=self.b
		I, trials, R=start_ini( f, a, b, k, tol)
		
		if trials == k:
			self.text_label.text="The number of trials execeeded %d, the result of the integration f(1/x) reached is %f with precision %f" %(k,I,R)
			with open ("The results.txt", 'a') as outFile:
				outFile.write(f"\n The number of trials exceeded {k}, the result of the integration f(1/x) reached is {I} with precision {R}")
		else:
			self.text_label.text="The result of the integration f(1/x) is {0} after {1} trials".format(I,trials)	
			with open ("The results.txt", 'a') as outFile:
				outFile.write(f"\n The result of the integration f(1/x) is {I} after {trials} trials")		
	
	
	def build(self):
		self.text_label=kivy.uix.label.Label(text="Numeric Quadrature of f(1/x)")
		
		self.A=kivy.uix.textinput.TextInput(text="")
		self.B=kivy.uix.textinput.TextInput(text="")
		button_a=kivy.uix.button.Button(text="Click to Insert lower bound(a)")
		button_b=kivy.uix.button.Button(text="Click to Insert Upper bound(b)")
		button_a.bind(on_press=self.button_a_press)
		button_b.bind(on_press=self.button_b_press)
		
		box_layout=kivy.uix.boxlayout.BoxLayout(orientation="vertical")
		
		box_layout1=kivy.uix.boxlayout.BoxLayout(orientation="horizontal")
		box_layout1.add_widget(widget=button_a)
		box_layout1.add_widget(widget=self.A)

		
		box_layout2=kivy.uix.boxlayout.BoxLayout(orientation="horizontal")
		box_layout2.add_widget(widget=button_b)
		box_layout2.add_widget(widget=self.B)

		
		box_layout.add_widget(widget=self.text_label)
		box_layout.add_widget(widget=box_layout1)
		box_layout.add_widget(widget=box_layout2)
		return box_layout
		
	
	

		
if __name__=="__main__":
	
	obj=KivyApp()
	obj.run()
