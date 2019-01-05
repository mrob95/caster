# new modulesThis is should be added in the dictionary
# the tupple contains the rules which will be imported


command_sets = {
    # # "bash.bash": ("Bash", ),
    "core.alphabet": ("Alphabet", ),
    "core.nav": ("Navigation", ),
    "core.numbers": ("Numbers", ),
    "core.punctuation": ("Punctuation", ),
    "core.my_commands": ("Mine", ),
    "cpp.cpp": ("CPP", ),
    # "csharp.csharp": ("CSharp", ),
    "go.go": ("Go", ),
    # "haxe.haxe": ("Haxe", ),
    "html.html": ("HTML", ),
    # "java.java": ("Java", ),
    # "javascript.javascript": ("Javascript", ),
    "latex.latex": ("LaTeX", ),
    # "matlab.matlab": ("Matlab", ),
    "markdown.markdown":("Markdown", ),
    "python.python": ("Python", ),
    # "python.python_data":("PythonData", ),
    "r.r2": ("Rlang", ),
    # "rust.rust": ("Rust", ),
    "sql.sql": ("SQL", ),
    # "prolog.prolog": ("Prolog", ),
    # "vhdl.vhdl": ("VHDL", ),
    # "hearthstone.hearthstone": ("Hearthstone", ),
    "mathematics.mathematics": ("mathematics", ),
}

# files_list = [f for f in os.listdir(os.getcwd()) if not (f.endswith('.py') or f.endswith('.pyc')) and not in ["__pycache__", "recording"]]
# print(files_list)

for module_name, class_name_tup in command_sets.iteritems():
    for class_name in class_name_tup:
        try:
            module = __import__(module_name, globals(), locals(),[class_name])    #attempts to import the class
            globals()[class_name]= module    #make the name available globally

        except Exception as e:
            print("Ignoring ccr rule '{}'. Failed to load with: ".format(class_name))
            print(e)
