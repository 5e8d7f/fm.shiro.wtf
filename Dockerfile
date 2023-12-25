FROM alpine:edge

WORKDIR /app
COPY . .

RUN apk add --no-cache python3 py3-pip
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 8080
CMD ["python", "-O", "app.py"]