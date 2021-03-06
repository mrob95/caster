'''
Created on Sep 4, 2018

@author: Mike Roberts
'''
import re
from dragonfly import Function, Choice
from caster.lib.actions import Key, Text, Mouse

from caster.ccr.standard import SymbolSpecs
from caster.lib import control, utilities, context
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.user.latex import word_counter

BINDINGS = utilities.load_toml_file(utilities.get_full_path("caster/ccr/latex/latex.toml"))

def quote():
    e, text = context.read_selected_without_altering_clipboard(False)
    if text:
        Text("``" + text + "\'\'").execute()
    else:
        Text("``\'\'").execute()
        Key("left:2").execute()

# Return \first{second}, if second is empty then end inside the brackets for user input
def back_curl(first, second):
    if str(second) != "":
        return (Text("\\") + Text(str(first)) + Key("lbrace, rbrace, left") + Text(
            str(second)) + Key("right"))
    if str(second) == "":
        return (Text("\\") + Text(str(first)) + Key("lbrace, rbrace, left"))


def symbol_letters(big, symbol):
    if big == "big":
        symbol = symbol.title()
    Text(str(symbol)).execute()

def packages(packopts):
    if type(packopts) in [str, unicode]:
        back_curl("usepackage", packopts).execute()
    elif type(packopts) in [tuple, list]:
        back_curl("usepackage" + packopts[0], packopts[1]).execute()

def begin_end(environment):
    if type(environment) in [str, unicode]:
        back_curl("begin", environment).execute()
        Key("enter:2").execute()
        back_curl("end", environment).execute()
        Key("up").execute()
    elif type(environment) in [tuple, list]:
        back_curl("begin", environment[0]).execute()
        Text(environment[1]).execute()
        Key("enter:2").execute()
        back_curl("end", environment[0]).execute()
        Key("up").execute()

class LaTeX(MergeRule):
    pronunciation = "latex"

    mapping = {
        SymbolSpecs.COMMENT:
            R(Text("%"), rdescript="LaTeX: Add Comment"),

        "document class [<class>]":
            R(back_curl("documentclass", "%(class)s")),

        "begin <environment>":
            R(Function(begin_end)),
        #
        "[use] package [<packopts>]":
            R(Function(packages), rdescript="LaTeX: Import packages"),
        #
        "symbol [<big>] <symbol>":
            R(Text("\\") + Function(symbol_letters, extra={"big", "symbol"}) + Key("space"),
              rdescript="LaTeX: Insert symbols"),
        #
        "insert <command>":
            R(back_curl("%(command)s", ""),
            rdescript="LaTeX: Insert command requiring an argument"),
        "insert <commandnoarg>":
            R(Text("\\%(commandnoarg)s "),
            rdescript="LaTeX: Insert command not requiring an argument"),
        
        "insert my bib resource":
            R(back_curl("addbibresource", "C:/Users/Mike/Documents/1 uni work/bibliography.bib")),

        "insert quote":
            R(Function(quote), rdescript="LaTeX: Insert a quote"),
        #
        "superscript":
            R(Text("^") + Key("lbrace, rbrace, left"), rdescript="LaTeX: Superscript"),
        "subscript":
            R(Text("_") + Key("lbrace, rbrace, left"), rdescript="LaTeX: Subscript"),
        "math fraction":
            R(Text("\\") + Text("frac") +
                Key("lbrace, rbrace, lbrace, rbrace, space, left:4"),
                rdescript="LaTeX: Fraction"),

        "(get | show) word count":
            R(Key("c-a") + Function(word_counter.print_count_from_selection) + Key("escape")),

        # "insert standard header":
        #     R(Text("\\documentclass[12pt, a4paper]{article}\n\n\\usepackage{graphicx}\n\n\\usepackage[english]{babel}\n\n" +
        #     "\\usepackage[utf8]{inputenc}\n\n\\usepackage[style=authoryear]{biblatex}\n" +
        #     "\\addbibresource{C:/Users/Mike/Documents/1 uni work/bibliography.bib}\n\n\\setlength{\parskip}{1em}\n\\renewcommand{\\baselinestretch}{1.3}")),

        "insert <template>": R(Text("%(template)s")),

    }

    extras = [
        Choice("packopts", BINDINGS["packages"]),
        Choice("class", BINDINGS["document_classes"]),
        Choice("symbol", BINDINGS["symbol"]),
        Choice("commandnoarg", BINDINGS["commandnoarg"]),
        Choice("command", BINDINGS["command"]),
        Choice("environment", BINDINGS["environments"]),
        Choice("big", {
            "big": "big",
        }),
        Choice("template", BINDINGS["templates"]),
    ]
    defaults = {
        "big": "",
        "packopts": "",
        "class": "",
    }


control.nexus().merger.add_global_rule(LaTeX())
