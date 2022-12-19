# создаем окружение
FROM python:3.9
# создаем рабочсую директорию в докере
WORKDIR .
#копируем всю текущую директорию в докер в созданную папку
COPY . .
#копируем файл requirements
COPY requirements.txt /src/requirements.txt
# запускаем команду внутри докера для загрузки из requirements
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt
# обозначаем порт
EXPOSE 6060
# запускаем файл manage.py

#CMD ["python", "stocks_products/manage.py runserver 0.0.0.0:6060"]
#CMD ["python", "/src/manage.py runserver 0.0.0.0:6060"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:6060"]