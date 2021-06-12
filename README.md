# POCKEMON DATABASE
## Contributors:
**19SE-1**
* ***Pavlova Daria*** 
* ***Khoroshilova Marina***

#### Придумать свою предметную область и продумать схему БД для неё.
	В качестве предсметной области мы выбрали реализацию Покедекса - энциклопедии по покемонам. Таблица pokedex хранит уникальный
	номер покемона в покедексе, имя на русском и английском языке, принадлежность к одной из пяти стихий(элементов), 
	тип покемона(например рыба), а также его рост и принадлежность к одной из трёх весовых категорий. От элемента зависит атака
	покемона, соотвественно таблица elements содержит показатель атаки для каждого элемента, а также total - число покемонов
	этого элемента, зарегестрированных в покедексе на данный момент. Количество здоровья покемона зависит от его весовой
	категории, таблица healths хранит показатель здоровья для каждой категории. Схема представлена ниже.
	
    
![alt text](https://github.com/jswark/dataBaseProject/blob/readme/new_schema.jpg)​

#### Критерии к БД:
**[1]** БД должна быть в третьей нормальной форме или выше;

*
 
**[2]** Минимальное количество таблиц – две;

* Созданная база данных состоит из 3х таблиц 

**[3]** Все подключения из GUI должны осуществляться выделенным, не root, пользователем;

* 

**[4]** Должен существовать как минимум один индекс, 
    созданный вами по выбранному текстовому не ключевому полю;

* 

**[5]** В одной из таблиц должно присутствовать поле, заполняемое/изменяемое только триггером 
(например, «общая стоимость бронирования» в таблице «бронирования», которое автоматически 
высчитывается при добавлении/изменении/удалении билетов, входящих в это бронирование)

*

#### Реализовать программу GUI со следующим функционалом:
**[1]** Создание базы данных (важно(!) именно create database, а не только create table) 
* 
**[2]** Удаление базы данных  
*
**[3]** Вывод содержимого таблиц  
*
**[4]** Очистка(частичная - одной, и полная - всех) таблиц  
*
**[5]** Добавление новых данных  
*
**[6]** Поиск по заранее выбранному (вами) текстовому не ключевому полю  
*
**[7]** Обновление кортежа  
*
**[8]** Удаление по заранее выбранному текстовому не ключевому полю  
*
**[9]** Удаление конкретной записи, выбранной пользователем  
*
**[10]** Все функции должны быть реализованы как хранимые процедуры. 
* 

![icons8-pikachu-pokemon-96](https://user-images.githubusercontent.com/55359172/121788046-d6aa7c80-cbd2-11eb-8a66-7bf7121a7305.png)


#### Демонтрация работы 
