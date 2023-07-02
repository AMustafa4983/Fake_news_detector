 FROM python:3.9.7

 COPY requirements.txt .

 RUN pip install -r requirements.txt

 RUN python -c "import nltk; nltk.download('stopwords')"

 COPY . .

 EXPOSE 5000

 ENV FLASK_APP=api.py

 CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
