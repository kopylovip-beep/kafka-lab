# kafka-lab
## Описание проекта

Данный проект демонстрирует работу потоковой обработки данных в реальном времени с использованием Apache Kafka.

Приложение состоит из двух компонентов:

- **Producer** — генерирует сообщения в формате JSON и отправляет их в Kafka.
- **Consumer** — получает сообщения из Kafka, выполняет их проверку (валидацию) и выводит результат в консоль.

Сообщения содержат информацию о вылетающих рейсах аэропорта.

---

## Структура проекта

```
kafka_stream_lab
│
├── producer.py # отправка сообщений в Kafka
├── consumer.py # получение и проверка сообщений
├── generator.py # генерация данных
├── config.py # настройки Kafka
├── docker-compose.yml
├── requirements.txt
└── README.md
```
## Стек технологий

- **Apache Kafka 4.2.0** (KRaft mode, без ZooKeeper) — брокер сообщений
- **Python 3** — язык разработки скриптов
- **kafka-python** — клиентская библиотека для работы с Kafka из Python
---

## Формат сообщений

Producer генерирует JSON-сообщения следующего вида:

```json
{
  "flight_number": "LH123",
  "destination": "Paris",
  "departure_time": "14:32:18",
  "status": "boarding"
}
```
## Установка зависимостей

Перед запуском необходимо установить Python-библиотеки:
``` bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Kafka и Zookeeper запускаются с помощью Docker.
```
docker-compose up -d
Запуск Consumer
```
В одном терминале запустить:
```
python consumer.py
Запуск Producer
```
В другом терминале выполнить:
```
python producer.py
```

Архитектура системы
Producer → Kafka → Consumer

Producer отправляет сообщения в Kafka, после чего Consumer получает и обрабатывает их.
