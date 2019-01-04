'''
Created on Sep 1, 2015

@author: synkarius
'''
from dragonfly import Mimic
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control
from caster.ccr.standard import SymbolSpecs
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R

def snip(key):
    return (Text(key) + Key("tab"))

class CPP(MergeRule):
    pronunciation = "C plus plus"

    mapping = {
        SymbolSpecs.IF:    R(snip("if")),
        SymbolSpecs.ELSE:      R(Key("e, l, s, e, leftbrace, enter")),
        SymbolSpecs.SWITCH:    R(Text("switch(){\ncase : break;\ndefault: break;") + Key("up,up,left,left")),
        SymbolSpecs.CASE:      R(Text("case :") + Key("left")),
        SymbolSpecs.BREAK:     R(Text("break;")),
        SymbolSpecs.DEFAULT:       R(Text("default: ")),
        SymbolSpecs.DO_LOOP:       R(snip("do")),
        SymbolSpecs.WHILE_LOOP:    R(Text("while ()") + Key("left")),
        SymbolSpecs.FOR_LOOP:      R(snip("for")),
        SymbolSpecs.FOR_EACH_LOOP:     R(Text("for_each (TOKEN, TOKEN, TOKEN);")),
        SymbolSpecs.TO_INTEGER:    R(Text("(int)")),
        SymbolSpecs.TO_FLOAT:      R(Text("(double)")),
        SymbolSpecs.TO_STRING:     R(Text("std::to_string()") + Key("left")),
        SymbolSpecs.AND:       R(Text(" && ")),
        SymbolSpecs.OR:    R(Text(" || ")),
        SymbolSpecs.NOT:       R(Text("!")),
        SymbolSpecs.SYSOUT:    R(Text("cout <<")),
        SymbolSpecs.IMPORT:    R(snip("inc")),
        SymbolSpecs.FUNCTION:      R(Text("TOKEN TOKEN(){}") + Key("left")),
        SymbolSpecs.CLASS:     R(snip("class")),
        SymbolSpecs.COMMENT:       R(Text("//")),
        SymbolSpecs.LONG_COMMENT:      R(Text("/**/") + Key("left, left")),
        SymbolSpecs.NULL:      R(Text("null")),
        SymbolSpecs.RETURN:    R(Text("return ")),
        SymbolSpecs.TRUE:      R(Text("true")),
        SymbolSpecs.FALSE:     R(Text("false")),

        # C++ specific
        "main":     R(snip("main")),
        "public":      R(Text("public "), rdescript="C++: Public"),
        "private":     R(Text("private "), rdescript="C++: Private"),
        "static":      R(Text("static "), rdescript="C++: Static"),
        "final":       R(Text("final "), rdescript="C++: Final"),
        "static cast integer":     R(Text("static_cast<int>()") + Key("left"),
              rdescript="C++: Static Cast Integer"),
        "static cast double":      R(Text("static_cast<double>()") + Key("left"),
              rdescript="C++: Static Cast Double"),
        "([global] scope | name)":     R(Text("::"), rdescript="C++: ::"),
        "Vic":     R(Text("vector"), rdescript="C++: Vector"),
        "pushback":    R(Text("push_back"), rdescript="C++: Pushback"),
        "standard":    R(Text("std"), rdescript="C++: Standard"),
        "constant":    R(Text("const"), rdescript="C++: Constant"),
        "array":       R(Mimic("brackets"), rdescript="C++: Array"),

        "assign ross": R(Text(" >> ")),
        "assign lease": R(Text(" << ")),

        #http://www.learncpp.com/cpp-tutorial/67-introduction-to-pointers/
        "(reference to | address of)":     R(Text("&"), rdescript="C++: Reference"),
        "member":      R(Text("->"), rdescript="C++: Member"),
        "new new":     R(Text("new "), rdescript="C++: New"),
        "(integer | inter)":     R(Text("int "), rdescript="C++: Integer"),
        "double":      R(Text("double "), rdescript="C++: Double"),
        "character":       R(Text("char "), rdescript="C++: Character"),
        "big integer":     R(Text("Integer"), rdescript="C++: Big Integer"),
        "string":      R(Text("string "), rdescript="C++: String"),
        "ternary":     R(Text("()?;") + (Key("left")*3), rdescript="C++: Ternary"),
    }

    extras = []
    defaults = {}


# SymbolSpecs.IF:    R(Key("i, f, lparen, rparen, leftbrace, enter,up,left"), rdescript="C++: If"),
#         SymbolSpecs.ELSE:      R(Key("e, l, s, e, leftbrace, enter"), rdescript="C++: Else"),
#         SymbolSpecs.SWITCH:    R(Text("switch(){\ncase : break;\ndefault: break;") + Key("up,up,left,left"),
#               rdescript="C++: Switch"),
#         SymbolSpecs.CASE:      R(Text("case :") + Key("left"), rdescript="C++: Case"),
#         SymbolSpecs.BREAK:     R(Text("break;"), rdescript="C++: Break"),
#         SymbolSpecs.DEFAULT:       R(Text("default: "), rdescript="C++: Default"),
#         SymbolSpecs.DO_LOOP:       R(Text("do {}") + Key("left, enter:2"), rdescript="C++: Do Loop"),
#         SymbolSpecs.WHILE_LOOP:    R(Text("while ()") + Key("left"), rdescript="C++: While"),
#         SymbolSpecs.FOR_LOOP:      R(Text("for (int i=0; i<TOKEN; i++)"), rdescript="C++: For i Loop"),
#         SymbolSpecs.FOR_EACH_LOOP:     R(Text("for_each (TOKEN, TOKEN, TOKEN);"), rdescript="C++: For Each Loop"),
#         SymbolSpecs.TO_INTEGER:    R(Text("(int)"), rdescript="C++: Convert To Integer"),
#         SymbolSpecs.TO_FLOAT:      R(Text("(double)"), rdescript="C++: Convert To Floating-Point"),
#         SymbolSpecs.TO_STRING:     R(Text("std::to_string()") + Key("left"), rdescript="C++: Convert To String"),
#         SymbolSpecs.AND:       R(Text("&&"), rdescript="C++: And"),
#         SymbolSpecs.OR:    R(Text("||"), rdescript="C++: Or"),
#         SymbolSpecs.NOT:       R(Text("!"), rdescript="Not"),
#         SymbolSpecs.SYSOUT:    R(Text("cout <<"), rdescript="C++: Print"),
#         SymbolSpecs.IMPORT:    R(Text("#include "), rdescript="C++: Import"),
#         SymbolSpecs.FUNCTION:      R(Text("TOKEN TOKEN(){}") + Key("left"), rdescript="C++: Function"),
#         SymbolSpecs.CLASS:     R(Text("class TOKEN{}") + Key("left"), rdescript="C++: Class"),
#         SymbolSpecs.COMMENT:       R(Text("//"), rdescript="C++: Add Comment"),
#         SymbolSpecs.LONG_COMMENT:      R(Text("/**/") + Key("left, left"), rdescript="C++: Long Comment"),
#         SymbolSpecs.NULL:      R(Text("null"), rdescript="C++: Null Value"),
#         SymbolSpecs.RETURN:    R(Text("return "), rdescript="C++: Return"),
#         SymbolSpecs.TRUE:      R(Text("true"), rdescript="C++: True"),
#         SymbolSpecs.FALSE:     R(Text("false"), rdescript="C++: False"),


control.nexus().merger.add_global_rule(CPP())
