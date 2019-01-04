from dragonfly import Function, Choice
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.lib.dfplus.additions import IntegerRefST

def table_row(n):
    row = "|"*(n-1)
    Text(row).execute()

def table_split(n):
    row = "---|"*(n-1) + "---"
    Text(row).execute()

class Markdown(MergeRule):
    pronunciation = "markdown"

    mapping = {
        "add horizontal rule":
            R(Text("---")),
        "add heading":
            R(Text("# ")),
        "add subheading":
            R(Text("## ")),
        "add sub sub heading":
            R(Text("### ")),
        "add link":
            R(Key("lbracket, rbracket, lparen, rparen, left:3")),
        "add reference":
            R(Key("lbracket, rbracket, left, at")),
        "add equation":
            R(Key("dollar, dollar, enter:2, dollar, dollar, up")),
        "add math":
            R(Key("dollar, dollar, left")),
        "dot MD":
            R(Text(".md")),
        "table (break | split) <n>":
            R(Function(table_split, extra={"n"}) + Key("enter")),
        "table row <n>":
            R(Function(table_row, extra={"n"}) + Key("home")),
        "text italics":
            R(Key("underscore:2, left")),
        "text bold":
            R(Key("asterisk:4, left:2")),

        "insert are code":
            R(Key("backtick:3, lbrace, r") + Text("") + Key("rbrace, enter:2, backtick:3, up")),

        "insert hidden code":
            R(Key("backtick:3") + Text("{r, include=FALSE}") + Key("enter:2, backtick:3, up")),

        "output <output>":
            R(Text("%(output)s")),

        "option <option>":
            R(Text("%(option)s")),
        }

    extras = [
        IntegerRefST("n", 1, 12),
        Choice("output", {
            "beamer [presentation]":"output:\nbeamer_presentation:\ndf_print: kable\ntheme: metropolis",
            "HTML": "html_document",
            "PDF":"output:\npdf_document:\ndf_print: kable",
            "word":"output:\nword_document",
        }),
        Choice("option", {
            "author":"author: ",
            "bibliography": "bibliography: ",
            "date":"date: ",
            "figure width":"fig_width: ",
            "figure height":"fig_height: ",
            "figure caption":"fig_caption: true",
            "font size":"fontsize: 11pt",
            "keep tex":"keep_tex: true",
            "small output":"header-includes:\n- \\let\\oldverbatim\\verbatim\n- \\def\\verbatim{\\tiny \\oldverbatim}",
            "table of contents":"toc: true",
            "title":"title: ",
        })
    ]
    defaults = {}

control.nexus().merger.add_global_rule(Markdown())
