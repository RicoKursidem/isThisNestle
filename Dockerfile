FROM python:3.9

# Folder for fastAPI 
WORKDIR /code

# installing requierments
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt --proxy http://10.255.0.10:8080 

# starting the app
COPY ./app /code/app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "5000"]