# Task_for_X5
Задание для X5 retail group



### ***Как запускать:***

(Предварительно нужно заполнить файл config.py, раздел "for sql:" - данные для подключения бд (Postgresql))

1. Активация виртуального окружения:

   Для активации виртуального окружения воспользуйтесь командой (для Linux):

    >source venv/bin/activate

   для Windows команда будет выглядеть так:

    >venv\Scripts\activate.bat

2. Выполняем установку зависимостей:
    >pip install -r requirements.txt

3. запускаем, как flask-приложение:

    >python app.py
 
### **Описание некоторых файлов:**
 
 _SQL_scheme.txt_ - схема таблиц, для того, чтобы можно было сравнить с заданием, если будут расхождения
 
 _crutches.py_ - все "костыли", котоыре всплывали в ходе разработки и пока неисправленные (в основоном это обработчики строк).
 
 _config.py_ - конфигурация для бд, логин и пароль для Basic_HTTP_authentication.py, который нужно придумать самому
 
 _Basic_HTTP_authentication.py_ (защита логином и паролем закоменчена, но существует для всех запросов, связанных с добавлением/удалением/изменением данных): 
 
           Функция get_password будет по имени пользователя возвращать пароль.

           Функция error_handler будет использоваться чтобы отправить ошибку авторизации, при неправильных данных.
           
### ***Описание API:***

###### GET_requests.py - все GET запросы:


_.../api/v1.0/processes_ - показать все процессы из таблицы "Process" в виде json.

Пример:
>$ curl -i http://localhost:5000/api/v1.0/processes
        ![screenshot of sample](https://i.imgur.com/tMsdjzg.png)

_.../api/v1.0/processes/<int:id>_ (где id - любой индекс (pk), существующий в таблице "Process") - показать конкретный процесс в виде json. 

Пример:
>$ curl -i http://localhost:5000/api/v1.0/processes/6
        ![screenshot of sample](https://i.imgur.com/d674QzC.png)
        
###### POST_requests.py - все POST запросы:


_.../api/v1.0/processes_ - добавляет новый процесс в таблицу "Process", эквивалентен INSERT запросу в бд, необходимо указать минимальные NOT NULL колонки.

Пример:
>$ curl -i -H "Content-Type: application/json" -X POST -d '{"process_id": 1}' http://localhost:5000/api/v1.0/processes
Добавит в таблицу новый процесс с id = 1, остальные колонки будут равны null
                     ![screenshot of sample](https://i.imgur.com/CcqVdBa.png)

_.../api/v1.0/processes/<int:process_id>/<table_name>_ (где process_id - любой индекс (pk), существующий в таблице "Process") - заполняет остальные таблицы,необходимо указать минимальные NOT NULL колонки.
 
Пример:
>$ curl -i -H "Content-Type: application/json" -X POST -d '{"quota_id": 15}' http://localhost:5000/api/v1.0/processes/1/process_quota

![screenshot of sample](https://i.imgur.com/hZUJ2yl.png)

###### PUT_requests.py - все PUT запросы:

_.../api/v1.0/processes/<int:process_id>/<table_name>/upd_ (где process_id - любой индекс (pk), существующий в таблице "Process") - 
К сожалению не очень функциональный запрос т.к. запрос UPDATE по структуре может быть сложным. Этот запрос эквиваленте запросу :
      
      UPDATE {table_name} SET {json} WHERE {id} = {process_id},
      
который находит записи с id = process_id и обновляет любое количество колонок существующей записи

###### DELETE_requests.py - все DELETE запросы:

_.../api/v1.0/processes/<int:process_id>/<table_name>/del_ (где process_id - любой индекс (pk), существующий в таблице "Process") - удаляет любую запись, если это возможно.
Как и с UPDATE-ом, DELETE запрос может быть сложен по структуре, поэтому функционал минимален и равносилен следующему запросу:

      DELETE FROM {table_name} WHERE {id} = {process_id}


 
           
           
