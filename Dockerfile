FROM python

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirement.txt .
RUN pip install -r requirement.txt

COPY . /usr/src/app/

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


