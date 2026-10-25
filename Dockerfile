FROM python:3.14.5-slim

WORKDIR /backend

RUN useradd -m myuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER myuser

EXPOSE 5000

CMD ["python", "app.py"]