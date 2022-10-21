import os
from genericpath import isfile
def cd(cur_f_dir, file_n):
        try:
            n_path=os.path.join(cur_f_dir, file_n)
            if(not os.path.exists(n_path)):
                raise FileExistsError(f"cd: There is no {file_n} in {os.path.dirname(cur_f_dir)}")
            return n_path
        except FileExistsError:
            print(FileExistsError)

def pwd(cur_f_dir):
        print(cur_f_dir)

def touch(cur_f_dir, file_n):
        new_file=os.path.join(cur_f_dir, file_n)
        try:
            with open(new_file, 'w') as file:
                pass
        except OSError:
            print(OSError)

def cat(cur_f_dir, file_n):
        try:    
            with open(os.path.join(cur_f_dir, file_n), "r") as file:
                for line in file:
                    print(line[-1])
        except OSError:
            print(OSError)

def ls(cur_f_dir):
        files = [f for f in os.listdir(cur_f_dir) if isfile(os.path.join(cur_f_dir, f))]
        for i in files:
            print("--"+i)

def rm(cur_f_dir, file_n):
        if (isfile(os.path.join(cur_f_dir, file_n))):
            os.remove(os.path.join(cur_f_dir, file_n))
        else: print(f"There is not {file_n} file in this directory")
def main():
    cur_f=os.getcwd()
    while True:
        
        act, *file = input().split()
        if act == "cd":
            cur_f = cd(cur_f, *file)

        elif act == "cat":
            cat(cur_f, *file)
        elif act == "ls":
            ls(cur_f)
        elif act == "pwd":
            pwd(cur_f)
        elif act == "rm":
            rm(cur_f, *file)
        elif act == "touch":
            touch(cur_f, *file)
if __name__=="__main__":
    main()

