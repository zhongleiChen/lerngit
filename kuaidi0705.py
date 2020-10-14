while 1==1:
	print("地址编号东三省为0，宁夏为1，青海为2，海南为3，\n新疆为4，西藏为5，港澳台为6，国外为7，其他为8");
	dizhi=int(input("请输入你的地址编号")); 
	zhongliang=float(input("请输入你的快递重量")); 
	if zhongliang<=3: 
		if dizhi<=3: 
			money=12*zhongliang 
		elif dizhi<=5:
			money=20*zhongliang 
		elif dizhi<=7: 
			money=0 
			print("对不起，不接收小于三公斤的国际快递")
		elif dizhi<=8: 
			money=10*zhongliang 
		else: print("请输入正确的地址编号") 
	else: 
		if dizhi<=3: 
			money=12*3+(zhongliang-3)*10 
		elif dizhi<=5:
			money=20*zhongliang 
		elif dizhi<=7: 
			money=0 
			print("联系总公司") 
		elif dizhi<=8: 
			money=10*3+(zhongling-3)*5 
		else: print("请输入正确的重量")
	print("您所寄快递费用为：",money)
