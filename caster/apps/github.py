from dragonfly import (Grammar, Repeat, Choice)
from caster.lib.actions import Key, Text
from caster.lib.context import AppContext

from caster.lib import control
from caster.lib import settings
from caster.lib.dfplus.additions import IntegerRefST
from caster.lib.dfplus.merge import gfilter
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

class GitHubRule(MergeRule):
    pronunciation = "github"

    mapping = {
            "new repository": R(Key("c-n")),
            "add local repository": R(Key("c-o")),
            "clone repository": R(Key("c-o")),
            "options": R(Key("c-comma")),
            
            "changes": R(Key("c-1")),
            "history": R(Key("c-2")),
            "(repositories | repository list)": R(Key("c-t")),
            "branches [list]": R(Key("c-b")),
            
            "zoom in [<n>]": R(Key("c-equals"))*Repeat(extra="n"),
            "zoom out [<n>]": R(Key("c-minus"))*Repeat(extra="n"),
            "reset zoom": R(Key("c-0")),
            
            "push [repository]": R(Key("c-p")),
            "pull [repository]": R(Key("cs-p")),
            "remove repository": R(Key("c-delete")),
            "view on github": R(Key("cs-g")),
            "(terminal | command prompt)": R(Key("c-backtick")),
            "explorer": R(Key("cs-f")),
            "edit": R(Key("cs-a")),

            "new branch": R(Key("cs-n")),
            "rename branch": R(Key("cs-r")),
            "delete branch": R(Key("cs-d")),

            "update from master": R(Key("cs-u")),
            "compare to [branch]": R(Key("cs-b")),
            "merge into current [branch]": R(Key("cs-m")),
            
            "compare on github": R(Key("cs-c")),
            "create pull request": R(Key("c-r")),
        }
    extras = [
        IntegerRefST("n", 1, 10),

    ]
    defaults = {"n": 1}


#---------------------------------------------------------------------------

context = AppContext(executable="GitHubDesktop")
grammar = Grammar("GitHubDesktop", context=context)

if settings.SETTINGS["apps"]["github"]:
    if settings.SETTINGS["miscellaneous"]["rdp_mode"]:
        control.nexus().merger.add_global_rule(GitHubRule())
    else:
        rule = GitHubRule(name="GitHubDesktop")
        gfilter.run_on(rule)
        grammar.add_rule(rule)
        grammar.load()
