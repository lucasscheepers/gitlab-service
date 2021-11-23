FROM python:3.8-alpine
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt
COPY . .
EXPOSE 8088
ENTRYPOINT [ "python", "main.py"]