FROM python:3.9
# Folder for fastAPI 

WORKDIR /code

# installing requierments
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# starting the app
COPY ./app /code/app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "5000"]