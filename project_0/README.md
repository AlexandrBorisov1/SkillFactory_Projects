# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Результат)    
[6. Выводы](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 10000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
Данные сгенерированны в библиотеке numpy.random
  
:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Оглавление)


### Этапы работы над проектом  
1. Подключил библиотеку numpy для генерации случайных чисел
2. Написал первую функцию отгадывания random_predict, которая просто выбирает случайное число от 1 до 100
3. Написал вторую функцию отгадывания game_core_v2, которая также выбирает число, учитывает > оно или < загаданного и в зависимости от этого увеличивает или уменьшает число на 1
4. Написал третью функцию отгадывания game_core_v3, которая сжимает диапозон выбора случайного числа, в зависимости от промаха.
5. Написал функцию подсчитывающую среднее количество попыток отгадывания числа

:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Оглавление)


### Результаты:  
1. random_predict отгадывает в среднем за 100 попыток
2. game_core_v2 отгадывает в среднем за 32 попытки
3. game_core_v3 отгадывает в среднем за 7 попыток

:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Оглавление)


### Выводы:  
game_core_v3 отгадывает быстрее всех.

:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/blob/master/project_0/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
