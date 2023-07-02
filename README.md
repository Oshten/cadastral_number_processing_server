# cadastral_number_processing_server

Сервер для обработки кадастровых номеров. <br>
Принимает следующие запросы:
```
POST /processing
```
Тело запроса должно иметь вид `{"cadastral_number":"<cadastral_number>", "latitude":<latitude>, "longitude":<longitude>}`
<br>
```
GET /<id>
```


## Запуск сервера
Для запуска сервера в терминале корневой папки выполнить следующие команы:
```
docker build -t server .
```
```
docker run -p 8000:8000 -d server
```
Для остановки сервера выполнить:
```
docker stop <название контейнера>
```
Для повторного запуска контейнера
```
docker start <название контейнера>
```
