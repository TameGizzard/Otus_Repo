# Для запуска контейнера используйте команду:
# docker run -d -p 8000:8000 имя_контейнера

FROM python:3.9-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
