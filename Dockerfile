FROM python:3.9

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm
RUN python -m spacy download es_core_news_sm
RUN python -m spacy download de_core_news_sm
RUN python -m spacy download fr_core_news_sm
RUN python -m spacy download it_core_news_sm
RUN python -m spacy download nl_core_news_sm
RUN python -m spacy download pt_core_news_sm
RUN python -m spacy download xx_ent_wiki_sm

RUN python -c "import nltk; nltk.download('wordnet'); nltk.download('punkt')"
ENV PYTHONPATH=/usr/src/app

CMD ["python", "-m", "pytest", "tests"]
