from dragonfly import (Grammar, Dictation, Choice, Repeat)
from caster.lib.actions import Key, Text
from caster.lib.context import AppContext

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class SublimeRule(MergeRule):
    pronunciation = "sublime"
    # mwith = ["navigation", "alphabet", "punctuation", "mine", "numbers", "python", "Go"]


    mapping = {
        "new (file | pane)": R(Key("c-n"), rdescript="Sublime: New File"),
        # {"keys": ["ctrl+alt+n"], "command": "new_window"}, 
        "new window":   R(Key("ca-n"), rdescript="Sublime: New Window"),
        "open file":    R(Key("c-o"), rdescript="Sublime: Open File"),
        # {"keys": ["ctrl+shift+o"], "command": "prompt_add_folder"},
        "open folder":  R(Key("cs-o"), rdescript="Sublime: Open Folder"),
        "save as":  R(Key("cs-s"), rdescript="Sublime: Save As"),
        #
        "comment line": R(Key("c-slash"), rdescript="Sublime: Comment Line"),
        "comment (block | lines)":    R(Key("cs-slash"), rdescript="Sublime: Comment Block"),
        "outdent lines":    R(Key("c-lbracket"), rdescript="Sublime: Outdent Lines"),
        "join lines [<n3>]":    R(Key("c-j"), rdescript="Sublime: Join Lines")*Repeat(extra="n3"),
        "match bracket":    R(Key("c-m"), rdescript="Sublime: Match Current Bracket"),
        #
        # "(select | sell) all":  R(Key("c-a"), rdescript="Sublime: Select All"),
        "(select | sell) scope [<n2>]": R(Key("cs-space"), rdescript="Sublime: Select Scope")*Repeat(extra="n2"),
        "(select | sell) brackets [<n2>]":  R(Key("cs-m"), rdescript="Sublime: Select Brackets")*Repeat(extra="n2"),
        "(select | sell) line [<n2>]":  R(Key("c-l"), rdescript="Sublime: Select lines")*Repeat(extra="n2"),
        "(select | sell) indent":   R(Key("cs-j"), rdescript="Sublime: Select Indent"),
        # {"keys": ["ctrl+alt+p"], "command": "expand_selection_to_paragraph"},
        "(select | sell) paragraph":    R(Key("ca-p"), rdescript="Sublime: Select Paragraph"),
        # SelectUntil
        "(select | sell) until":    R(Key("as-s"), rdescript="Sublime: Select Paragraph"),
    
        "toggle side bar": R(Key("c-k, c-b")),
        "duplicate": R(Key("cs-d")),

        #
        # "find": R(Key("c-f"), rdescript="Sublime: Find"),
        "get all":  R(Key("a-enter"), rdescript="Sublime: Get All"),
        "replace":  R(Key("c-h"), rdescript="Sublime: Find And Replace"),
        "edit lines":   R(Key("cs-l"), rdescript="Sublime: Edit Selected Lines"),
        "edit next [<n3>]": R(Key("c-d"), rdescript="Sublime: Edit Next n")*Repeat(extra="n3"),
        "edit skip next [<n3>]": R(Key("c-k, c-d"), rdescript="Sublime: Edit Next n")*Repeat(extra="n3"),
        "edit all": R(Key("c-d, a-f3"), rdescript="Sublime: Edit All Instances"),
        #
        "transform upper":  R(Key("c-k, c-u"), rdescript="Sublime: Transform Upper"),
        "transform lower":  R(Key("c-k, c-l"), rdescript="Sublime: Transform Lower"),
        # {"keys": ["ctrl+k", "ctrl+t"], "command": "title_case"},
        "transform title":  R(Key("c-k, c-t"), rdescript="Sublime: Transform Title"),
        #
        "line <n11> [<n12>]": R(Key("c-g") + Text("%(n11)s" + "%(n12)s") + Key("enter"), rdescript="Sublime: Line n"),
        "go to file":   R(Key("c-p"), rdescript="Sublime: Go To"),
        "go to word":   R(Key("c-semicolon"), rdescript="Sublime: Go To"),
        "go to symbol": R(Key("c-r"), rdescript="Sublime: Go To"),
        "go to [symbol in] project": R(Key("cs-r"), rdescript="Sublime: Go To"),
        "command pallette": R(Key("cs-p"), rdescript="Sublime: Command Pallette"),
        "(find | search) in (project | folder | directory)": R(Key("cs-f")),
        #
        "fold": R(Key("cs-lbracket"), rdescript="Sublime: Fold"),
        "unfold":   R(Key("cs-rbracket"), rdescript="Sublime: Unfold"),
        "unfold all":   R(Key("c-k, c-j"), rdescript="Sublime: Unfold All"),
        "fold [level] <n2>":    R(Key("c-k, c-%(n2)s"), rdescript="Sublime: Fold Level 1-9"),
        #
        "full screen":  R(Key("f11"), rdescript="Sublime: Fullscreen"),
        "(set | add) bookmark": R(Key("c-f2"), rdescript="Sublime: Set Bookmark"),
        "next bookmark":    R(Key("f2"), rdescript="Sublime: Next Bookmark"),
        "previous bookmark":    R(Key("s-f2"), rdescript="Sublime: Previous Bookmark"),
        "clear bookmarks":  R(Key("cs-f2"), rdescript="Sublime: Clear Bookmarks"),
        #
        "build it": R(Key("c-b"), rdescript="Sublime: Build It"),
        # "cancel build": R(Key("c-break")),
        #
        "record macro": R(Key("c-q"), rdescript="Sublime: Record Macro"),
        "play [back] macro [<n3>]": R(Key("cs-q"), rdescript="Sublime: Play Macro")*Repeat(extra="n3"),
        "(new | create) snippet":   R(Key("a-n"), rdescript="Sublime: New Snippet"),
        #
        "close tab":   R(Key("c-w"), rdescript="Sublime: Close Window"),
        "next tab":    R(Key("c-pgdown"), rdescript="Sublime: Next Tab"),
        "previous tab":    R(Key("c-pgup"), rdescript="Sublime: Previous Tab"),
        "<nth> tab":    R(Key("a-%(n2)s"), rdescript="Sublime: Tab n"),
        #
        "column <cols>":    R(Key("as-%(cols)s"), rdescript="Sublime: Column"),
        "focus <panel>":    R(Key("c-%(panel)s"), rdescript="Sublime: Focus Panel n"),
        "move <panel>": R(Key("cs-%(panel)s"), rdescript="Sublime: Move File to Panel n"),
        # {"keys": ["ctrl+alt+v"], "command": "clone_file"}
        "split right":  R(Key("as-2, c-1, ca-v, cs-2")),
        #
        "open terminal":    R(Key("cs-t"), rdescript="Sublime: Open Terminal Here"),

        "zoom in [<n2>]":   R(Key("c-equal"))*Repeat(extra="n2"),
        "zoom out [<n2>]":   R(Key("c-minus"))*Repeat(extra="n2"),

    }
    extras = [
        IntegerRefST("n11", 1, 100),
        IntegerRefST("n12", 0, 100),
        IntegerRefST("n2", 1, 9),
        IntegerRefST("n3", 1, 21),
        Choice("nth", {
            "first": "1",
            "second": "2",
            "third": "3",
            "fourth": "4",
            "fifth": "5",
            "sixth": "6",
            "seventh": "7",
            "eighth": "8",
            "ninth": "9",
            "tenth": "10",
            }),
        Choice("cols", {
            "one": "1",
            "two": "2",
            "three": "3",
            "grid": "5",
        }),
        Choice("panel", {
            "one": "1",
            "left": "1",
            "two": "2",
            "right": "2",
            }),
    ]
    defaults = {
        "n12": "",
        "n2": 1,
        "n3": 1,
    }


#---------------------------------------------------------------------------

context = AppContext(executable="sublime_text", title="Sublime Text")
grammar = Grammar("Sublime", context=context)

if settings.SETTINGS["apps"]["sublime"]:
    rule = SublimeRule(name="sublime")
    gfilter.run_on(rule)
    grammar.add_rule(rule)
    grammar.load()
