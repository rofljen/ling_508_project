# Use a lightweight base image with Python
FROM python:3.9

# Set working directory
WORKDIR /python-docker

# Set environment variables
ENV FLASK_APP=test_app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
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

# Copy the rest of the application code into the container
COPY . /python-docker

EXPOSE 8000

# Command to run the application
CMD ["flask", "run"]
