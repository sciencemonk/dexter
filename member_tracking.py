import time

members = {
	"1234" : ["michael",1551650375.540954,2],
	"1235": ["evan",0,10],
	"1236": ["bryant",0,"unlimited"]
}

print(members)
rfid_num = 1234
duration = 0

for key,value in members.items():
	if str(rfid_num) == key and value[1] == 0:
		print('Hello {}'.format(value[0]))
		value[1] = time.time()
		break
	elif str(rfid_num) == key and value[2] == "unlimited":
		print('Good bye {}'.format(value[0]))
		duration = (time.time() - value[1]) / 3600 
		print("Duraton of visit: {} hours".format(round(duration,2)))
		value[1] = 0
		break
	elif str(rfid_num) == key and value[1] != 0:
		print('Good bye {}'.format(value[0]))
		duration = (time.time() - value[1]) / 3600 
		print("Duraton of visit: {} hours".format(round(duration,2)))
		print('Time left: {}'.format(round(value[2]-duration),2))
		value[1] = 0
		break
