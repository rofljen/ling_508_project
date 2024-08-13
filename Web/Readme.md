# Linguistic Classifier #

## Introduction ##

The Linguistic Classifier is a tool to provide linguistic information for a text input by a user. The user enters a chunk of text, it is parsed into sentences, and then parsed into individual words, for which linguistic information is generated, including parts of speech, lemmas, glosses and example usages for the glosses. 
Both the text and its metadata, including text name, source, genre, word count and language, as well as the word form, and its linguistic information are saved to a database.

The Linguistic Classifier uses:
- Python
  - Spacy and NLTK packages for linguistic data
- MySQL
- Docker
- Flask API
- HTML

This program is intended to be scalable; the intent is to add more language models as well as funcitonality that provides more linguistic information.
There were some issues using

## Installation ##

1. Clone the Repository
```bash
git clone https://github.com/rofljen/ling_508_project
```
2. Navigate to the project directory
```bash
cd <project directory>
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

## Congfiguration ##

1. Ensure MySQL is set up according to the 'docker-compose.yml' file


2. If applicable, set up environment variables for the database connection

## Usage ##
## Testing ##

## Known Issues ##

Some issues encountered during development:
Issues with MySQL connection during testing, issues with language recognition.

## Future Work ##

The program is intended to be scalable, with plans to:

Add more language models
Enhance functionality to provide additional linguistic information

## Contributing ## 

## License ##

## Contact ##

For questions or feedback, please contact jennifer.haliewicz@gmail.com