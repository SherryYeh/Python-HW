def BMI(w, h):
	return w/(h*h)
	print('BMI為', bmi)
w = float(input('請輸入體重(KG)？'))
h = float(input('請輸入身高(M)？'))
bmi = BMI(w, h)
