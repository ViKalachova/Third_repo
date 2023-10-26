from datetime import date, timedelta



def get_birthdays_per_week(users):
    week = []                                                    #список з днями тижня від сьогоднішнього дня
    week_1 = []                                                  #список з переліком дат від сьогоднішнього дня
    today_date = date.today()                       
    counter = 0
    while counter < 7:
        one_day = timedelta(days = counter)
        next_day = today_date + one_day
        week_1.append(next_day)
        name_weekday = next_day.strftime('%A')
        week.append(name_weekday)
        counter += 1
    date_dict = dict(zip(week, week_1))                          #створюємо словник, де ключ - це день тижня, а значення - це дата
    filter_date_in_dict = []                                     #список дат, що буде віключено до понеділка (субота, неділя, понеділок)
    for d, a in date_dict.items():
         if d == 'Saturday' or d == 'Sunday' or d == 'Monday':   
              filter_date_in_dict.append(a)                  
    del date_dict['Saturday']                                    #видаляємо ключ з пустим значенням суботи
    del date_dict['Sunday']                                      #видаляємо ключ з пустим значенням неділі
    date_dict['Monday'] = filter_date_in_dict                    #дадаємо у словник ключ - понеділок, з усіма вираними датами

    need_bithday_date = []                                       #створюємо список з відфільтрованими співробітниками, що мають день народження на цьому тижні
    for e in week_1:
         e = e.strftime('%d.%m')                                 #переводимо сьогоднішню дату до типу строка 
         for element in users:                                   #беремо словник зі списку, що був за умовою                     
            for key, value in element.items():                   
                if key == 'birthday':                            #вибираэмо значення лише за ключем 'birthday'
                     value_day = value.strftime('%d.%m')         #приводимо значення до типу, що й сьогоднішня дата (для порівняння)
                     if value_day == e:
                          need_bithday_date.append(element)      #додаємо словник(що задовільнив усі умови) до нового списку

    dict_with_name_date = {}                                     #строримо словник, де значення по ключу 'name' стане ключем словника 'dict_with_name_date', а значення по ключу 'birthday' стане значенням словника 'dict_with_name_date'
    for elements in need_bithday_date:                           #беремо перший словник у відсортованому списку
        list_with_name_date = []                                 #створюємо список з ключем та значенням для нового словника
        for value in elements.values():                          #дістаємо значення з обох ключів
                list_with_name_date.append(value)
        dict_with_name_date[list_with_name_date[0]] = list_with_name_date[1]

    users = {}                                                   #створюємо підсумовуючий словник, де ключем буде день тижня, а значенням список співробітників
    if dict_with_name_date == 0:                                 #додамо умову, якщо буде відсутнє вхідне значення 'users' або на цьомц тижні не має день народження у жодного зі співробітників
         return {}
    else:
        for w, day in date_dict.items():                         #беремо словник 'день тижня: дата'
            list_with_person = []                                #створюємо список, аби записати усіх співробітників ітерованого дня
            users[w] = list_with_person                          #додаємо у підсумовуючий словник ключ - день тижня, значення - список співробітників
            if w == 'Monday':                                    #додаємо перевірку для понеділка, адже у понедок збережено декілька дат
                 for m_day in day:
                      m_day = m_day.strftime('%d.%m')
                      for person, birthday in dict_with_name_date.items():
                           birthday = birthday.strftime('%d.%m')
                           if birthday == m_day:
                                list_with_person.append(person)
                      
            else:
                 day = day.strftime('%d.%m')                     #переводимо дату до типу строка
                 for person, birthday in dict_with_name_date.items():  #дістаємо значення з відфільтрованого словника зі співробітниками
                      birthday = birthday.strftime('%d.%m')
                      if birthday == day:                        #якщо дата народження співробітника буду дорівнювати даті на цьому тижні(словник 'date_dict')
                           list_with_person.append(person)       #додажмо співробітника до списку співробітників, що народилися у ітерований день

        users = {k:v for (k, v) in users.items() if v}           #видаляємо зі словника дні тижня, які не мають співробітників
    return users
