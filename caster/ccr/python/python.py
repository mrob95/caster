'''
Created on Sep 1, 2015

@author: synkarius
'''
from dragonfly import Dictation, MappingRule, Choice, Function
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control
from caster.ccr.standard import SymbolSpecs
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class PythonNon(MappingRule):
    mapping = {
        "try catch":
            R(Text("try:") + Key("enter:2/10, backspace") + Text("except Exception:") +
              Key("enter"),
              rdescript="Python: Try Catch"),
    }

def soup(soupfun):
    if type(soupfun) is str:
        Text(soupfun).execute()
    else:
        Text(soupfun[0]).execute()
        Key(soupfun[1]).execute()

class Python(MergeRule):
    non = PythonNon

    mapping = {
        SymbolSpecs.IF:
            R(Key("i,f,space,colon,left"), rdescript="Python: If"),
        SymbolSpecs.ELSE:
            R(Text("else:") + Key("enter"), rdescript="Python: Else"),
        # (no switch in Python)
        SymbolSpecs.BREAK:
            R(Text("break"), rdescript="Python: Break"),
        SymbolSpecs.FOR_EACH_LOOP:
            R(Text("for  in :") + Key("left:5"), rdescript="Python: For Each Loop"),
        SymbolSpecs.FOR_LOOP:
            R(Text("for i in range(0, ):") + Key("left:2"),
              rdescript="Python: For i Loop"),
        SymbolSpecs.WHILE_LOOP:
            R(Text("while :") + Key("left"), rdescript="Python: While"),
        # (no do-while in Python)
        SymbolSpecs.TO_INTEGER:
            R(Text("int()") + Key("left"), rdescript="Python: Convert To Integer"),
        SymbolSpecs.TO_FLOAT:
            R(Text("float()") + Key("left"),
              rdescript="Python: Convert To Floating-Point"),
        SymbolSpecs.TO_STRING:
            R(Text("str()") + Key("left"), rdescript="Python: Convert To String"),
        SymbolSpecs.AND:
            R(Text(" and "), rdescript="Python: And"),
        SymbolSpecs.OR:
            R(Text(" or "), rdescript="Python: Or"),
        SymbolSpecs.NOT:
            R(Text("!"), rdescript="Python: Not"),
        SymbolSpecs.SYSOUT:
            R(Text("print()") + Key("left"), rdescript="Python: Print"),
        SymbolSpecs.IMPORT:
            R(Text("import "), rdescript="Python: Import"),
        SymbolSpecs.FUNCTION:
            R(Text("def") + Key("tab"), rdescript="Python: Function"),
        SymbolSpecs.CLASS:
            R(Text("class "), rdescript="Python: Class"),
        SymbolSpecs.COMMENT:
            R(Text("#"), rdescript="Python: Add Comment"),
        SymbolSpecs.LONG_COMMENT:
            R(Text("''''''") + Key("left:3"), rdescript="Python: Long Comment"),
        SymbolSpecs.NULL:
            R(Text("None"), rdescript="Python: Null"),
        SymbolSpecs.RETURN:
            R(Text("return "), rdescript="Python: Return"),
        SymbolSpecs.TRUE:
            R(Text("True"), rdescript="Python: True"),
        SymbolSpecs.FALSE:
            R(Text("False"), rdescript="Python: False"),

        "with open":
            R(Text("with open() as f:") + Key("left:7"), rdescript="Python: With"),

        "assign":
            R(Text(" = ")),

        # Python specific
        "sue iffae":
            R(Text("if "), rdescript="Python: Short If"),
        "sue shells":
            R(Text("else "), rdescript="Python: Short Else"),
        "python from":
            R(Text("from "), rdescript="Python: From"),
        "python self":
            R(Text("self"), rdescript="Python: Self"),
        "lodge not":
            R(Text(" not "), rdescript="Python: Long Not"),
        "lodge in":
            R(Text(" in "), rdescript="Python: In"),  #supposed to sound like "iter in"
        "shell iffae | LFA":
            R(Key("e,l,i,f,space,colon,left"), rdescript="Python: Else If"),
        "convert to character":
            R(Text("chr()") + Key("left"), rdescript="Python: Convert To Character"),
        "length of":
            R(Text("len()") + Key("left"), rdescript="Python: Length"),
        "global":
            R(Text("global "), rdescript="Python: Global"),
        "make assertion":
            R(Text("assert "), rdescript="Python: Assert"),
        # "list comprehension":
        #     R(Text("[ for  in  if ]"),
        #       rdescript="Python: List Comprehension"),
        "list (comp | comprehension)":
            R(Key("l, c, tab")),
        "dot (pie | pi)":
            R(Text(".py"), rdescript="Python: .py"),
        "jason":
            R(Text("json"), rdescript="Python: json"),
        "identity is":
            R(Text(" is "), rdescript="Python: is"),
        "python yield":
            R(Text("yield "), rdescript="Python: Yield"),
        "lambda":
            R(Text("lambda ")),

        "fun <listmethod>":
            R(Text("%(listmethod)s()") + Key("left")),
        "fun <dictmethod>":
            R(Text("%(dictmethod)s()") + Key("left")),
        "fun <stringmethod>":
            R(Text("%(stringmethod)s()") + Key("left")),

        "fun <fun>":
            R(Text("%(fun)s()") + Key("left")),

        "soup <soupfun>":
            R(Function(soup, extra={"soupfun"})),
    }

    extras = [
        Dictation("text"),
        Choice("listmethod", {
            "append": "append",
            "clear": "clear",
            "copy": "copy",
            "count": "count",
            "extend": "extend",
            "index": "index",
            "insert": "insert",
            "pop": "pop",
            "remove": "remove",
            "reverse": "reverse",
            "sort": "sort",
        }),
        Choice("dictmethod", {
            "get": "get",
            "items": "items",
            "keys": "keys",
            "set default": "setdefault",
            "update": "update",
            "values": "values",
        }),
        Choice("stringmethod", {
            "strip": "strip",
            "replace": "replace",
        }),
        Choice("soupfun", {
            "beautiful [soup]": ("BeautifulSoup()", "left"),
            "find all": ("find_all(\"\")", "left:2"),
            "find": ("find(\"\")", "left:2"),
            "prettify": "prettify()",
        }),
        Choice("fun", {
            "execute": "execute",
            "(int | inter)": "int",
            "length": "len",
            "range": "range",
            "string": "str",
            "sum": "sum",
            "read lines": "readlines",
            "type": "type",
            }),
    ]

    defaults = {}


control.nexus().merger.add_global_rule(Python(ID=100))
