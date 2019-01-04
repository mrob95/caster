#
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Lyx

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, Context, AppContext, Dictation, Key, Text, Repeat,
                       Function, Choice)

from caster.lib import control
from caster.lib import settings
from caster.lib.actions import Key, Text
from caster.lib.context import AppContext
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class LyxRule(MergeRule):
    pronunciation = "lyx"

    mapping = {

        "new file": R(Key("c-n")),
        "open file": R(Key("c-o")),
        "math mode": R(Key("c-m")),
        
      

        

        }
    extras = [
        # Choice("environment", {
        #     "(in line formula | in line)": "i",
            
        #     "(display formula | display)": "d",
        #     "(equation array environment | equation array)": "e",
        #     "(AMS align environment | AMS align)": "a",
        #     "AMS align at [environment]": "t",
        #     "AMS flalign [environment]": "f",
        #     "(AMS gathered environment | AMS gather)": "g",
        #     "(AMS multline [environment]| multiline)": "m",
        #     "array [environment]": "y",
        #     "(cases [environment] | piecewise)": "c",
        #     "(aligned [environment] | align)": "l",
        #     "aligned at [environment]": "v",
        #     "gathered [environment]": "h",
        #     "split [environment]": "s",
        #     "delimiters": "r",
        #     "matrix": "x",
        #     "macro": "o",
            
            
        # }),
        # Dictation("dictation"),
        # IntegerRefST("n", 1, 10),
        # IntegerRefST("m", 1, 10),
        # IntegerRefST("numbers", 1, 1000),

    ]
    # defaults = {"n": 1, "dict": "", "click_by_voice_options": "c"}


#---------------------------------------------------------------------------

context = AppContext(executable="lyx")
grammar = Grammar("lyx", context=context)

if settings.SETTINGS["apps"]["lyx"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(LyxRule())
    else:
        rule = LyxRule(name="lyx")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
