FROM python:3.8
ENV PYTHONBUFFERED 1
RUN mkdir /server
WORKDIR /server
RUN pip install --upgrade pip
RUN pip install flask requests
COPY . /server
EXPOSE 5000
CMD ["flask","run","--host","0.0.0.0"]
