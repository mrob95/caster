#
# This file is a command-module for Dragonfly.
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#
"""
Command-module for Chrome and Firefox

"""
#---------------------------------------------------------------------------

from dragonfly import (Grammar, Dictation, Repeat, Choice, Clipboard, Function)
from caster.lib.actions import Key, Text
from caster.lib.context import AppContext

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.user.latex import bibtexer
from caster.user.latex import book_citation_generator

class ChromeRule(MergeRule):
    pronunciation = "google chrome"

    mapping = { # most keybinds are taken from https://support.google.com/chrome/answer/157179?hl=en
        "[new] incognito window":       R(Key("cs-n"), rdescript="Browser: New Incognito Window"),
        "new tab [<n>]":                R(Key("c-t"), rdescript="Browser: New Tab") * Repeat(extra="n"),
        "reopen tab [<n>]":             R(Key("cs-t"), rdescript="Browser: Reopen Tab") * Repeat(extra="n"),
        "close all tabs":               R(Key("cs-w"), rdescript="Browser: Close All Tabs"),

        "page back [<n>]":                R(Key("a-left/20"), rdescript="Browser: Navigate History Backward") * Repeat(extra="n"),
        "page forward [<n>]":             R(Key("a-right/20"), rdescript="Browser: Navigate History Forward") * Repeat(extra="n"),
        "zoom in [<n>]":                R(Key("c-plus/20"), rdescript="Browser: Zoom In") * Repeat(extra="n"),
        "zoom out [<n>]":               R(Key("c-minus/20"), rdescript="Browser: Zoom") * Repeat(extra="n"),
        "zoom reset":                   R(Key("c-0"), rdescript="Browser: Reset Zoom"),
        "refresh":                      R(Key("c-f5"), rdescript="Browser: Super Refresh"),
        "switch focus [<n>]":           R(Key("f6/20"), rdescript="Browser: Switch Focus") * Repeat(extra="n"),
        "[find] next match [<n>]":      R(Key("c-g/20"), rdescript="Browser: Next Match") * Repeat(extra="n"),
        "[find] prior match [<n>]":     R(Key("cs-g/20"), rdescript="Browser: Prior Match") * Repeat(extra="n"),
        "[toggle] caret browsing":      R(Key("f7"), rdescript="Browser: Caret Browsing"), # now available through an add on, was a standard feature

        "home page":                    R(Key("a-home"), rdescript="Browser: Home Page"),
        "show history":                 R(Key("c-h"), rdescript="Browser: Show History"),
        "[google] search":              R(Key("c-l"), rdescript="Browser: Address Bar"),
        "show downloads":               R(Key("c-j"), rdescript="Browser: Show Downloads"),
        "[add] bookmark":               R(Key("c-d"), rdescript="Browser: Add Bookmark"),
        "bookmark all tabs":            R(Key("cs-d"), rdescript="Browser: Bookmark All Tabs"),
        "[toggle] bookmark bar":        R(Key("cs-b"), rdescript="Browser: Toggle Bookmark Bar"),
        "show bookmarks":               R(Key("cs-o"), rdescript="Browser: Show Bookmarks"),
        "switch user":                  R(Key("cs-m"), rdescript="Browser: Switch User"),
        "chrome task manager":          R(Key("s-escape"), rdescript="Browser: Chrome Task Manager"),
        "[toggle] full-screen":         R(Key("f11"), rdescript="Browser: Toggle Fullscreen Mode"),
        "focus notification":           R(Key("a-n"), rdescript="Browser: Focus Notification"),
        "allow notification":           R(Key("as-a"), rdescript="Browser: Allow Notification"),
        "deny notification":            R(Key("as-a"), rdescript="Browser: Deny Notification"),

        "developer tools":              R(Key("f12"), rdescript="Browser: Developer Tools"),
        "view [page] source":           R(Key("c-u"), rdescript="Browser: View Page Source"),
        "resume":                       R(Key("f8"), rdescript="Browser: Resume"),
        "step over":                    R(Key("f10"), rdescript="Browser: Step Over"),
        "step into":                    R(Key("f11"), rdescript="Browser: Step Into"),
        "step out":                     R(Key("s-f11"), rdescript="Browser: Step Out"),

        # "IRC identify":                 R(Text("/msg NickServ identify PASSWORD"), rdescript="IRC Chat Channel Identify"),

        "<numberth> tab":
            R(Key("c-%(numberth)s")),

        "copy all":
            R(Key("c-a/20, c-c")),

        "go <site>":
            R(Key("c-l/10") + Text("%(site)s") + Key("del, enter")),
        "search <text>":
            R(Key("c-l/10") + Text("%(text)s") + Key("enter")),

        "add to bibliography":
            R(Function(bibtexer.save_bibtex_to_bib)),

        "add link to bibliography":
            R(Function(bibtexer.save_link_to_bib)),

        "add good reads to bibliography":
            R(Function(book_citation_generator.save_goodreads_link_to_bib)),

        "create latex table":
            R(Function(bibtexer.html_table_to_latex_clipboard)),

        "science hub": R(Key("a-d, c-x") + Text("https://sci-hub.tw/") + Key("c-v, enter")),
        }
    extras = [
        Dictation("dict"),
        Dictation("text"),
        IntegerRefST("n", 1, 10),
        Choice("site", {
            "amazon":"smile.amazon.co.uk",
            "facebook":"facebook.com",
            "scholar":"scholar.google.co.uk",
            "spectator":"spectator.co.uk",
            "times":"thetimes.co.uk",
            "twitter":"twitter.com",
            "youtube":"youtube.com",
        }),
        Choice("numberth", {
            "first": "1",
            "second": "2",
            "third": "3",
            "fourth": "4",
            "fifth": "5",
            "sixth": "6",
            "seventh": "7",
            "eighth": "8",
            "ninth": "9",
            "next":"pgdown",
            "previous":"pgup",

        }),
    ]
    defaults = {"n": 1, "dict": "nothing"}


#---------------------------------------------------------------------------

context = AppContext(executable="chrome")
grammar = Grammar("chrome", context=context)

if settings.SETTINGS["apps"]["chrome"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(ChromeRule())
    else:
        rule = ChromeRule(name="chrome")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
