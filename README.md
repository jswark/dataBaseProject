# POCKEMON DATABASE
## Contributors:
**19SE-1**
* ***Pavlova Daria*** 
* ***Khoroshilova Marina***

#### Придумать свою предметную область и продумать схему БД для неё.
	
В качестве предметной области мы выбрали реализацию Покедекса - энциклопедии по покемонам. Таблица pokedex хранит уникальный
номер покемона в Покедексе, имя на русском и английском языке, принадлежность к одной из пяти стихий(элементов), 
тип покемона(например, рыба), а также его рост и принадлежность к одной из трёх весовых категорий. От элемента зависит атака
покемона, соотвественно таблица elements содержит показатель атаки для каждого элемента, а также total - число покемонов
этого элемента, зарегестрированных в Покедексе на данный момент. Количество здоровья покемона зависит от его весовой
категории, таблица healths хранит показатель здоровья для каждой категории. Схема представлена ниже.
	
    
![alt text](https://github.com/jswark/dataBaseProject/blob/readme/new_schema.jpg)​

#### Критерии к БД:
**[1]** БД должна быть в третьей нормальной форме или выше;

* Все условия соблюдены. Все атрибуты зависят от первичного ключа целиком, а не от какой-то его части. 
* Все атрибуты зависят от первичного ключа, но не от других атрибутов
 
**[2]** Минимальное количество таблиц – две;

* Созданная база данных состоит из 3х таблиц 

**[3]** Все подключения из GUI должны осуществляться выделенным, не root, пользователем;

* Подключаемся с помощью созданного пользователя jswark:
####
	engine = create_engine('postgresql://jswark:12345@localhost/new', echo=True)

**[4]** Должен существовать как минимум один индекс, 
    созданный вами по выбранному текстовому не ключевому полю;

* Обыявляем индексом имя покемона:
####
	Column('name_rus', String, nullable=False, index=True),

**[5]** В одной из таблиц должно присутствовать поле, заполняемое/изменяемое только триггером 
(например, «общая стоимость бронирования» в таблице «бронирования», которое автоматически 
высчитывается при добавлении/изменении/удалении билетов, входящих в это бронирование)

* Поле total в таблице elements обновляется триггером

![icons8-pikachu-pokemon-96](https://user-images.githubusercontent.com/55359172/121788046-d6aa7c80-cbd2-11eb-8a66-7bf7121a7305.png)

