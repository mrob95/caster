from dragonfly import (AppContext, Grammar, Key, MappingRule,
                       Pause, Text, Choice, Function)

from caster.lib import control, settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class photoshopRule(MergeRule):
    pronunciation = "Photo shop"

    mapping = {
        "new (file | pane)": R(Key("c-n"), rdescript="Photoshop: New File"),

        "open file":    R(Key("c-o"), rdescript="Photoshop: Open File"),
        "close file":    R(Key("c-w"), rdescript="Photoshop: Open File"),

        "transform":    R(Key("c-t"), rdescript="Photoshop: Open File"),

        "new layer": R(Key("cs-n"), rdescript="Photoshop: New File"),
    

        "open folder":  R(Key("cs-o"), rdescript="Photoshop: Open Folder"),
        "save as":  R(Key("cs-s"), rdescript="Photoshop: Save As"),
        }

    extras = []
    defaults = {}


context = AppContext(executable="photoshop", title="photoshop")
grammar = Grammar("photoshop", context=context)
if settings.SETTINGS["apps"]["photoshop"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(photoshopRule())
    else:
        rule = photoshopRule()
        gfilter.run_on(rule)
        grammar.add_rule(photoshopRule(name="photoshop"))
        grammar.load()
