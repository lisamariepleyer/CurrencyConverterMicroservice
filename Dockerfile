FROM python:3.11
RUN apt update -y
RUN apt-get install python3 python3-pip -y
RUN pip install grpcio
RUN pip install grpcio-tools
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install lxml
COPY . .
RUN chmod +x /CurrencyConverterService.py
EXPOSE 8501
ENTRYPOINT [ "python3", "CurrencyConverterService.py" ]