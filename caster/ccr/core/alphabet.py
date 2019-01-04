from dragonfly import Choice
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control
from caster.lib.dfplus.merge.ccrmerger import CCRMerger
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
#
# def letter_choice(name):
#     return (Choice(name, {
#     "alpha": "s-a", "(air | ash)":"a",
#     "bravo": "s-b", "bat":"b",
#     "charlie": "s-c", "cap":"c",
#     "delta": "s-d", "die":"d",
#     "echo": "s-e", "each":"e",
#     "foxtrot": "s-f", "fail":"f",
#     "golf": "s-g", "gone":"g",
#     "hotel": "s-h", "harm":"h",
#     "india": "s-i", "sit":"i",
#     "juliet": "s-j", "jury":"j",
#     "kilo": "s-k", "crash":"k",
#     "lima": "s-l", "look":"l",
#     "mike": "s-m", "mad":"m",
#     "november": "s-n", "near":"n",
#     "oscar": "s-o", "odd":"o",
#     "papa": "s-p", "pit":"p",
#     "quebec": "s-q", "quest":"q",
#     "romeo": "s-r", "red":"r",
#     "sierra": "s-s", "sun":"s",
#     "tango": "s-t", "trap":"t",
#     "uniform": "s-u", "urge":"u",
#     "victor": "s-v", "vest":"v",
#     "whiskey": "s-w", "whale":"w",
#     "x-ray": "s-x", "box":"x",
#     "yankee": "s-y", "yes":"y",
#     "zulu": "s-z", "zip":"z",}))


def letter_choice(name):
    return (Choice(name, {
        "(anti | arch)":"a",
        "bat":"b",
        "cap":"c",
        "die":"d",
        "each":"e",
        "fail":"f",
        "(gone | gust)":"g",
        "(harp | harm)":"h",
        "sit":"i",
        "jury":"j",
        "crunch":"k",
        "look":"l",
        "(made | mad)":"m",
        "near":"n",
        "odd":"o",
        "pit":"p",
        "queer":"q",
        "red":"r",
        "sun":"s",
        "trap":"t",
        "urge":"u",
        "vest":"v",
        "whale":"w",
        "box":"x",
        "yes": "y",
        "zulu":"z",}))

class Alphabet(MergeRule):
    pronunciation = "alphabet"

    mapping = {
        "<letter>":
            R(Key("%(letter)s"),
              rdescript="Spell"),
        "big <letter>":
            R(Key("s-%(letter)s")),
    }
    extras = [
        letter_choice("letter"),
    ]
    defaults = {

    }


control.nexus().merger.add_global_rule(Alphabet())
