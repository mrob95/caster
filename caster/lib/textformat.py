import time
import sys

from caster.lib.actions import Key, Text
from caster.lib.clipboard import Clipboard
from caster.lib import settings, context
from caster.lib import settings


class TextFormat():
    '''
    Represents text formatting (capitalization and spacing) rules

    Commands for capitalization:
    1 yell - ALLCAPS
    2 tie - TitleCase
    3 Gerrish - camelCase
    4 sing - Sentencecase
    5 laws (default) - alllower
    Commands for word spacing:
    0 (default except Gerrish) - words with spaces
    1 gum (default for Gerrish)  - wordstogether
    2 spine - words-with-hyphens
    3 snake - words_with_underscores
    4 pebble - words.with.fullstops
    5 incline - words/with/slashes
    '''

    @classmethod
    def formatted_text(cls, capitalization, spacing, t):
        if capitalization == 0:
            capitalization = 5
        if spacing == 0 and capitalization == 3:
            spacing = 1

        if capitalization == 6:
            t = "".join(t.split(" "))
            punc = "@1/4#9?5%,."
            j = 0
            result = []
            t = t.lower()
            for i in range(len(t)):
                if i%2==0:
                    result.append(punc[j%len(punc)])
                    j += 1
                if i%3==0:
                    result.append(t[i].upper())
                else:
                    result.append(t[i])
            t = "".join(result)
        elif capitalization != 0:
            if capitalization == 1:
                t = t.upper()
            elif capitalization == 2:
                t = t.title()
            elif capitalization == 3:
                if tlen > 1:
                    t = t.title()
                    t = t[0].lower() + t[1:]
                else:
                    t = t[0].lower()
            elif capitalization == 4:
                t = t.capitalize()
            elif capitalization == 5:
                t = t.lower()
        if spacing != 0:
            if spacing == 1:
                t = "".join(t.split(" "))
            elif spacing == 2:
                t = "-".join(t.split(" "))
            elif spacing == 3:
                t = "_".join(t.split(" "))
            elif spacing == 4:
                t = ".".join(t.split(" "))
            elif spacing == 5:
                t = "/".join(t.split(" "))
            elif spacing == 6:
                t = "\\".join(t.split(" "))
        return t

    @classmethod
    def get_text_format_description(cls, capitalization, spacing):
        caps = {0: "<none>", 1: "yell", 2: "tie", 3: "gerrish", 4: "sing", 5: "laws"}
        spaces = {0: "<none>", 1: "gum", 2: "spine", 3: "snake",
                  4: "pebble", 5: "incline", 6: "descent"}
        if capitalization == 0 and spacing == 0:
            return "<none>"
        else:
            text = cls.formatted_text(capitalization, spacing, str("this is a test"))
            return "%s %s (%s)" % (caps[capitalization], spaces[spacing], text)

    def __init__(self, default_cap, default_spacing):
        self.default_cap = default_cap
        self.default_spacing = default_spacing
        self.capitalization = 0
        self.spacing = 0

    def _normalize_text_format(self):
        if self.capitalization == 0:
            self.capitalization = 5
        if self.spacing == 0 and self.capitalization == 3:
            self.spacing = 1

    def set_text_format(self, capitalization, spacing):
        self.capitalization = capitalization
        self.spacing = spacing
        self._normalize_text_format()

    def clear_text_format(self):
        self.capitalization = self.default_cap
        self.spacing = self.default_spacing

    def __str__(self):
        return self.get_text_format_description(self.capitalization, self.spacing)

    def get_formatted_text(self, t):
        return TextFormat.formatted_text(self.capitalization, self.spacing, t)


format = TextFormat(*settings.SETTINGS["formats"]["_default"]["text_format"])
secondary_format = TextFormat(*settings.SETTINGS["formats"]["_default"]["secondary_format"])

def _choose_format(big):
    return format if not big else secondary_format

# module interface
def set_text_format(big, capitalization, spacing):
    _choose_format(big).set_text_format(capitalization, spacing)

def clear_text_format(big):
    _choose_format(big).clear_text_format()

def peek_text_format(big):
    print("Text formatting: %s" % str(_choose_format(big)))

def partial_format_text(big, word_limit, textnv):
    Text(_choose_format(big).get_formatted_text(" ".join(str(textnv).split(" ")[0:word_limit]))).execute()

def prior_text_format(big, textnv):
    Text(_choose_format(big).get_formatted_text(str(textnv))).execute()

def master_format_text(capitalization, spacing, textnv):
    Text(TextFormat.formatted_text(capitalization, spacing, str(textnv))).execute()
