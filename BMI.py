height = input('请输入您的身高(cm): ')
weight = input('请输入您的体重(kg): ')
height = float(height)
weight = float(weight)
height = height / 100
BMI = weight / height / height
BMI = float('%.2f' % BMI)
if BMI < 18.5:
	print('体重过轻')
elif BMI >= 18.5 and BMI <= 24:
	print('正常范围')
elif BMI >=24 and BMI <27:
	print('您的BMI指数为： ',BMI,'过重')
elif BMI >=27 and BMI <30 :
	print('轻度肥胖')
elif BMI >=30 and BMI <35:
	print('中度肥胖')
else:
	print('重度肥胖')