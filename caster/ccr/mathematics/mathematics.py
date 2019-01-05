'''
Created on Sep 4, 2018

@author: Mike Roberts
'''
from dragonfly import Function, Choice, Key, Text, Mouse

from caster.lib import control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

def texchar(symbol):
    keychain = "ctrl:down, "
    for character in symbol:
        keychain = keychain + character + ", "
    keychain=keychain + "ctrl:up"
    Key(keychain).execute()

def greek(greek):
    keychain = "c-g, " + greek
    Key(keychain).execute()

def matrix(rows, cols):
    Mouse("[100, 150], left/100").execute()
    Key(str(rows) + "/50, tab, " + str(cols) + "/50, enter").execute()

class mathematics(MergeRule):
    pronunciation = "mathematics"

    mapping = {
        "<wnKK>":R(Text("%(wnKK)s")),

        "<symbol>":
            R(Function(texchar, extra={"symbol"})),
        #
        "greek <greek>":
            R(Function(greek, extra={"greek"})),

        "accent <accent>":
            R(Key("c-%(accent)s")),
        #
        "matrix <rows> by <cols>":
            R(Function(matrix)),

        "is less equal": R(Key("ctrl:down, l, e, q,  ctrl:up")),
        "is less than": R(Text("<")),
        "is greater equal": R(Key("ctrl:down, g, e, q,  ctrl:up")),
        "is greater than": R(Text(">")),
        "is not equal": R(Key("ctrl:down, n, e, q,  ctrl:up")),
        "limit": R(Key("l, l, i, m, left, down")),
        "probability": R(Key("P, c-0")),
        "absolute": R(Text("||") + Key("left")),
        "inverse": R(Key("c-h, minus, 1, right")),

        "toggle math":R(Key("c-m")),
        "toggle text":R(Key("c-t")),
        "fraction":R(Key("c-f")),
        "(radical | root)":R(Key("c-r")),
        "super [script]":R(Key("c-h")),
        "sub [script]":R(Key("c-l")),
        "integral":R(Key("c-i")),
        "summation":R(Key("c-7")),
        "squared":R(Key("c-h, 2, right")),
        "prime":R(Key("apostrophe")),

        "parens":R(Key("c-0")),
        "squares":R(Key("c-6")),

        "beta":R(Key("c-g, b")),
        "epsilon":R(Key("c-g, e")),
        "sigma":R(Key("c-g, s")),



    }

    extras = [
        IntegerRefST("rows", 1, 6),
        IntegerRefST("cols", 1, 6),
        IntegerRefST("wnKK", 1, 10),
        Choice("greek", {
            "alpha":"a", "beater":"b", "gamma":"g", "delta":"d", "epsilon":"e",
            "zita":"z", "eater":"h", "theta":"y", "iota":"i", "kappa":"k",
            "lambda":"l", "mu":"m",
            #"new":"n",
            "zee":"x", "pie":"p", "row":"r",
            "sigma":"s", "tau":"t", "upsilon":"u", "phi":"f", "chi":"q",
            "sigh":"c", "omega":"w",

            "big gamma":"G",
            "big delta":"D",
            "big lambda":"L",
            "big sigma":"S",
            "big phi":"F",
            "big omega":"W",
            }),

        Choice("symbol", {
            "times":"times", "divide":"div", "intersection":"cap", "union":"cup",
            "stop":"cdot", "approximate":"approx", "proportional":"propto", "not equal":"neq",
            "member":"in", "for all":"forall", "partial":"partial", "infinity":"infty",
            "dots":"dots",
            #
            "left arrow":"leftarrow", "right arrow":"rightarrow", "up arrow":"uparrow",
            "down arrow":"downarrow",
        }),
        Choice("accent", {
            "hat":"caret",
            "tilde":"tilde",
            "dot":"dot",
            "double dot":"dquote",
            "bar":"underscore",
        }),


    ]

control.nexus().merger.add_global_rule(mathematics())
