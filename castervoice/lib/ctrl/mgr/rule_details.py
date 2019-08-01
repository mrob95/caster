import inspect


class RuleDetails(object):
    """
    A per-rule instantiation configuration.
    """

    def __init__(self, name=None, executable=None, grammar_name=None,
                 enabled=True, ccrtype=None, rdp_mode_exclusion=False, transformer_exclusion=False):
        """
        :param name: Dragonfly rule name
        :param executable: Dragonfly AppContext executable
        :param grammar_name: Dragonfly grammar name
        :param enabled: settings.py toggle
        :param ccrtype: global, app, selfmod, or none
        :param rdp_mode_exclusion: exclude from rdp mode
        :param transformer_exclusion: exclude from transformations
        """
        self.name = name
        self.executable = executable
        self.grammar_name = grammar_name
        self.enabled = enabled
        self.declared_ccrtype = ccrtype
        self.rdp_mode_exclusion = rdp_mode_exclusion
        self.transformer_exclusion = transformer_exclusion

        # Python black magic to determine which file to track:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        self._filepath = module.__file__

    def get_filepath(self):
        return self._filepath
