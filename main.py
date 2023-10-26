from datetime import date, datetime, timedelta



def get_birthdays_per_week(users):
    week = []
    week_1 = []
    today_date = datetime.now().date()
    counter = 0
    while counter < 7:
        one_day = timedelta(days = counter)
        next_day = today_date + one_day
        week_1.append(next_day)
        name_weekday = next_day.strftime('%A')
        week.append(name_weekday)
        counter += 1
    date_dict = dict(zip(week, week_1))
    filter_date_in_dict = []
    for d, a in date_dict.items():
         if d == 'Saturday' or d == 'Sunday' or d == 'Monday':
              filter_date_in_dict.append(a)
    del date_dict['Saturday']
    del date_dict['Sunday']
    date_dict['Monday'] = filter_date_in_dict

    need_bithday_date = []
    for e in week_1:
         e = e.strftime('%d.%m')                           #переводимо сьогоднішню дату до типу строка 
         for element in users:                             #беремо словник зі списку                      
            for key, value in element.items():             #дістаємо усі ключі та значення
                if key == 'birthday':                      #вибираэмо значення лише за ключем 'birthday'
                     value_day = value.strftime('%d.%m')   #приводимо значення до типу, що й сьогоднішня дата (для порівняння)
                     if value_day == e:
                          need_bithday_date.append(element)  #додаємо словник(що задовільнив усі умови) до нового списку
    
    dict_with_name_date = {}                                #строримо словник, де значення по ключу 'name' стане ключем словника 'dict_with_name_date', а значення по ключу 'birthday' стане значенням словника 'dict_with_name_date'
    for elements in need_bithday_date:                      #беремо перший словник у відсортованому списку
        list_with_name_date = []                            #створюємо список з ключем та значенням для нового словника
        for value in elements.values():                     #дістаємо значення з обох ключів
                list_with_name_date.append(value)
        dict_with_name_date[list_with_name_date[0]] = list_with_name_date[1]

    result_dict = {}
    if not users or dict_with_name_date == 0:
         return {}
    else:
        for w, day in date_dict.items():
            list_with_person = []
            result_dict[w] = list_with_person
            if w == 'Monday':
                 for m_day in day:
                      m_day = m_day.strftime('%d.%m')
                      for person, birthday in dict_with_name_date.items():
                           birthday = birthday.strftime('%d.%m')
                           if birthday == m_day:
                                list_with_person.append(person)
                      
            else:
                 day = day.strftime('%d.%m')
                 for person, birthday in dict_with_name_date.items():
                      birthday = birthday.strftime('%d.%m')
                      if birthday == day:
                           list_with_person.append(person)

        result_dict = {k:v for (k, v) in result_dict.items() if v}
    return result_dict