'''
Created Jan 2019

@author: Alex Boche, Mike Roberts
'''
from dragonfly import Function, Choice, Mouse, IntegerRef

from caster.lib.actions import Key, Text
from caster.lib import control, utilities
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.mergerule import MergeRule

BINDINGS = utilities.load_toml_file(utilities.get_full_path("caster/ccr/mathematics/lyx.toml"))


def greek(big, greek_letter):
    if big:
        greek_letter = greek_letter.title()
    Text("\\" + greek_letter + " ").execute()

def matrix(rows, cols):
    Text("\\bmatrix ").execute()
    for _ in range(0, rows-1):
        Key("a-m, w, i").execute()
    for _ in range(0, cols-1):
        Key("a-m, c, i").execute()

# Alternate between executing as text and executing as keys
def misc(misc_lyx_commands):
    if type(misc_lyx_commands) in [str, int]:
        Text(misc_lyx_commands).execute()
    elif type(misc_lyx_commands) in [list, tuple]:
        for i in range(len(misc_lyx_commands)):
            if i%2==0:
                Text(misc_lyx_commands[i]).execute()
            else:
                Key(misc_lyx_commands[i]).execute()

class lyx_mathematics(MergeRule):
    pronunciation = "licks maths"

    mapping = {
        BINDINGS["symbol1_prefix"] + " <symbol1>":
            Text("\\%(symbol1)s "),
        BINDINGS["symbol2_prefix"] + " <symbol2>":
            Text("\\%(symbol2)s "),
        BINDINGS["text_prefix"] + " <text_modes>":
            Text("\\%(text_modes)s "),

        BINDINGS["greek_prefix"] + " [<big>] <greek_letter>":
            Function(greek),

        BINDINGS["number_prefix"] + " <numbers>":
            Text("%(numbers)s"),

        "<misc_lyx_keys>":
            Key("%(misc_lyx_keys)s"),
            
        "<misc_lyx_commands>":
            Function(misc),

        "matrix <rows> by <cols>":
            Function(matrix),

        "<numbers> <denominator>":
            Key("a-m, f, %(n1)s, down, %(denominator)s, right"),
    }

    extras = [
        IntegerRefST("rows", 1, 10),
        IntegerRefST("cols", 1, 10),
        IntegerRefST("numbers", 1, 500),
        Choice("big", {BINDINGS["capitals_prefix"]: True}),
        Choice("greek_letter", BINDINGS["greek_letters"]),
        Choice("symbol1", BINDINGS["tex_symbols1"]),
        Choice("symbol2", BINDINGS["tex_symbols2"]),
        Choice("text_modes", BINDINGS["text_modes"]),
        Choice("misc_lyx_keys", BINDINGS["misc_lyx_keys"]),
        Choice("misc_lyx_commands", BINDINGS["misc_lyx_commands"]),
        Choice("denominator", BINDINGS["denominators"]),        
    ]

    defaults = {
        BINDINGS["capitals_prefix"]: False,
    }

control.nexus().merger.add_global_rule(lyx_mathematics())
