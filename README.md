# Add_fingerprint_remote_host

SSH Automation Script
Описание
Этот скрипт на Python автоматизирует процесс копирования SSH-ключей на удаленные сервера с использованием sshpass и ssh-copy-id. Скрипт принимает список IP-адресов, имя пользователя и пароль, затем выполняет команду ssh-copy-id для каждого IP-адреса.

Требования
Python 3.6 или выше
ОС: Ubuntu, macOS
Установка зависимостей
Скрипт автоматически проверяет наличие утилиты sshpass и устанавливает её при необходимости.

Использование
Чтобы использовать скрипт, клонируйте этот репозиторий и запустите скрипт с помощью Python:

```bash
python script.py -i [Список IP-адресов] -p [Пароль] -u [Имя пользователя]
```
Пример
```bash
python script.py -i 192.168.1.1 192.168.1.2 -p your_password -u your_username
```
В этом примере your_password — это пароль для SSH, your_username — это имя пользователя для SSH, а 192.168.1.1 и 192.168.1.2 — это IP-адреса серверов, на которые нужно скопировать SSH-ключи.

Вывод
Скрипт выводит статус выполнения каждой операции и сообщает о любых ошибках, если они возникнут.