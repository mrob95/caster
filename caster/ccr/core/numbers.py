from dragonfly import Function, Choice
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control, alphanumeric, settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.ccrmerger import CCRMerger
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class Numbers(MergeRule):
    pronunciation = "numbers"
    mapping = {
        "word number <wn>":
            R(Function(alphanumeric.word_number, extra="wn"), rdescript="Number As Word"),
        "numb <wnKK> [<wnKK2>] [<wnKK3>] [<wnKK4>] [<wnKK5>]":
            R(Text("%(wnKK)s" + "%(wnKK2)s" + "%(wnKK3)s" + "%(wnKK4)s" + "%(wnKK5)s"),
              rspec="number",
              rdescript="Number"),
        # "<numberalias>":
        #     R(Key("%(numberalias)s")),

    }

    extras = [
        IntegerRefST("wn", 0, 10),
        IntegerRefST("wnKK", 0, 10),
        IntegerRefST("wnKK2", 0, 10),
        IntegerRefST("wnKK3", 0, 10),
        IntegerRefST("wnKK4", 0, 10),
        IntegerRefST("wnKK5", 0, 10),

        Choice("numberalias", {
            "zero":"0",
            "ein":"1",
            "twit":"2",
            "tray":"3",
            "fear":"4",
            "firth":"5",
            "sex":"6",
            "seventh":"7",
            "eigen":"8",
            "net":"9",
        }),
    ]
    defaults = {
        "wnKK2": "",
        "wnKK3": "",
        "wnKK4": "",
        "wnKK5": "",
    }

if settings.SETTINGS["core"]["numbers"]:
    control.nexus().merger.add_global_rule(Numbers())
