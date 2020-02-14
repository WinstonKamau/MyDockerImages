FROM python:3.7.6

RUN pip install flask
RUN pip install gunicorn

WORKDIR python_app

COPY src /python_app/src

CMD ["gunicorn", "-b", "0.0.0.0:8770", "--access-logfile", "-", "src.wsgi:app" ]
