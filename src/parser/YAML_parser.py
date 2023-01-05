import yaml

from src.parser.parser_base import ParserBase

class YAMLParser(ParserBase):

    def parse(self):
        return self._parse_yaml()

    def _parse_yaml(self):
        with open(self.filepath, 'r') as file:
            dag_config_dict = yaml.safe_load(file)

        dag = self._try_get(dag_config_dict, 'dag')

        initial_parser = {
            "dag_id": self._try_get(dag, 'id'),
            "data_path": self._try_get(dag, 'data_path'),
            "output_folder": self._try_get(dag, 'output_folder'),
            "description": self._try_get(dag, 'description'),
            "feature_engineering": self._try_get(dag, 'feature_engineering'),
            "model": self._try_get(dag, 'model'),
        }

        return initial_parser
