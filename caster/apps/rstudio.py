'''
Mike Roberts 13/09/18
'''

from dragonfly import (Dictation, Grammar, IntegerRef, MappingRule,
                       Pause, Repeat)
from dragonfly.actions.action_mimic import Mimic
from caster.lib.actions import Key, Text
from caster.lib.context import AppContext

from caster.lib import control, settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

class RStudioRule(MergeRule):
    pronunciation = "are studio"

    mapping = {
    "new file":
        R(Key("cs-n"), rdescript="RStudio: New File"),
    "open file":
        R(Key("c-o"), rdescript="RStudio: Open File"),
    "save all":
        R(Key("ac-s"), rdescript="RStudio: Save All"),
    "select all":
        R(Key("c-a"), rdescript="RStudio: Select All"),
    "find":
        R(Key("c-f"), rdescript="RStudio: Find"),

    "[go to] line <n>":
        R(Key("as-g") + Pause("10") + Text("%(n)s") + Key("enter"),
          rdescript="RStudio: Go to Line #"),
    "focus console":
        R(Key("c-2"), rdescript="RStudio: Focus Console"),
    "focus main":
        R(Key("c-1"), rdescript="RStudio: Focus Main"),

    "next pane":
        R(Key("c-f12"), rdescript="RStudio: Next pane"),
    "first pane":
        R(Key("cs-f11"), rdescript="RStudio: First pane"),
    "previous pane":
        R(Key("c-f11"), rdescript="RStudio: Previous pane"),
    "last pane":
        R(Key("cs-f12"), rdescript="RStudio: Last pane"),
    "close pane":
        R(Key("c-w"), rdescript="RStudio: Close pane"),


    "run (line | that)":
        R(Key("c-enter"), rdescript="RStudio: Run Line"),
    "run document":
        R(Key("ac-r"), rdescript="RStudio: Run Document"),
    "comment (line | selected)":
        R(Key("cs-c"), rdescript="RStudio: Comment Line"),
    "knit (document | file)":
        R(Key("cs-k")),

    "next plot":
        R(Key("ac-f12"), rdescript="RStudio: Next Plot"),
    "previous plot":
        R(Key("ac-f11"), rdescript="RStudio: Previous Plot"),

    "help":
        R(Key("c-c, c-2, question, c-v, enter, c-1")),
    }
    extras = [
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {}

context = AppContext(executable="rstudio")
grammar = Grammar("RStudio", context=context)
if settings.SETTINGS["apps"]["rstudio"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(RStudioRule())
    else:
        rule = RStudioRule()
        gfilter.run_on(rule)
        grammar.add_rule(RStudioRule(name="rstudio"))
        grammar.load()
