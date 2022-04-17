#FROM prabhu12yuva/fsm-appx:python-3.10.4
FROM python:3.10.4-slim
 
WORKDIR /app
COPY . /app
 
RUN python -m pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["FlaskPgSharedDB.py"]