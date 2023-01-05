from whatlies.language import BytePairLanguage
import numpy as np

class WordEmbedding:
    def __init__(self, lang, dimensions):
        """Initialize a word embedding object using the BytePairLanguage model.

        Parameters
        ----------
        lang: str
            The language to use for the word embedding (default is "es")
        dimensions: str
            The number of dimensions for the word embedding vectors (default is 25)
        """
        self.bpl = BytePairLanguage(lang=lang, dim=dimensions) 
        
    def get_embedding(self, text):
        """Get the word embedding vector for a given text.

        Parameters
        ----------
        text: str
            The string to be processed

        Returns
        ----------
        arr[float]
            A word embedding vector for the given text
        
        Examples
        --------
        >>> get_embedding("This is a text", "es", 25)
        [ 0.06799883  0.17547965  0.47599664  0.16108984 -0.1360625  -0.10632467
        -0.10654568 -0.09805    -0.33004168 -0.33528003 -0.23304085  0.36661038
        -0.5797167   0.53252834  0.30276018 -0.01584417  0.85087484  0.14121284
        0.74862367 -0.33011952  0.015432    0.02694534  0.10118082 -0.34017918
        -0.14560167]
        """
        return self.bpl[text].vector