from ml4data.base import ML4DataClient
from enum import Enum

class Lang(Enum):
    ENGLISH = 'en'
    SPANISH = 'es'

class NLPClient(ML4DataClient):
    base_url = ML4DataClient.base_url + '/text'

    def guess_gender(self, name):
        """ Guess the gender of any given name

        Parameters:
            name (str): Name to guess gender
        """
        return self._post('/gender-guesser',
                          params={'name': name})

    def analyze_sentiment(self, text):
        """ Analyze sentiment of a given text

        Parameters:
            text (str): Text to analyze sentiment
        """
        return self._get('/sentiment',
                         params={'text': text})

    def detect_language(self, text):
        """ Detect the language of a given text

        Parameters:
            text (str): Text to detect language
        """
        return self._get('/language',
                         params={'text': text})

    def extract_entities(self, text, lang='en'):
        """ Analyze sentiment of a given text

        Parameters:
            text (str): Text to extract sentiment
            lang (str or `nlp.Lang`): Language of given text
        """
        return self._get('/ner',
                         params={'text': text,
                                 'lang': Lang(lang)})

    def classify_product(self, text):
        """ Classify product given a text description

        Parameters:
            text (str): Text to classify
        """
        return self._get('/products',
                         params={'text': text})

    def classify_supermarket_product(self, text):
        """ Classify product given a text description

        Parameters:
            text (str): Text to classify
        """
        return self._get('/products/supermarket',
                         params={'text': text})

    def analyze_company(self, name):
        """ Analyze a company by the name

        Parameters:
            text (str): Company name
        """
        return self._get('/company-guesser',
                         params={'name': name})
