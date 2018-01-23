from time import sleep
import vk_api
import random
# vk = vk_api.VkApi(login = 'login', password = 'password')
vk=vk_api.VkApi(token = 'cc487665d922ca1413eac02381daf09e0f52096a9ccad28207a91f189e6297cff14a8d939732e05ecccc0') #Авторизоваться как сообщество
# vk.auth()
values = {'count': 100,'time_offset': 100, 'read_state':0}

def write_msg(user_id, s, at):
	vk.method('messages.send', {'user_id':user_id,'message':s,'attachment':at})
dn={'Пн':'','Вт':'','':'','Ср':'' ,'Чт':'' ,'Пт':''}


while True:
	response = vk.method('messages.get', values)
	if response['items']:
		values['last_message_id'] = response['items'][0]['id']
		print(values)
	for item in response['items']:
		if 'Пн' in response['items'][0]['body']:
			write_msg(item['user_id'], 'Расписание на понедельник:','photo-159875078_456239020')

		if 'Вт' in response['items'][0]['body']:
			write_msg(item['user_id'], 'Расписание на вторник:','photo-159875078_456239024')

		if 'Ср' in response['items'][0]['body']:
			write_msg(item['user_id'], 'Расписание на среду:','photo-159875078_456239022')

		if 'Чт' in response['items'][0]['body']:
			write_msg(item['user_id'], 'Расписание на четверг:','photo-159875078_456239023')

		if 'Пт' in response['items'][0]['body']:
			write_msg(item['user_id'], 'Расписание на пятницу:','photo-159875078_456239021')

		if 'All' in response['items'][0]['body']:
			write_msg(item['user_id'], 'Расписание на неделю:','photo-159875078_456239018')
