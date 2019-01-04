from dragonfly import (AppContext, Grammar, Key, MappingRule,
                       Pause, Text, Choice, Function)

from caster.lib import control, settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class TeXworksRule(MergeRule):
    pronunciation = "tex works"

    mapping = {
        "new file":
            R(Key("c-n")),
        "build it":
            R(Key("c-t")),
        "comment that":
            R(Key("cs-rbracket")),
        "uncomment that":
            R(Key("cs-lbracket")),
    }

    extras = [
    ]
    defaults = {

    }


context = AppContext(executable="TeXworks", title="TeXworks")
grammar = Grammar("TeXworks", context=context)
if settings.SETTINGS["apps"]["TeXworks"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(TeXworksRule())
    else:
        rule = TeXworksRule()
        gfilter.run_on(rule)
        grammar.add_rule(TeXworksRule(name="TeXworks"))
        grammar.load()
