import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
from bs4 import BeautifulSoup
import json

# API токен сообщества
mytoken=''
url = ''
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36 OPR/74.0.3911.218'
      }
# Функция посылающая сообщение
def write_msg(user_id, message, keyboard):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id, "keyboard": keyboard1})

def parser():
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    news_list = soup.find('div', {'class':"info"}).find('a').text
    halflink = soup.find('div', {'class':"info"}).find('a').get('href')
    link = '{}{}'.format('https://cchgeu.ru/', halflink)
    data = soup.find('div', {'class':"info"}).find('span').text
    msg = '{} \n \n {} \n \n Ссылка на новость: {}'.format(data, news_list, link)
    return msg

def parser5msg():
    response = requests.get(url)                        #подключились к сайту
    html = response.content                             #взяли весь хтмл файл
    soup = BeautifulSoup(html, "html.parser")           #переменная ктороя имеет в себе весь текст
    novostey5 = []                                      #список для будущих 5 записей 
    dat5 = []                                           #список для будущих 5 дат
    link5 = []                                          #список для будущих 5 ссылок
    msg = str()                                                   #переменная в которой будет уже весь текст сообщения, т.е. 5 новостей
    news_list = soup.find_all('div', {'class':"middle"})[0]       #взяли блок со всеми дивами
    div_list = news_list.find_all('div', {'class':"info"})        #нашли из прошлого блока дивы что имеют класс инфо
    for new in div_list:                                          #начинаем перебирать значения дивов с классом инфо
        text = new.find('a', {'class':'name'}).text                #ищем там текст для 1 новости
        dat = new.find('span', {'class':'badge'}).text             #ищем там дату для 1 новости
        halflink = new.find('a').get('href')                     #ищем части ссылки на 1 новость
        novostey5.append(str(text))           #добавляем в созданый список по 1 записи
        dat5.append(str(dat))                 #добавляем в созданый список по 1 записи
        link5.append(str(halflink))           #добавляем в созданый список по 1 записи
    for q in range(11, 4, -1):                #убираем из списка ненужные 7 ностей
        novostey5.pop(q)                      #удаляем последний не нужный елемент списка
        dat5.pop(q)                           #удаляем последний не нужный елемент списка
        link5.pop(q)                          #удаляем последний не нужный елемент списка
    for num in range(5):                      #цикл чтобы создать уже итоговую переменную с сообщением
        full_link = '{}{}'.format('https://cchgeu.ru/', link5[num])                #делаем ссылку нормально, т.е. целой
        msghalf = '{} \n \n {} \n \n Ссылка на новость: {} \n \n -------------------------'.format(dat5[num], novostey5[num],full_link )   #создаем 1 сообщение 
        msg ='{} \n {}'.format(msg, msghalf)        #прибавляем его к всему уже созданому сообщению
    return msg                 #возвращаем функции наше большое сообщение
    

 


# Авторизуемся как сообщество
vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            request
            num_key = 0
            # Логика формирования ответа бота
            if((str('Последние 5 новостей').lower() in request.lower() or (str('Новости').lower()) in request.lower())):
                otvet = parser5msg()
                num_key = 0
            elif (str('Последняя новость').lower() in request.lower() or (str('Новость').lower() in request.lower())):
                otvet = parser()  
                num_key = num_key + 1
            elif (str('Начать').lower() in request.lower()): 
                otvet = (''' Привет! Это бот с новостями ВГТУ. 
                        Если ты хочешь получить последнюю новость, напиши "Новость". Если ты хочешь получить последние 5 новостей, напиши "Новости".
                        Также ты можешь воспользоваться клавиатурой. ''')
            else:
                otvet='Я такое не понимаю'

            if num_key == 0:    
                write_msg(event.user_id, otvet, keyboard)
                print('1')
            else:
                write_msg(event.user_id, otvet, keyboard1)
                print('9')