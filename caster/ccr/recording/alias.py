from dragonfly.actions.action_function import Function
from dragonfly import Dictation, Choice

from caster.lib.asynch.hmc import h_launch
from caster.lib import context, utilities, settings, textformat
from caster.lib import control
from caster.lib.actions import Text
from caster.lib.dfplus.merge.selfmodrule import SelfModifyingRule
from caster.lib.dfplus.state.actions import AsynchronousAction
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.state.actions2 import NullAction
from caster.lib.dfplus.state.short import R, L, S

_NEXUS = control.nexus()


def read_highlighted(max_tries):
    for i in range(0, max_tries):
        result = context.read_selected_without_altering_clipboard(True)
        if result[0] == 0: return result[1]
    return None


def delete_all(alias, path):
    aliases = utilities.load_toml_file(settings.SETTINGS["paths"]["ALIAS_PATH"])
    aliases[path] = {}
    utilities.save_toml_file(aliases, settings.SETTINGS["paths"]["ALIAS_PATH"])
    alias.refresh()


class Alias(SelfModifyingRule):
    mapping = {"default command": NullAction()}
    toml_path = "single_aliases"
    pronunciation = "alias"
    extras = [
        IntegerRefST("n", 1, 50), 
        Dictation("s"),
        Dictation("textnv"),
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
        "textnv": "",
        "capitalization": 0,
        "spacing": 0,
    }

    def alias(self, spec):
        spec = str(spec)
        if spec != "":
            text = read_highlighted(10)
            if text != None: self.refresh(spec, str(text))


    def vary(self, capitalization, spacing, textnv):
        textnv2 = textformat.TextFormat.formatted_text(capitalization, spacing, str(textnv))
        Text(textnv2).execute()
        self.refresh(str(textnv), textnv2)


    def refresh(self, *args):
        '''args: spec, text'''
        aliases = utilities.load_toml_file(settings.SETTINGS["paths"]["ALIAS_PATH"])
        if not Alias.toml_path in aliases:
            aliases[Alias.toml_path] = {}
        if len(args) > 0:
            aliases[Alias.toml_path][args[0]] = args[1]
            utilities.save_toml_file(aliases, settings.SETTINGS["paths"]["ALIAS_PATH"])
        mapping = {}
        for spec in aliases[Alias.toml_path]:
            mapping[spec] = R(
                Text(str(aliases[Alias.toml_path][spec])),
                rdescript="Alias: " + spec)
        mapping["alias <s>"] = R(
            Function(lambda s: self.alias(s)), rdescript="Create Alias")
        mapping["delete aliases"] = R(
            Function(lambda: delete_all(self, Alias.toml_path)),
            rdescript="Delete Aliases")
        mapping["vary (<capitalization> <spacing> | <capitalization> | <spacing>) (bow|bowel) <textnv>"] = R(
            Function(lambda capitalization, spacing, textnv: self.vary(capitalization, spacing, textnv)))
        self.reset(mapping)



if settings.SETTINGS["feature_rules"]["alias"]:
    control.nexus().merger.add_selfmodrule(Alias())
