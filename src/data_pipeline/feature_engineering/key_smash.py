from statistics import mean

class KeySmash:
    """A class for calculating metrics to indicate key smashing behavior in a text.
    
    Key smashing is the act of typing on a keyboard in a rapid and uncontrolled manner,
    often resulting in a series of random characters being entered into a document or text field.
    """
    
    
    def __init__(self):
        self.char_sets = {
            "vowels": 'aeiouáéíóúãõ',
            "consonants": 'bcdfghjklmnñpqrstvwxyz',
            "special_characters": '!@#$%^¨|\'\"&*()_+:;~`´]}{[}ºª=-.¿¡'
        }
    
    def calculate_char_frequency_metric(self, text):
        """
        Calculate the Char Frequency Metric.
        
        Parameters
        ----------
        text : str
            The text to use for the calculation.
            
        Returns
        -------
        float
            Char Frequency Metric.
            
        Examples
        --------
        >>> calculate_char_frequency_metric("PUENTECILLA KM. 1.7")
        1.121212121212121
        >>> calculate_char_frequency_metric("ASDASD XXXX")
        3.0
        """
        word_results = []

        for w in text.split(' '):
            char_count = []
            if w and len(w) > 0:
                for e in set(w):
                    char_count.append(w.count(e)**2)
                word_results.append(sum(char_count)/len(w))

        if word_results == 0 or len(word_results) == 0:
            return 0
        else:
            return mean(word_results)
    
    def calculate_irregular_sequence_metric(self, text, opt):
        """
        Calculate the Irregular Sequence Metric.
        
        Parameters
        ----------
        text : str
            The text to use for the calculation.
        opt : str
            The type of characters to consider for the calculation,
            can be one of 'vowels', 'consonants', or 'special_characters'.
            
        Returns
        -------
        float
            Irregular Sequence Metric.
            
        Examples
        --------
        >>> calculate_irregular_sequence_metric("PUENTECILLA KM. 1.7", "vowels")
        0.21052631578947367
        >>> calculate_irregular_sequence_metric("ASDASD XXXX", "consonants")
        2.1818181818181817
        >>> calculate_irregular_sequence_metric("!@#$% ASDFGHJKL", "special_characters")
        1.5625
        """
        count_sequence = 1
        sequence_regex = []

        text = str(text).lower()
        opt = self.char_sets[opt]

        for i in range(len(text) - 1):
            if text[i] in opt and text[i + 1] in opt:
                count_sequence = count_sequence + 1
            else:
                if (count_sequence != 1):
                    sequence_regex.append(count_sequence**2)
                    count_sequence = 1

        if (count_sequence != 1):
            sequence_regex.append(count_sequence**2)
            
        return sum(sequence_regex)/len(text)
    
    def calculate_number_count_metric(self, text):
        """
        Calculate the Number Count Metric.
        
        Parameters
        ----------
        text : str
            The text field to use for the calculation.
            
        Returns
        -------
        float
            Number Count Metric.
            
        Examples
        --------
        >>> calculate_number_count_metric("ABC 123 !@#")
        0.0 
        >>> calculate_number_count_metric("ABC123 !@#")
        0.9
        """
        text_list = text.split()
        calc_num_line = 0

        if text_list:
            for word in text_list:
                if any(char.isdigit() for char in word) and any(not char.isdigit() for char in word):
                    num = len([char for char in word if char.isdigit()])
                    calc_num = num**2
                    calc_num_line += calc_num

            return calc_num_line / len(' '.join(text_list))
        return 0