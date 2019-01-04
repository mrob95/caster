from dragonfly import Choice, Repeat
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.ccrmerger import CCRMerger
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class Punctuation(MergeRule):
    pronunciation = "punctuation"

    mapping = {
        "semper":
            R(Key("semicolon"), rdescript="Semicolon"),
        "quotes":
            R(Key("dquote"), rdescript="Quotation Marks"),
        "thin quotes":
            R(Key("apostrophe,apostrophe,left"), rdescript="Thin Quotation Marks"),
        "[<long>] greater than":
            R(Text("%(long)s" + ">" + "%(long)s"), rdescript="> Comparison"),
        "[<long>] less than":
            R(Text("%(long)s" + "<" + "%(long)s"), rdescript="< Comparison"),
        "[<long>] greater [than] [or] equal [to]":
            R(Text("%(long)s" + ">=" + "%(long)s"), rdescript=">= Comparison"),
        "[<long>] less [than] [or] equal [to]":
            R(Text("%(long)s" + "<=" + "%(long)s"), rdescript="<= Comparison"),
        "[<long>] equal to":
            R(Text("%(long)s" + "==" + "%(long)s"), rdescript="Equality"),
        "[<long>] not equal":
            R(Text("%(long)s" + "!=" + "%(long)s")),
        "[<long>] equals":
            R(Text("%(long)s" + "=" + "%(long)s"), rdescript="Equals Sign"),
        "prekris":
            R(Key("lparen, rparen, left"), rdescript="Parentheses"),
        "brax":
            R(Key("lbracket, rbracket, left"), rdescript="Square Brackets"),
        "curly":
            R(Key("lbrace, rbrace, left"), rdescript="Curly Braces"),
        "angle":
            R(Key("langle, rangle, left"), rdescript="Angle Brackets"),
        "[<long>] plus":
            R(Text("%(long)s" + "+" + "%(long)s"), rdescript="Plus Sign"),
        "[<long>] minus":
            R(Text("%(long)s" + "-" + "%(long)s"), rdescript="Dash"),
        "pipe (sim | symbol)":
            R(Text("|"), rdescript="Pipe Symbol"),
        'ace [<npunc>]':
            R(Key("space"), rdescript="Space")*Repeat(extra="npunc"),
        "clamor":
            R(Text("!"), rdescript="Exclamation Mark"),
        "(deckle | colon)":
            R(Text(":"), rdescript="Colon"),
        "starling":
            R(Key("asterisk"), rdescript="Asterisk"),
        "questo":
            R(Text("?"), rdescript="Question Mark"),
        "comma":
            R(Text(","), rdescript="Comma"),
        "carrot":
            R(Text("^"), rdescript="Carat"),  
        "point":
            R(Text("."), rdescript="Dot"),
        "at sign":
            R(Text("@"), rdescript="At Sign"),
        "hash tag":
            R(Text("#"), rdescript="Hash Tag"),
        "apostrophe":
            R(Text("'"), rdescript="Apostrophe"),
        "underscore":
            R(Text("_"), rdescript="Underscore"),
        "backslash":
            R(Text("\\"), rdescript="Back Slash"),
        "slash":
            R(Text("/"), rdescript="Forward Slash"),
        "dollar sign":
            R(Text("$"), rdescript="Dollar Sign"),
        "modulo":
            R(Key("percent"), rdescript="Percent Sign"),
        'tabby [<direction>] [<npunc>]':
            R(Key("%(direction)s" + "tab"), rdescript="Tab")*Repeat(extra="npunc"),
        "boom":
            R(Text(", "), rdescript="Comma + Space"),
        "ampersand":
            R(Key("ampersand"), rdescript="Ampersand"),
        "tilde":
            R(Key("tilde")),
        "back tick":
            R(Key("backtick")),

    }

    extras = [
        IntegerRefST("npunc", 0, 10),
        Choice("long", {
            "long": " ",
        }),
        Choice("direction", {
                "lease": "s-",
            }),
    ]
    defaults = {
        "npunc": 1,
        "long": "",
        "direction": "",
    }


control.nexus().merger.add_global_rule(Punctuation())
