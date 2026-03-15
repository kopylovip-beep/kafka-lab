# Лабораторная работа №1  
## Потоковая обработка данных в реальном времени с использованием Apache Kafka

---

## Цель работы

Изучить потоковую обработку данных с помощью Apache Kafka и реализовать полный цикл передачи данных: генерация события → Producer → Kafka → Consumer → валидация.

---

## Задачи

- Развернуть Apache Kafka;  
- Разработать Kafka Producer для генерации событий пункта приема вторсырья;  
- Разработать Kafka Consumer для получения и проверки сообщений;  
- Реализовать генерацию сообщений в формате JSON;  
- Проверить корректность передачи данных в реальном времени.

---

## Тема лабораторной работы

**Пункт приема вторсырья**

Producer генерирует события сдачи вторсырья:

- `deposit` — материал принят  
- `reject` — материал не принят  

Consumer принимает сообщения, валидирует их и выводит результат в консоль.

---

## Архитектура приложения

Generator → Producer → Apache Kafka → Consumer

### Компоненты

- **generator.py** — генерация сообщений (отделена от Producer согласно принципам SOLID);  
- **producer.py** — отправка сообщений в Kafka;  
- **consumer.py** — получение и проверка сообщений;  
- **Kafka Topic:** `recycling`.  

---

## Формат сообщения

Пример JSON-сообщения:

```json
{
  "user": "Anna",
  "material": "Plastic",
  "action": "deposit",
  "weight_kg": 2.35,
  "time": "2026-03-15 20:10:12"
}
```
## Поля
| Поле      | Описание                        |
| --------- | ------------------------------- |
| user      | имя человека, сдающего материал |
| material  | вид вторсырья                   |
| action    | действие (`deposit` / `reject`) |
| weight_kg | вес материала в килограммах     |
| time      | время события                   |

## Требования

- Python 3.9+
- Apache Kafka
- kafka-python

## Установка зависимостей
```
pip install kafka-python
```

## Запуск проекта
1. Запуск Zookeeper
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
2. Запуск Kafka
```
bin/kafka-server-start.sh config/server.properties
```
3. Создание топика
```
bin/kafka-topics.sh --create \
--topic recycling \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```
4. Запуск Consumer
```
python consumer.py
```
5. Запуск Producer
```
python producer.py
```
## Структура проекта
kafka_recycling/
│
├── generator.py
├── producer.py
├── consumer.py
└── README.md

##  Результат выполнения лабораторной работы

В ходе лабораторной работы реализована система потоковой обработки данных для пункта приема вторсырья с использованием Apache Kafka.  

##  Работа Producer

- Producer генерирует события сдачи вторсырья каждые несколько секунд.  
- Каждое сообщение содержит: пользователя, тип материала, действие (`deposit` или `reject`), вес в кг и время события.  
- Сообщение выводится в консоль Producer и отправляется в Kafka-топик `recycling`.

**Пример вывода Producer:**
```
Produced: {"user": "Anna", "material": "Plastic", "action": "deposit", "weight_kg": 2.35, "time": "2026-03-15 20:10:12"}
Produced: {"user": "Ivan", "material": "Glass", "action": "reject", "weight_kg": 5.00, "time": "2026-03-15 20:10:14"}
Produced: {"user": "Maria", "material": "Paper", "action": "deposit", "weight_kg": 3.75, "time": "2026-03-15 20:10:16"}
```

---

## Работа Consumer

- Consumer получает сообщения из Kafka-топика `recycling`.  
- Каждое сообщение проверяется на наличие всех полей и корректность значений.  
- Результат проверки выводится в консоль:

**Пример вывода Consumer (валидные сообщения):**
```
VALID: {'user': 'Anna', 'material': 'Plastic', 'action': 'deposit', 'weight_kg': 2.35, 'time': '2026-03-15 20:10:12'}
VALID: {'user': 'Ivan', 'material': 'Glass', 'action': 'reject', 'weight_kg': 5.0, 'time': '2026-03-15 20:10:14'}
VALID: {'user': 'Maria', 'material': 'Paper', 'action': 'deposit', 'weight_kg': 3.75, 'time': '2026-03-15 20:10:16'}
```

**Пример невалидного сообщения:**
```
NOT VALID: {"user":"Ivan","material":"Glass","action":"deposit"}
```

- Такое сообщение считается некорректным, так как отсутствует поле `weight_kg` или `time`.

---

## Итоговый результат

- Apache Kafka успешно развернута и работает.  
- Producer и Consumer корректно обмениваются сообщениями в реальном времени.  
- Сообщения валидируются: корректные выводятся как **VALID**, а некорректные как **NOT VALID**.  
- Реализована цепочка **Generator → Producer → Kafka → Consumer**, демонстрирующая полный цикл потоковой обработки данных.  
- Система позволяет отслеживать события приема вторсырья и фильтровать некорректные данные без потерь.

## Используемые технологии
- Apache Kafka — брокер сообщений
- Python — язык программирования
- kafka-python — клиент Kafka для Python
- JSON — формат обмена данными

  
## Дополнительные материалы
- https://kafka.apache.org
- https://habr.com/ru/companies/otus/articles/789896/
- https://stepik.org/course/258122
