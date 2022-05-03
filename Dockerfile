FROM python:3.8
ENV PYTHONBUFFERED 1
RUN mkdir /request
WORKDIR /request
RUN pip install --upgrade pip
RUN pip install flask requests 
COPY . /request
EXPOSE 5000
CMD ["python","req.py"]

