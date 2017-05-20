import pickle

from revscoring import ScorerModel
from revscoring.features import wikitext


class FleschComplexityModel(ScorerModel):
    """
    Implementation of the Flesch reading ease model
    https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, features=[wikitext.revision.flesh_kincaid],**kwargs)

    def score(self, feature_values):
        """
        Make a prediction or otherwise use the model to generate a score.

        :Parameters:
            feature_values : collection(`mixed`)
                an ordered collection of values that correspond to the
                `Feature` s provided to the constructor

        :Returns:
            A `dict` of statistics
        """
        return feature_values[0]

    @classmethod
    def from_config(cls, config, name, section_key='scorer_models'):
        section = config[section_key][name]
        return cls(**{k: v for k, v in section.items() if k != "class"})

    def info(self):
        return {
            'type': "FleschScorer",
            'version': self.version,
            'behavior': "Returns the flesch readability score."
        }

    def format_info(self, format="str"):
        if format == 'str':
            return str(self.info())
        elif format == 'json':
            return self.info()
        else:
            raise TypeError("Format {0} not supported".format(format))
