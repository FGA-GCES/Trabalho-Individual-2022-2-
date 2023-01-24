from parser.parser_base import ParserBase

class FeatureEngineeringParser(ParserBase):

    def parse(self, data: list):
        return self._parse_feature_engineering_configs(data)
        
    def _parse_feature_engineering_configs(self, data: list):
        if(not data): return
        
        configs = []
        columns_set_alias = []
        for inputs in data:
            input = self._try_get(inputs, 'input')
            
            # columns
            columns_set, columns_alias = self._get_dataframe(self._try_get(input, 'columns'))
            columns_set_alias = columns_alias + columns_set_alias
            
            # features
            word_embedding, keyboard_smash = self._get_features_details(self._try_get(input, 'features'))
            data_lang, dimensions = self._get_word_embedding_config(word_embedding, columns_set_alias)
            
            # Enabled features
            enabled_features = keyboard_smash
            if(not dimensions): enabled_features['word_embedding'] = False
            else: enabled_features['word_embedding'] = True
            
            configs.append({ 
                'columns_alias': columns_alias, 
                'columns_set': columns_set, 
                'data_lang': data_lang, 
                'dimensions': dimensions, 
                'enabled_features': enabled_features
            })
            
        return configs, columns_set_alias
            
    def _get_dataframe(self, columns: dict):
        if(not columns): return 
        
        columns_alias = []
        
        for column in columns:
            for key in column.keys():
                columns_alias.append(key)
                
        return columns, columns_alias

    def _get_features_details(self, features: dict):
        if(not features): return
        
        word_embedding = self._try_get(features, 'word_embedding')
        if (word_embedding == 'off'): word_embedding = False
        
        keyboard_smash = self._get_keyboard_smash_config(features)
        
        return word_embedding, keyboard_smash
    
    def _get_word_embedding_config(self, feature: dict, columns_alias: list):
        if(not feature): return 'es', None
        
        data_lang = self._get(feature, 'data_lang', 'es')
        if ('data_lang' in feature): del feature['data_lang']
        
        dimensions = {}
        dimensions_default_value = 25
        for key, item in feature.items():
            if(not(key in columns_alias)): 
                error_msg = f'Label {key} not match'
                raise ValueError(error_msg)
            
            dimensions[key] = self._get(item, 'dimensions', dimensions_default_value)
            
        for name in columns_alias:
            if(not(name in dimensions)): dimensions[name] = dimensions_default_value
        
        return data_lang, dimensions

    def _get_keyboard_smash_config(self, features: dict):
        keyboard_smash_default_value = {
            'ksmash_sequence_vowels': True,
            'ksmash_sequence_consonants': True,
            'ksmash_sequence_special_characters': True,
            'ksmash_numbers': True,
            'ksmash_char_frequence': True
        }
        
        keyboard_smash = self._get(features, 'keyboard_smash', keyboard_smash_default_value)
        if (keyboard_smash == keyboard_smash_default_value): return keyboard_smash
        
        for key in keyboard_smash.keys():
            if(key in keyboard_smash_default_value and keyboard_smash[key] == 'off'):
                keyboard_smash_default_value[key] = False
        
        return keyboard_smash_default_value        
