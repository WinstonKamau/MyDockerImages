FROM python:2.7

RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /usr/local/bin/cloud_sql_proxy

RUN chmod +x /usr/local/bin/cloud_sql_proxy

COPY cloud_sql_proxy/database.sh /usr/local/bin/

EXPOSE 3300

CMD ["bash", "database.sh"]