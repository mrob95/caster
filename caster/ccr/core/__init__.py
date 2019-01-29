# new modulesThis is should be added in the dictionary
# the tupple contains the rules which will be imported


command_sets = {
    "alphabet": ("Alphabet", ),
    "nav": ("Navigation", ),
    "numbers": ("Numbers", ),
    "punctuation": ("Punctuation", ),
    "my_commands": ("Mine", ),
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
