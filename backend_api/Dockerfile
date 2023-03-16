FROM python:3.9
# Folder for fastAPI 

# installing requierments
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /code

# starting the app
COPY ./app /code/app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "5000"]