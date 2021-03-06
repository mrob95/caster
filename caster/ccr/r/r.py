'''
Created on May 23, 2017

@author: shippy
'''

from dragonfly import Dictation, MappingRule, Choice
from caster.lib.actions import Key, Text, Mouse

from caster.lib import control
from caster.ccr.standard import SymbolSpecs
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class Rlang(MergeRule):
    auto = [".R", ".r"]
    pronunciation = "are"

    mapping = {
        SymbolSpecs.IF:
            R(Text("if ()") + Key("left"), rdescript="Rlang: If"),
        SymbolSpecs.ELSE:
            R(Text("else ") + Key("enter"), rdescript="Rlang: Else"),
        #
        # (no switch in Rlang)
        SymbolSpecs.BREAK:
            R(Text("break"), rdescript="Rlang: Break"),
        #
        SymbolSpecs.FOR_EACH_LOOP:
            R(Text("for ( in ):") + Key("left:6"), rdescript="Rlang: For Each Loop"),
        SymbolSpecs.FOR_LOOP:
            R(Text("for (i in 1:)") + Key("left"), rdescript="Rlang: For i Loop"),
        SymbolSpecs.WHILE_LOOP:
            R(Text("while ()") + Key("left"), rdescript="Rlang: While"),
        # (no do-while in Rlang)
        #
        SymbolSpecs.AND:
            R(Text(" && "), rdescript="Rlang: And"),
        SymbolSpecs.OR:
            R(Text(" || "), rdescript="Rlang: Or"),
        SymbolSpecs.NOT:
            R(Text("!"), rdescript="Rlang: Not"),
        #
        SymbolSpecs.SYSOUT:
            R(Text("print()") + Key("left"), rdescript="Rlang: Print"),
        #
        SymbolSpecs.FUNCTION:
            R(Text("function()") + Key("left"), rdescript="Rlang: Function"),
        # SymbolSpecs.CLASS:          R(Text("setClass()") + Key("left"), rdescript="Rlang: Class"),
        #
        SymbolSpecs.COMMENT:
            R(Text("#"), rdescript="Rlang: Add Comment"),
        #
        SymbolSpecs.NULL:
            R(Text("NULL"), rdescript="Rlang: Null"),
        #
        SymbolSpecs.RETURN:
            R(Text("return()") + Key("left"), rdescript="Rlang: Return"),
        #
        SymbolSpecs.TRUE:
            R(Text("TRUE"), rdescript="Rlang: True"),
        SymbolSpecs.FALSE:
            R(Text("FALSE"), rdescript="Rlang: False"),

        # Rlang specific
        "assign":
            R(Text(" <- "), rdescript="Rlang: Assignment"),
        "(contained | percent) in":
            R(Key('space, percent, i, n, percent, space'),
              rdescript="Rlang: In operator"),
        "chain":
            R(Key('space, percent, rangle, percent, space'), rdescript="Rlang: Pipe"),
        "tell chain":
            R(Key('end, space, percent, rangle, percent, enter'),
              rdescript="Rlang: Pipe at end"),
        "tell add":
            R(Key('end, space, plus, enter'), rdescript="Rlang: plus at end"),
        "NA":
            R(Text("NA"), rdescript="Rlang: Not Available"),
        "shell iffae | LFA":
            R(Text("elseif ()") + Key("left"), rdescript="Rlang: Else If"),
        "dot (our|are)":
            R(Text(".R"), rdescript="Rlang: .py"),

        # dplyr and tidyr keywords: https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf
        "tidy verse":
            R(Text("tidyverse"), rdescript="Rlang: tidyverse"),
        #
        "fun <function>":
            R(Text("%(function)s()") + Key("left"), rdescript="Rlang: insert a function"),
        #
        "graph <ggfun>":
            R(Text("%(ggfun)s()") + Key("left"),
              rdescript="Rlang: insert a ggplot function"),

        "model <modelargs>":
            R(Text("%(modelargs)s")),

        "meant <argument>":
            R(Text("%(argument)s")),
    }

    extras = [
        Dictation("text"),
        Choice(
            "function", {
                "arrange": "arrange",
                "as character": "as.character",
                "as data frame": "as.data.frame",
                "as double": "as.double",
                "as factor": "as.factor",
                "as numeric": "as.numeric",
                "bind rows": "bind_rows",
                "cable":"kable",
                "case when": "case_when",
                "count": "count",
                "drop NA": "drop_na",
                "everything":"everything",
                "filter": "filter",
                "full join": "full_join",
                "gather": "gather",
                "glimpse": "glimpse",
                "group by": "group_by",
                "head": "head",
                "if else":"ifelse",
                "inner join": "inner_join",
                "install packages":"install.packages",
                "is NA":"is.na",
                "left join": "left_join",
                "length": "length",
                "library": "library",
                "list": "list",
                "(LM | linear model)": "lm",
                "mean": "mean",
                "mutate": "mutate",
                "names": "names",
                "paste": "paste0",
                "read CSV": "read_csv",
                "read excel": "read_excel",
                "read RDS":"read_rds",
                "rename": "rename",
                "select": "select",
                "string contains": "str_contains",
                "string detect": "str_detect",
                "string replace": "str_replace",
                "string replace all": "str_replace_all",
                "starts with": "starts_with",
                "subset":"subset",
                "sum": "sum",
                "summarise": "summarise",
                "summary":"summary",
                "tail":"tail",
                "tibble":"tibble",
                "trim white space": "trimws",
                "type [of]":"typeof",
                "ungroup": "ungroup",
                "vector": "c",
                "view": "View",
                "write RDS":"write_rds",
            }),
        Choice(
            "ggfun", {
                "aesthetics": "aes",
                "column [plot]": "geom_col",
                "density [plot]": "geom_density",
                "ex limit": "xlim",
                "facet grid": "facet_grid",
                "facet wrap": "facet_wrap",
                "histogram [plot]": "geom_histogram",
                "labels": "labs",
                "line [plot]": "geom_line",
                "path [plot]": "geom_path",
                "[GG] plot": "ggplot",
                "point [plot]": "geom_point",
                "save": "ggsave",
                "smooth [plot]": "geom_smooth",
                "theme minimal": "theme_minimal",
                "why limit": "ylim",
            }),
        Choice(
            "argument", {
                "by":"by = ",
                "colour":"colour = ",
                "dodge":"\"dodge\"",
                "fill":"fill = ",
                "header":"header = ",
                "gather":"key = \"\",\nvalue = \"\",\n",
                "labels":"x = \"\",\ny = \"\",\ntitle = \"\",\nsubtitle = \"\",\ncaption = \"\"",
                "LM":"\"lm\"",
                "method":"method = ",
                "position":"position = ",
                "year":"year",
            }),
        Choice(
            "modelargs", {
                "chi square":"qchisq",
                "coefficients":"coefficients",
                "fixed effects":"plm(,\ndata=,\nindex=c(,),\nmodel = \"within\")",
                "fitted [values]":"fitted.values",
                "instrumental [variable]":"ivreg( ~  | ,\ndata = )",
                "libraries":"library(AER)\nlibrary(car)\nlibrary(stats)\nlibrary(DescTools)\nlibrary(plm)",
                "(linear | LM)": "lm(, data=)",
                "[(linear | test)] hypothesis [test]": "linearHypothesis(model = ,\nc(\" = 0\"),\ntest=c(\"F\", \"Chisq\"))",
                "(log it)":"glm(,\nfamily = binomial(link=\"logit\"),\ndata=)",
                "log likelihood":"logLik()",
                "normal":"pnorm(q = , mean = , sd = )",
                "pro bit":"glm(,\nfamily = binomial(link=\"probit\"),\ndata=)",
                "(pseudo | McFadden) R squared":"PseudoR2(, which=\"McFadden\")",
                "random effects":"plm(,\ndata=,\nindex=c(,),\nmodel = \"random\")",
                "residuals":"residuals",
            }),
    ]
    defaults = {}


control.nexus().merger.add_global_rule(Rlang())
