'''
~ Desktop Cleaner ~

1. What should this program do?
    This program should automatically sort the files on your Desktop into predetermined folders.
2. How will it achieve this?
    To start, we will create folders for a defined list of file extensions. Then we will loop through the
    files on our desktop and put them into their designated folder.
3. How can we expand on this?
    * Add a GUI 
    * Allow for folders to be sorted as well as files
    * Create custom sorting conditions beyond file extensions

'''
import shutil
import os

def start_cleanup(path_to_source, rules):
    # For each rule in rules, loop through files in source (path_to_source) and check for name or extension match
    source_files = os.listdir(path_to_source)
    for file in source_files:
        split_file = file.split(".")

        for dest in rules:
            if path_to_source+"/"+file != dest: # Skip destination folder in case it matches the name filter
                if rules[dest]['names'][0] != '': # Empty names
                    for name in rules[dest]['names']:
                        if name in split_file[0]:
                            shutil.move(path_to_source+"/"+file, dest)
                            continue
                if len(split_file) > 1: # This is a file, check for extension match
                    if "."+split_file[1] in rules[dest]['extensions']:
                        shutil.move(path_to_source+"/"+file, dest)
    
def main():
    rules = {}
    done_with_rules = False
    done_with_extensions = False
    done_with_names = False
    done_with_dest_path = False
    print("Welcome to File Cleanup!")

    # Retrieve source folder
    source_path_valid = False
    path_to_source = input("What folder would you like to cleanup? Ex: C:/Users/<username>/Desktop \n")
    # Validate / create source folder
    while not source_path_valid:
        if not os.path.exists(path_to_source):
            create_source = input("Folder doesn't exist, would you like to create it? (Y/N)")
            if create_source.lower() == 'y':    
                try:
                    os.makedirs(path_to_source)
                except OSError:
                    path_to_source = input("Please enter a valid directory.\n")
                else:
                    source_path_valid = True
            else:
                exit()
        else:
            source_path_valid = True

    # Create rules to filter by
    while not done_with_rules:
        print("Rule #" + str(len(rules)+1)+ ":")

        # Retrieve / verify destination folder for this rule
        rule_dest = input("What folder would you like these files put into?\n")
        while not done_with_dest_path:
            if not os.path.isdir(rule_dest):
                rule_dest = input("Please enter a valid directory.\n")
            elif rule_dest == path_to_source: # Destination folder cannot be same as source folder
                rule_dest = input("Destination folder cannot equal the source folder.\n")
            else:
                done_with_dest_path = True


        # Initialize item for this rule
        rules[rule_dest] = {}
        rules[rule_dest]['extensions'] = []
        rules[rule_dest]['names'] = [] 

        # Retrieve extensions for this rule
        while not done_with_extensions:
            temp_extensions = input("What file extensions do you want to be put into this folder? Enter as comma separated list. Ex: .jpg, .png \n")
            temp_extensions = temp_extensions.replace(" ", "") # Remove whitespace in str
            temp_extensions = temp_extensions.split(',')
            rules[rule_dest]['extensions'] = temp_extensions

            num_extensions = len(rules[rule_dest]['extensions'])
            if num_extensions > 1 or (num_extensions == 1 and rules[rule_dest]['extensions'][0] != ""): #Non-empty list of extensions to  confirm
                print("Confirm the following ", end="")
                if num_extensions > 1: 
                    print (str(num_extensions)+" extensions:")
                else:
                    print("extension:")
            
                for i in range(num_extensions):
                    print("#" + str(i+1) + ": " + rules[rule_dest]['extensions'][i])
                confirm_exts_input = input("Continue with these extensions? (Y/N)")
            else: # Empty list of extensions to confirm
                confirm_exts_input = input("Continue with no extensions? (Y/N)")
            if confirm_exts_input.lower() == "y":
                done_with_extensions = True
            else:
                done_with_extensions = False

        # Retrieve names for this rule
        while not done_with_names:
            temp_names = input("What file names do you want to be put into this folder? Enter as comma separated  list. Ex: Screenshots, 062425\n")
            temp_names = temp_names.replace(" ", "") # Remove whitespace in str
            temp_names = temp_names.split(',')
            rules[rule_dest]['names'] = temp_names # 

            num_names = len(rules[rule_dest]['names'])
            if num_names > 1 or (num_names == 1 and rules[rule_dest]['names'][0] != ""): # Non-empty list of names to  confirm
                print("Confirm the following ", end="")
                if num_names > 1: 
                    print (str(num_names)+" names:")
                else:
                    print("name:")
                for i in range(num_names):
                    print("#" + str(i+1) + ": " + rules[rule_dest]['names'][i])
                    confirm_names_input = input("Continue with these names? (Y/N)")
            else: # Empty list of names to confirm
                confirm_names_input = input("Continue with no names? (Y/N)")
            
            
            if confirm_names_input.lower() == "y":
                done_with_names = True
            else:
                done_with_names = False

        # Loop again if we want to create another rule
        more_rules = input("Would you like to create another Rule? (Y/N)")
        if more_rules.lower() == "n":
            done_with_rules = True
    
    # Once all rules are create, display them so user can confirm before starting
    print("\nYour cleanup rules:")
    print("--------------------\n")
    rule_counter = 1
    for dest in rules:
        print("Rule #"  + str(rule_counter) +":")
        print("Destination folder: " + dest)
        print("Extensions: ", end="")
        if (rules[dest]['extensions'][0] == ""):
            print("No extensions", end="")
        else:
            for ext in rules[dest]['extensions']:
                print(ext.strip(), end=' ')
        print("\nNames: ", end="")
        if (rules[dest]['names'][0] == ""):
            print("No names", end="")
        else:
            for name in rules[dest]['names']:
                print(name.strip(), end=' ')
        rule_counter += 1
        print("\n")
    start_cleanup_input = input("\nStart cleanup with these rules? (Y/N)")
    if start_cleanup_input.lower() == "y":
        print("Start cleanup")
        start_cleanup(path_to_source, rules)
    elif start_cleanup_input.lower() == "n":
        print("Do not start cleanup")
    
if __name__ == "__main__":
    main() 