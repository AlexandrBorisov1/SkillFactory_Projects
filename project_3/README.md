# Проект 3. EDA + Feature Engineering. Соревнование на Kaggle

## Оглавление  
[1. Описание проекта](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Результаты)    
[6. Выводы](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Выводы) 

### Описание проекта    
Представим, что мы работаем дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Оглавление)


### Какой кейс решаем?    
Нужно посредством разведовательного анализа и проектирования признаков добиться наилучшей метрики качества модели **RandomForestRegressor**.

**Что практикуем**     
Практикуемся проводить разведывательный анализ данных, проектирование, изменение и отбор признаков.


### Краткая информация о данных
Данные предоставленны на странице соревнования на [Kaggle](https://www.kaggle.com/competitions/sf-booking/data)
  
:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Оглавление)


### Этапы работы над проектом  
* загрузка и очистка данных;
* проектирование признаков;
* кодирование признаков;
* масштабирование данных;
* отбор признаков.
* обучение модели.
* предсказание на соревновательных данных
* отправка результата предсказания на Kaggle

:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Оглавление)

### Метрика качества 

Результаты оцениваются по метрике MAPE.

### Результаты:  
В ходе экспериментов удалось выяснить что удаление высоко-коррелированных признаков и масштабирование данных не улучшает метрику.



:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Оглавление)


### Выводы:  
Интересный проект, позволяющий множество разрозненных знаний в голове, перевести в структурированный алгоритм выполнения ML проекта.

С данным вариантом ноутбука добился метрики MAPE = 12.21639 в соревновании.

Возможно, при наличии свободного времени, попробую улучшить результат

:arrow_up:[к оглавлению](https://github.com/AlexandrBorisov1/SkillFactory_Projects/tree/master/project_3/README.md#Оглавление)


## Авторы

Борисов Александр Игоревич

* [VK](https://vk.com/id7127336)
* [YouTube](https://www.youtube.com/channel/UCBmroxXpM4zgYNm1uRY8Nrg)
* [Kaggle](https://www.kaggle.com/alexandrborisov0o)

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
