FROM httpd:latest

COPY ./site /usr/local/apache2/htdocs/
COPY ./data /usr/local/apache2/htdocs/data
