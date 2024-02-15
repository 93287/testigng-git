import os

print("Python File Remover")

path = input("Input the directory: ")
os.chdir(path)

wtd = input("Do you wish to delete files, folders or both?\n(files/folders/both): ")

if wtd == "files":
    for x in os.listdir(path):
        if os.path.isfile(os.path.join(path, x)):
            print(x)
            exp = input("Do you wish to not delete one of those files\n(y/n): ")

            if exp == "y":
                filexp = input("input the file's name: ")
                jfilexp = path+"/"+filexp #can be removed
                os.mkdir("savedfiles")
                ndf = path+"/savedfiles" #can be removed
                os.system("mv "+filexp+" savedfiles")
                files = [f for f in os.listdir(path) if os.path.isfile(f)] #https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
                for f in files:        
                    os.remove(f)
                    print(f+" has been removed.")

            elif exp == "n":
                files = [f for f in os.listdir(path) if os.path.isfile(f)]
                for f in files:        
                    os.remove(f)

elif wtd == "folders":
    for x in os.listdir(path):
        if os.path.isdir(os.path.join(path, x)):
            print(x+" (folder)")
            exp = input("Do you wish to not delete one of those files\n(y/n): ")

            if exp == "y":
                filexp = input("input the file's name: ")
                jfilexp = path+"/"+filexp #can be removed
                os.mkdir("savedfiles")
                ndf = path+"/savedfiles" #can be removed
                os.system("mv "+filexp+" savedfiles")
                files = [f for f in os.listdir(path) if os.path.isfile(f)] #https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
                for f in files:        
                    os.remove(f)
                    print(f+" has been removed.")

            elif exp == "n":
                files = [f for f in os.listdir(path) if os.path.isfile(f)]
                for f in files:        
                    os.remove(f)

elif wtd == "both":
    for x in os.listdir(path):
        if os.path.isfile(os.path.join(path, x)):
            print(x)
        if os.path.isdir(os.path.join(path, x)):
            print(x+" (folder)")
        exp = input("Do you wish to not delete one of those files\n(y/n): ")

        if exp == "y":
            filexp = input("input the file's name: ")
            jfilexp = path+"/"+filexp #can be removed
            os.mkdir("savedfiles")
            ndf = path+"/savedfiles" #can be removed
            os.system("mv "+filexp+" savedfiles")
            files = [f for f in os.listdir(path) if os.path.isfile(f)] #https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
            for f in files:        
                os.remove(f)
                print(f+" has been removed.")

        elif exp == "n":
            files = [f for f in os.listdir(path) if os.path.isfile(f)]
            for f in files:        
                os.remove(f)

print("\nAll files removed.")
