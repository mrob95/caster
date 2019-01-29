'''
Created on , 2018

@author: Mike Roberts
'''

from dragonfly import Choice
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R
from caster.ccr.standard import SymbolSpecs


def snip(key):
    return (Text(key) + Key("tab"))


class Go(MergeRule):

    mapping = {
        SymbolSpecs.IF:
            R(snip("if")),
        SymbolSpecs.ELSE:
            R(Text("else {}") + Key("left, enter"), rdescript="Go: else"),
        #
        SymbolSpecs.SWITCH:
            R(Text("switch  {}") + Key("left, enter, up, end, left:2"),
              rdescript="Go: switch"),
        SymbolSpecs.CASE:
            R(Text("case :") + Key("left"), rdescript="Go: case"),
        SymbolSpecs.DEFAULT:
            R(Text("default:") + Key("enter"), rdescript="Go: default"),
        SymbolSpecs.BREAK:
            R(Text("break"), rdescript="Go: break"),
        #
        SymbolSpecs.WHILE_LOOP:
            R(Text("for  {}") + Key("left, enter, up, end, left:2"),
              rdescript="Go: while loop"),
        SymbolSpecs.FOR_LOOP:
            R(snip("for"), rdescript="Go: for loop"),
        SymbolSpecs.FOR_EACH_LOOP:
            R(Text("for  := range  {}") + Key("left, enter, up, home, right:4"),
              rdescript="Go: for each"),
        #
        SymbolSpecs.TO_INTEGER:
            R(Text("strconv.Atoi()") + Key("left"), rdescript="Go: convert to integer"),
        SymbolSpecs.TO_STRING:
            R(Text("strconv.Itoa()") + Key("left"), rdescript="Go: convert to string"),
        #
        SymbolSpecs.AND:
            R(Text(" && "), rdescript="Go: and"),
        SymbolSpecs.OR:
            R(Text(" || "), rdescript="Go: or"),
        SymbolSpecs.NOT:
            R(Text("!"), rdescript="Go: not"),
        #
        SymbolSpecs.SYSOUT:
            R(Text("fmt.Println()") + Key("left"), rdescript="Go: sysout"),
        #
        SymbolSpecs.IMPORT:
            R(Text("import ()") + Key("left, enter"), rdescript="Go: import"),
        #
        SymbolSpecs.FUNCTION:
            R(snip("func"), rdescript="Go: function"),
        "(" + SymbolSpecs.CLASS  + " | type struct)":
            R(Text("type  struct {}") + Key("left, enter, up, home, right:5"),
              rdescript="Go: class"),
        #
        SymbolSpecs.COMMENT:
            R(Text("//"), rdescript="Go: comment"),
        SymbolSpecs.LONG_COMMENT:
            R(Text("/**/") + Key("left, left"), rdescript="Go: long comment"),
        #
        SymbolSpecs.NULL:
            R(Text("nil"), rdescript="Go: nil"),
        #
        SymbolSpecs.RETURN:
            R(Text("return "), rdescript="Go: return"),
        #
        SymbolSpecs.TRUE:
            R(Text("true"), rdescript="Go: true"),
        SymbolSpecs.FALSE:
            R(Text("false"), rdescript="Go: false"),
        #
        "type (inter | integer) [<bn>]":
            R(Text("int" + "%(bn)s"), rdescript="Go: integer"),
        "type unsigned [<bn>]":
            R(Text("uint" + "%(bn)s"), rdescript="Go: integer"),

        "type boolean":
            R(Text("bool"), rdescript="Go: boolean"),
        "type string":
            R(Text("string"), rdescript="Go: string"),
        "type rune":
            R(Text("rune"), rdescript="Go: rune"),
        "type byte":
            R(Text("byte"), rdescript="Go: byte"),
        "type interface":
            R(Text("interface"), rdescript="Go: interface"),
        "type float":
            R(Text("float64"), rdescript="Go: float64"),

        "assign":
            R(Text(" := "), rdescript="Go: assign"),
        "(function | funk) main":
            R(Text("func main() {}") + Key("left, enter"), rdescript="Go: main function"),
        "make map":
            R(Text("make(map[])") + Key("left:2"), rdescript="Go: create a map"),
        "make channel":
            R(Text("make(chan )") + Key("left"), rdescript="Go: create a map"),
        "package":
            R(Text("package "), rdescript="Go: package"),
        "package main":
            R(Text("package main") + Key("enter"), rdescript="Go: package"),
        "variable":
            R(Text("var "), rdescript="Go: variable"),
        "go routine":
            R(Text("go ")),
        "create mutex":
            R(Text("var mutex = sync.Mutex{}")),
        "mutex lock":
            R(Text("mutex.Lock()")),
        "mutex unlock":
            R(Text("mutex.Unlock()")),
        "create weight group":
            R(Text("var wg sync.WaitGroup")),
        "weight group add":
            R(Text("wg.Add(1)")),
        "weight group done":
            R(Text("wg.Done()")),
        "weight group weight":
            R(Text("wg.Wait()")),
        "(start | begin) timer":
            R(Text("start := time.Now()")),
        "(end | finish) timer":
            R(Text("elapsed := time.Since(start)\nfmt.Printf(") + Key("dquote") +
                Text("execution took ") + Key("percent, s, dquote") + Text(", elapsed)")),
        "send (message | channel)":
            R(Text(" <- ")),
        "append":
            R(Key("home/5, s-end, c-c, right, space, equal, space, a, p, p, e, n, d, lparen, c-v, comma, space")),

        "regular compile":
            R(Text("regexp.MustCompile()") + Key("left, dquote")),
        "regular find all [string]":
            R(Text("FindAllString(, -1)") + Key("left:5")),
        "regular find all [string] submatch":
            R(Text("FindAllStringSubmatch(, -1)") + Key("left:5")),

        "read file":
            R(Text("ioutil.ReadFile()") + Key("left, dquote")),

        "(split string | strings split)":
            R(Text("strings.Split()") + Key("left")),

        "file open":
            R(Text("file, _ := os.Open()\ndefer file.Close()") + Key("up, end, left, dquote")), 

        "scanner new":
            R(Text("scanner := bufio.NewScanner(file)")),
        "scanner scan":
            R(Text("scanner.Scan()")),
        "scanner text":
            R(Text("scanner.Text()")),
        

    }

    # mapping = {
    #     SymbolSpecs.IF:
    #         R(Text("if  {}") + Key("left, enter, up, end, left:2"), rdescript="Go: if"),
    #     SymbolSpecs.ELSE:
    #         R(Text("else {}") + Key("left, enter"), rdescript="Go: else"),
    #     #
    #     SymbolSpecs.SWITCH:
    #         R(Text("switch  {}") + Key("left, enter, up, end, left:2"), rdescript="Go: switch"),
    #     SymbolSpecs.CASE:
    #         R(Text("case :") + Key("left"), rdescript="Go: case"),
    #     SymbolSpecs.DEFAULT:
    #         R(Text("default:") + Key("enter"), rdescript="Go: default"),
    #     SymbolSpecs.BREAK:
    #         R(Text("break"), rdescript="Go: break"),
    #     #
    #     SymbolSpecs.WHILE_LOOP:
    #         R(Text("for  {}") + Key("left, enter, up, end, left:2"), rdescript="Go: while loop"),
    #     SymbolSpecs.FOR_LOOP:
    #         R(Text("for i := 0; i<; i++ {}") + Key("left, enter, up, end, left:7"),
    #           rdescript="Go: for loop"),
    #     SymbolSpecs.FOR_EACH_LOOP:
    #         R(Text("for  := range  {}") + Key("left, enter, up, home, right:4"),
    #           rdescript="Go: for each"),
    #     #
    #     SymbolSpecs.TO_INTEGER:
    #         R(Text("strconv.Atoi()") + Key("left"), rdescript="Go: convert to integer"),
    #     SymbolSpecs.TO_STRING:
    #         R(Text("strconv.Itoa()") + Key("left"), rdescript="Go: convert to string"),
    #     #
    #     SymbolSpecs.AND:
    #         R(Text(" && "), rdescript="Go: and"),
    #     SymbolSpecs.OR:
    #         R(Text(" || "), rdescript="Go: or"),
    #     SymbolSpecs.NOT:
    #         R(Text("!"), rdescript="Go: not"),
    #     #
    #     SymbolSpecs.SYSOUT:
    #         R(Text("fmt.Println()") + Key("left"), rdescript="Go: sysout"),
    #     #
    #     SymbolSpecs.IMPORT:
    #         R(Text("import ()") + Key("left, enter"), rdescript="Go: import"),
    #     #
    #     SymbolSpecs.FUNCTION:
    #         R(Text("func "), rdescript="Go: function"),
    #     SymbolSpecs.CLASS:
    #         R(Text("type  struct {}") + Key("left, enter, up, home, right:5"),
    #           rdescript="Go: class"),
    #     #
    #     SymbolSpecs.COMMENT:
    #         R(Text("//"), rdescript="Go: comment"),
    #     SymbolSpecs.LONG_COMMENT:
    #         R(Text("/**/") + Key("left, left"), rdescript="Go: long comment"),
    #     #
    #     SymbolSpecs.NULL:
    #         R(Text("nil"), rdescript="Go: nil"),
    #     #
    #     SymbolSpecs.RETURN:
    #         R(Text("return "), rdescript="Go: return"),
    #     #
    #     SymbolSpecs.TRUE:
    #         R(Text("true"), rdescript="Go: true"),
    #     SymbolSpecs.FALSE:
    #         R(Text("false"), rdescript="Go: false"),
    #     "[type] (inter | integer)":
    #         R(Text("int"), rdescript="Go: integer"),
    #     "[type] boolean":
    #         R(Text("bool"), rdescript="Go: boolean"),
    #     "[type] string":
    #         R(Text("string"), rdescript="Go: string"),
    #     "assign":
    #         R(Text(" := "), rdescript="Go: assign"),
    #     "(function | funk) main":
    #         R(Text("func main() {}") + Key("left, enter"), rdescript="Go: main function"),
    #     "make map":
    #         R(Text("make(map[])") + Key("left:2"), rdescript="Go: create a map"),
    #     "package":
    #         R(Text("package "), rdescript="Go: package"),
    #     "variable":
    #         R(Text("var "), rdescript="Go: variable"),
    # }

    extras = [
        Choice("bn", {
            "eight": "8",
            "sixteen": "16",
            "thirty two": "32",
            "sixty four": "64",
            }),
    ]

    defaults = {
    "bn": ""
    }
    


control.nexus().merger.add_global_rule(Go())
