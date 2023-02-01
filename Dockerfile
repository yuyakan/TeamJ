FROM httpd:latest

RUN apt-get update && apt-get install -y \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install --no-cache-dir pandas

COPY ./src /usr/local/apache2/htdocs/src
COPY ./site /usr/local/apache2/htdocs/site
COPY ./data /usr/local/apache2/htdocs/data

RUN ln -s /usr/local/apache2/htdocs/data /usr/local/apache2/htdocs/site/data

RUN echo DocumentRoot "/usr/local/apache2/htdocs/site" >> /usr/local/apache2/conf/httpd.conf
