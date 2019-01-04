'''
Created on Sep 4, 2018

@author: Mike Roberts
'''
from dragonfly import Function, Choice, Repeat
from caster.lib.actions import Key, Text

from caster.lib import control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

def greek(big, greek):
    if big:
        keychain = " %" + greek.upper()
    else:
        keychain = " %" + greek
    Text(keychain).execute()

def insert(element):
    if type(element) is str:
        n_markers = 0
        to_enter = element
    else:
        n_markers = element[1]
        to_enter = element[0]
    Text(to_enter).execute()
    for _ in range(n_markers):
        Key("s-f4").execute()

def matrix(blank, rows, cols):
    if blank:
        text = "matrix{"
    else:
        text = "left [ matrix{"
    for i in range(0, rows):
        text+="<?>"
        for _ in range(0, cols-1):
            text+= " # <?>"
        if i!=rows-1:
            text+=" ## "
    if blank:
        text+="} <?>"
    else:
        text+="} right ] <?>"
    Text(text).execute()
    for _ in range((rows*cols) + 1):
        Key("s-f4").execute()

class mathematics(MergeRule):
    pronunciation = "mathematics"

    mapping = {
        "next [<n>]": R(Key("f4"))*Repeat(extra="n"),
        "previous [<n>]": R(Key("s-f4"))*Repeat(extra="n"),
        "new line": R(Key("enter, n, e, w, l, i, n, e, enter")),
        #
        "<element>": R(Function(insert)),
        #
        "greek [<big>] <greek>": R(Function(greek)),

        "accent <accent>": R(Text("%(accent)s ")),

        "[<blank>] matrix <rows> by <cols>": R(Function(matrix)),
        #
        "over": R(Key("c-x") + Function(insert, element=("{<?>} over {<?>} <?>", 3)) + Key("c-v, f4")),
        "not equal": R(Text(" <> ")),
        "squared": R(Text("^{2}")),
        "prime": R(Key("apostrophe")),
        "thick space": R(Key("space, tilde, space")),
        
    }

    extras = [
        IntegerRefST("n", 1, 6),
        IntegerRefST("rows", 1, 6),
        IntegerRefST("cols", 1, 6),
        Choice("element", {
                # functions
                "absolute": ("abs{<?>} <?>", 2),
                "factorial": ("fact{<?>} <?>", 2),
                "log (nat | natural)": ("ln{<?>} <?>", 2),
                "log": ("log{<?>} <?>", 2),
                "exponential": ("exp{<?>} <?>", 2),
                "E to the": ("func e^{<?>} <?>", 2),
                "(power | super [script])": ("^{<?>} <?>", 2),
                "sub [script]": ("_{<?>} <?>", 2),

                "sine": ("sin(<?>) <?>", 2),
                "cosine": ("cos(<?>) <?>", 2),
                "tangent": ("tan(<?>) <?>", 2),
                "square root": ("sqrt{<?>} <?>", 2),
                "root": ("nroot{<?>}{<?>} <?>", 3),
                # operators
                "fraction": ("{<?>} over {<?>} <?>", 3),
                "times": " times ",
                "product": " otimes ",
                "divide": " div ",
                "dot": " cdot ",
                #
                "limit": ("lim from{<?>} <?>", 2),
                "(probability | P) limit": ("p lim <?>", 1),
                "integral": ("lim from{<?>} to{<?>} <?>", 3),
                "(sum | summation)": ("sum from{<?>} to{<?>} <?>", 3),
                #
                "right arrow": "rightarrow ",
                "left arrow": "leftarrow ",
                "up arrow": "uparrow ",
                "down arrow": "downarrow ",
                "for all": "forall ",
            }),

        Choice("greek", {
            "alpha":"alpha", "beater":"beta", "gamma":"gamma", "delta":"delta", "epsilon":"epsilon",
            "zita":"zeta", "eater":"eta", "theta":"theta", "iota":"iota", "kappa":"kappa",
            "lambda":"lambda", "mu":"mu",
            #"new":"new",
            "zee":"xi", "pie":"pi", "row":"rho",
            "sigma":"sigma", "tau":"tau", "upsilon":"upsilon", "phi":"phi", "chi":"chi",
            "sigh":"psi", "omega":"omega",

            }),
        Choice("big", {"big": True}),
        Choice("blank", {"blank": True}),

        Choice("accent", {
            "hat":"hat",
            "tilde":"tilde",
            "dot":"dot",
            "double dot":"ddot",
            "bar":"bar",
        }),
    ]
    defaults = {
        "big": False,
        "blank": False
    }

control.nexus().merger.add_global_rule(mathematics())
