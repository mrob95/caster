from dragonfly import Repeat, Function, FocusWindow, BringApp, FocusWindow
from dragonfly import Dictation, Choice, MappingRule, Clipboard, Playback
from caster.lib.actions import Key, Text, Mouse

from caster.ccr.recording import alias
from caster.lib import context, navigation, alphanumeric, textformat, control
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge.ccrmerger import CCRMerger
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import L, S, R
from caster.lib import settings, utilities

from caster.user.latex import book_citation_generator, bibtexer
from caster.user.window_switcher import window_switcher
from caster.user.personal import personal
from caster.user.clipshow import clip_transparent
from subprocess import Popen

class MineNon(MappingRule):
	mapping = {	
       	# "switch <exec_path>":
        #     R(Function(window_switcher.switch_window)),
        # "switch notepad":
        # 	R(Playback([(["switch", "to", "notepad"], 0.0)])),
        # "switch kindle":
        # 	R(Playback([(["switch", "to", "kindle"], 0.0)])),
        # "switch spot if I":
        # 	R(Playback([(["switch", "to", "spotify"], 0.0)])),
        # "switch file man":
        # 	R(Playback([(["switch", "to", "fman"], 0.0)])),
  
        # "open spot if I":
        # 	R(Playback([(["open", "spotify"], 0.0)])),
        # "open file man":
        # 	R(Playback([(["open", "fman"], 0.0)])),
		"show work [spaces]":
            R(Key("w-tab")),
        "(create | new) work [space]":
            R(Key("wc-d")),
        "close work [space]":
            R(Key("wc-f4")),
        "next work [space] [<n>]":
            R(Key("wc-right"))*Repeat(extra="n"),
        "(previous | prior) work [space] [<n>]":
            R(Key("wc-left"))*Repeat(extra="n"),

        


		# "normal mode":
		# 	R(Playback([(["switch", "to", "normal", "mode"], 0.0)])),
		# "command mode":
		# 	R(Playback([(["switch", "to", "command", "mode"], 0.0)])),
		# "dictation mode":
		# 	R(Playback([(["switch", "to", "dictation", "mode"], 0.0)])),

		}

	extras = [
		window_switcher.get_choice(),
		IntegerRefST("n", 1, 5),
	]
	defaults = {
		"n": 1,
	}
            

def vary(capitalization, spacing, textnv):
    textnv2 = textformat.TextFormat.formatted_text(capitalization, spacing, str(textnv))
    Text(textnv2).execute()
    a = alias.Alias()
    a.refresh(str(textnv), textnv2)

class Mine(MergeRule):
	non = MineNon

	pronunciation = "mine"

	mapping = {
        # "vary (<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel) <textnv> [brunt]":
        #     R(Function(vary), rdescript="Text Format"),

        "super hold":        Key("win:down"),
        "super release":     Key("win:up"),
        "shift hold":        Key("shift:down"),
        "shift release":     Key("shift:up"),
        "control hold":      Key("ctrl:down"),
        "control release":   Key("ctrl:up"),
        "(meta|alt) hold":   Key("alt:down"),
        "(meta|alt) release":Key("alt:up"),
        "all release":       Key("win:up, shift:up, ctrl:up, alt:up"),
        "release all":       Key("win:up, shift:up, ctrl:up, alt:up"),


        "shift (look | click)":
            R(Key("shift:down") + Mouse("left") + Key("shift:up"),
            rdescript="Mouse: Shift Click"),

        "<personal>":
            R(Text("%(personal)s")),

        "add title to bibliography":
            R(Function(bibtexer.save_title_to_bib)),

        "add book to bibliography":
            R(Function(book_citation_generator.save_book_title_to_bib)),

        "close dragon":
            R(Key("")),

        "(eskimo | escape)":
            R(Key("escape")),

        "check [<n>]":
        	R(Key("c-enter"))*Repeat(extra="n"),

        "select all":
            R(Key("c-a")),

        "find":
            R(Key("c-f")),

		"<sidepunc>":
			R(Key("%(sidepunc)s")),		

		# "slap":
		# 	R(Key("c-enter")),
        # "hello world": R(Text("hello <?> world")),
        # "test hello world": R(Text("blargh ishello <?> world")),

	}
	extras = [
        IntegerRefST("n", 1, 10),
		personal.get_choice(),
        Dictation("textnv"),
		Choice("sidepunc", {
			"left paren": "lparen",
			"right paren": "rparen",
			"left bracket": "lbracket",
			"right bracket": "rbracket",
			"left brace": "lbrace",
			"right brace": "rbrace",
			}),
        Choice("capitalization", {
            "yell": 1,
            "tie": 2,
            "(Gerrish | camel)": 3,
            "sing": 4,
            "laws": 5
        }),
        Choice(
            "spacing", {
                "gum": 1,
                "gun": 1,
                "spine": 2,
                "snake": 3,
                "pebble": 4,
                "incline": 5,
                "dissent": 6,
                "descent": 6,
                "list": 7,
                "dictionary": 8,
            }),

		]
	defaults = {
        "n": 1,
    }

control.nexus().merger.add_global_rule(Mine())