from dragonfly import Key, Text, Dictation, MappingRule, Choice

from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule
from caster.lib.dfplus.state.short import R


class PythonData(MergeRule):
    pronunciation = "python data"

    mapping = {
        #pandas
        "import pandas":
            R(Text("import pandas as pd"), rdescript="Python: pandas"),
        "pandas <pdfun>":
            R(Text("pd.%(pdfun)s") + Key("left"), rdescript="Python: pandas"),
        "meth <pdmethod>":
            R(Text("%(pdmethod)s"), rdescript="Python: pandas"),
        "meth <pdmethodleft>":
            R(Text("%(pdmethodleft)s") + Key("left"), rdescript="Python: pandas"),

        #pyplot
        "import pie plot":
            R(Text("import matplotlib.pyplot as plt"), rdescript="Python: pyplot"),
        "plot <pltfun>":
            R(Text("plt.%(pltfun)s") + Key("left"), rdescript="Python: pyplot"),
        "meth <pltmethod>":
            R(Text("%(pltmethod)s")+ Key("left"), rdescript="Python: pyplot"),
    }

    extras = [
        Choice("pdfun", {
            "con cat":"concat()",
            "data frame":"DataFrame()",
            "melt":"melt()",
            "merge":"merge()",
            "read CSV":"read_csv()",
            "read excel":"read_excel()",
            "series":"Series()",
            "to date time":"to_datetime()",
            "to numeric":"to_numeric()",
            }),
        #methods which do not require an argument, or attributes
        Choice("pdmethod",{
            "all":"all()",
            "columns":"columns",
            "D types":"dtypes",
            "describe":"describe()",
            "drop duplicates":"drop_duplicates()",
            "drop NA":"dropna()",
            "head":"head()",
            "index":"index",
            "info":"info()",
            "reset index":"reset_index()",
            "not null":"notnull()",
            "shape":"shape",
            "tail":"tail()",
            "value counts":"value_counts()",
            }),
        #methods whimch do require an argument
        Choice("pdmethodleft",{
            "apply":"apply()",
            "assign":"assign()",
            "as type":"astype()",
            "con cat":"concat()",
            "count":"count()",
            "drop":"drop()",
            "fill NA":"fillna()",
            "filter":"filter()",
            "group by":"groupby()",
            "I lock":"iloc[]",
            "lock":"loc[]",
            "max":"max()",
            "mean":"mean()",
            "median":"median()",
            "melt":"melt()",
            "merge":"merge()",
            "min":"min()",
            "N largest":"nlargest()",
            "N smallest":"nsmallest()",
            "pivot":"pivot()",
            "pivot table":"pivot_table()",
            "Q cut":"qcut()",
            "quantile":"quantile()",
            "query":"query()",
            "rename":"rename()",
            "resample":"resample()",
            "rolling":"rolling()", 
            "sample":"sample()",
            "sort values":"sort_values()",
            "standard":"std()",
            "sum":"sum()",
            "to CSV":"to_csv()",
            "to excel":"to_excel()",
            }),
            Choice("pltfun", {
                "show":"show()",
                "title":"title()",
                "ex label":"xlabel()",
                "ex limit":"xlim()",
                "why label":"ylabel()",
                "why limit":"ylim()",
            }),
            Choice("pltmethod", {
                "plot":"plot()",
            }),

    ]
    defaults = {

    }

control.nexus().merger.add_global_rule(PythonData(ID=100))
