print("hi")
#for i in range(0,8):
#	print(i)
coins=[2,5,7]
i=0;
#data=[]
len2=999999
num=0
num2=0
inputcoin= []
def dp(input=None,data=[]):
	value=[0]
	#value=value+[-1]
	length= 1+input
	inputcoin=[[]]
	global num2
	for i in range(1,length):
		value=value+[999]
		inputcoin=inputcoin+[[-1]]
		#print(inputcoin)
		for coin in coins:
			num2=1+num2
			if(i>=coin):
				if(value[i-coin]+1<value[i]):
					inputcoin[i]=inputcoin[i-coin]+[coin]
					value[i] = value[i-coin]+1;
	print("value is ",value)
	print("coin is ",inputcoin)
	print("num2 is ",num2)


def myfunc(input=None,data=[]):
	global i
	global len2
	#global data
	global num
	num=num+1
	data=data+[input]
	for coin in coins:
		#print (coin,":", input," ",end="")

		if (input ==0):
			if(len2 > len(data)):
				len2 = len(data)
				print(data)
				print("find it",len2)
				i=i+1
				if(i%8==0):
					print("\n")
			return
		if(input >=coin):		
			next = input-coin
			myfunc(next,data)			
		else:
			#print("not find it")
			return;
			
data=[]
a=myfunc(27,data)
dp(27,data)
print("myfunc is ",a)
print ("num is ",num)
print (coins,type(coins))