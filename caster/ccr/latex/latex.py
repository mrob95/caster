'''
Created on Sep 4, 2018

@author: Mike Roberts
'''
from dragonfly import Function, Choice
from caster.lib.actions import Key, Text, Mouse

from caster.ccr.standard import SymbolSpecs
from caster.lib import control, utilities
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.user.latex import word_counter

# from caster.lib.terminal import terminal_command


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

def begin_end(element):
    if type(element) in [str, unicode]:
        back_curl("begin", element).execute()
        Key("enter:2").execute()
        back_curl("end", element).execute()
        Key("up").execute()
    elif type(element) in [tuple, list]:
        back_curl("begin", element[0]).execute()
        Text(element[1]).execute()
        Key("enter:2").execute()
        back_curl("end", element[0]).execute()
        Key("up").execute()

class LaTeX(MergeRule):
    pronunciation = "latex"

    mapping = {
        SymbolSpecs.COMMENT:
            R(Text("%"), rdescript="LaTeX: Add Comment"),
        # "begin <element>":
        #     R(back_curl("begin", "%(element)s") + Key("enter:2") + back_curl(
        #         "end", "%(element)s") + Key("up"),
        #       rdescript="LaTeX: Define beginning and end of an element"),
        "begin <element>":
            R(Function(begin_end, extra={"element"})),
        #
        "[use] package [<packopts>]":
            R(Function(packages, extra={"packopts"}), rdescript="LaTeX: Import packages"),
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
            R(Text("``\'\'") + Key("left:2"), rdescript="LaTeX: Insert a quote"),
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

        "insert standard header":
            R(Text("\\documentclass[12pt, a4paper]{article}\n\n\\usepackage{graphicx}\n\n\\usepackage[english]{babel}\n\n" +
            "\\usepackage[utf8]{inputenc}\n\n\\usepackage[style=authoryear]{biblatex}\n" +
            "\\addbibresource{C:/Users/Mike/Documents/1 uni work/bibliography.bib}\n\n\\setlength{\parskip}{1em}\n\\renewcommand{\\baselinestretch}{1.3}")),

        # "test data": R(Function(utilities.save_toml_file, data={
        #     "bib latex":("[style=authoryear]", "biblatex"),
        #     "colour":("color", 3),
        #     "math tools": "mathtools",
        #     "multi col":"multicol",
        #     "geometry":"geometry",
        #     "graphic ex": "graphicx",
        #     "wrap figure": "wrapfig",
        # }, path="C:/Users/Mike/Documents/NatLink/ud2/caster/ccr/latex/test.toml")),

        # "<index_operator> from":R(Text("\%(index_operator)s _")),
        # "until": R(Key("right, caret")),

    }

    extras = [
        utilities.Choice_from_file("packopts", [utilities.get_full_path("caster/ccr/latex/latex.toml"), "packopts"]),
        # Choice("packopts", {
        #     "bib latex":("[style=authoryear]", "biblatex"),
        #     "colour":"color",
        #     "math tools": "mathtools",
        #     "multi col":"multicol",
        #     "geometry":"geometry",
        #     "graphic ex": "graphicx",
        #     "wrap figure": "wrapfig",
        # }),
        Choice(
            "element", {
                "add margin":"addmargin",
                "center": "center",
                "columns": "columns",
                "description": "description",
                "document": "document",
                "(enumerate | numbered list)": "enumerate",
                "equation": "equation",
                "figure": ("figure", "[h!]"),
                "flush left": "flushleft",
                "flush right": "flushright",
                "frame": "frame",
                "(list | itemise)": "itemize",
                "mini page": "minipage",
                "multi (cols | columns)":("multicols", "{2}"),
                "quotation": "quotation",
                "quote": "quote",
                "table": ("table", "[h!]\n\\centering"),
                "tabular": ("tabular", "{llll}"),
                "title page": "titlepage",
                "verbatim": "verbatim",
                "verse": "verse",
                "wrap figure": "wrapfigure",
            }),
        Choice(
            "command", {
                "author": "author",
                "[add] bib resource": "addbibresource",
                "caption": "caption",
                "chapter": "chapter",
                "column": "column",
                "document class": "documentclass",
                "footnote":"footnote",
                "footnote text":"footnotetext[]",
                "graphics path": "graphicspath",
                "[include] graphics": "includegraphics[width=1\\textwidth]",
                "label": "label",
                "new command": "newcommand\{\}[]",
                "paragraph": "paragraph",
                "paren cite": "parencite",
                "part": "part",
                "reference": "ref",
                "renew command":"renewcommand",
                "sub paragraph": "subparagraph",
                "(section | heading)": "section",
                "sub (section | heading)": "subsection",
                "sub sub (section | heading)": "subsubsection",
                "text cite": "textcite",
                "[text] bold": "textbf",
                "[text] italics": "textit",
                "[text] slanted": "textsl",
                "title": "title",
                "use theme": "usetheme",
            }),
        Choice(
            "commandnoarg", {
                "centring":"centering",
                "footnote mark":"footnotemark[]",
                "horizontal line":"hline",
                "line break": "linebreak",
                "[list] item": "item",
                "make title": "maketitle",
                "new page": "newpage",
                "page break": "pagebreak",
                "print bibliography": "printbibliography",
                "table of contents": "tableofcontents",
                "text width": "textwidth",
                "vertical line": "vline",
            }),
        # Choice(
        #     "symbol",
        #     {
        #         "alpha": "alpha",
        #         "beater": "beta",
        #         "gamma": "gamma",
        #         "delta": "delta",
        #         "epsilon": "epsilon",
        #         "zita": "zeta",
        #         "eater": "eta",
        #         "theta": "theta",
        #         "iota": "iota",
        #         "kappa": "kappa",
        #         "lambda": "lambda",
        #         "mu": "mu",
        #         "new": "nu",
        #         "zee": "xi",
        #         "pie": "pi",
        #         "row": "rho",
        #         "sigma": "sigma",
        #         "tau": "tau",
        #         "upsilon": "upsilon",
        #         "phi": "phi",
        #         "chi": "chi",
        #         "sigh": "psi",
        #         "omega": "omega",
        #         #
        #         "times": "times",
        #         "divide": "div",
        #         "intersection": "cap",
        #         "union": "cup",
        #         "stop": "cdot",
        #         "approximate": "approx",
        #         "proportional": "propto",
        #         "not equal": "neq",
        #         "member": "in",
        #         "for all": "forall",
        #         "partial": "partial",
        #         "infinity": "infty",
        #         "dots": "dots",
        #         #
        #         "left arrow": "leftarrow",
        #         "right arrow": "rightarrow",
        #         "up arrow": "uparrow",
        #         "down arrow": "downarrow",
        #         #
        #         "left": "left(",
        #         "right": "right)",
        #     }),
        utilities.Choice_from_file("symbol", [utilities.get_full_path("caster/ccr/latex/latex.toml"), "symbol"]),
        Choice("big", {
            "big": "big",
        }),
    ]
    defaults = {
        "big": "",
        "packopts": "",
    }


control.nexus().merger.add_global_rule(LaTeX())
