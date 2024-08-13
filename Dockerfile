# Start with a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the content of the current directory to /usr/src/app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download SpaCy language models
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download es_core_news_sm
RUN python -m spacy download de_core_news_sm
RUN python -m spacy download fr_core_news_sm
RUN python -m spacy download it_core_news_sm
RUN python -m spacy download nl_core_news_sm
RUN python -m spacy download pt_core_news_sm
RUN python -m spacy download xx_ent_wiki_sm

# Download NLTK corpora
RUN python -c "import nltk; nltk.download('wordnet'); nltk.download('punkt')"

# Set the Python path environment variable
ENV PYTHONPATH=/usr/src/app

# Run the application or tests
CMD ["flask", "run", "--host=0.0.0.0"]
