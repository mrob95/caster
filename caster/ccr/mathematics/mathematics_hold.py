'''
Created on Sep 4, 2018

@author: Mike Roberts
'''
from dragonfly import Function, Choice, Key, Text

from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
#
# def texchar(symbol):
#     keychain = "ctrl:down, "
#     for character in symbol:
#         keychain = keychain + character + ", "
#     keychain=keychain + "ctrl:up"
#     Key(keychain).execute()

def texchar(symbol):
    keychain = "c-g, " + symbol
    Key(keychain).execute()

class mathematics(MergeRule):
    pronunciation = "mathematics"

    mapping = {
        "symbol <symbol>":
            R(Function(texchar, extra={"symbol"})),
        #
        "accent <accent>":
            R(Key("c-%(accent)s")),
        #
        "toggle math":
            R(Key("c-m")),
        "toggle text":
            R(Key("c-t")),
        "fraction":
            R(Key("c-f")),
        "radical":
            R(Key("c-r")),
        "super":
            R(Key("c-h")),
        "sub":
            R(Key("c-l")),
        "integral":
            R(Key("c-i")),
        "summation":
            R(Key("c-7")),
        "squared":
            R(Key("c-h, 2, right")),
        "prime":
            R(Key("apostrophe")),

        "parens":
            R(Key("c-0")),
        "squares":
            R(Key("c-6")),

        "beta":
            R(Key("ctrl:down, b, e, t, a, ctrl:up")),
        "epsilon":
            R(Key("ctrl:down, e, p, s, i, l, o, n, ctrl:up")),
        "sigma":
            R(Key("ctrl:down, s, i, g, m, a, ctrl:up")),


    }

    extras = [
        Choice("symbol", {
            "alpha":"a", "beater":"beta", "gamma":"gamma", "delta":"delta", "epsilon":"varepsilon",
            "zita":"zeta", "eater":"eta", "theta":"theta", "iota":"iota", "kappa":"kappa",
            "lambda":"lambda", "mu":"mu", "new":"nu", "zee":"xi", "pie":"pi", "row":"rho",
            "sigma":"sigma", "tau":"tau", "upsilon":"upsilon", "phi":"phi", "chi":"chi",
            "sigh":"psi", "omega":"omega",
            #
            "times":"times", "divide":"div", "intersection":"cap", "union":"cup",
            "stop":"cdot", "approximate":"approx", "proportional":"propto", "not equal":"neq",
            "member":"in", "for all":"forall", "partial":"partial", "infinity":"infty",
            "dots":"dots",
            #
            "left arrow":"leftarrow", "right arrow":"rightarrow", "up arrow":"uparrow",
            "down arrow":"downarrow",
            #

        }),
        Choice("accent", {
            "hat":"caret",
            "tilde":"tilde",
            "dot":"dot",
            "double dot":"dquote",
            "bar":"underscore",
        })


    ]

control.nexus().merger.add_global_rule(mathematics())
