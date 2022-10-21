def get_arguments():
    f_num=int(input())
    s_num=int(input())
    oper=input()
    return f_num, oper, s_num
def update_hist(hist:dict, key:str, eq:str):
    hist[key].append(eq)

def h_print(hist:dict):
    for oper, op_hist in hist.items():
        print(oper, op_hist)
hist={
        '+': [],
        '-': [],
        '/': [],
        '*': []
    }
def count_n_hist(hist:dict, args:list):
    res=f"{args[0]}{args[1]}{args[2]}"
    res+="="+str(eval(res))
    update_hist(hist, args[1], res)
    print(res)
    h_print(hist)

def main():
    while True:
        args = get_arguments()
        count_n_hist(hist, args)

if __name__=="__main__":
    main()


    

    
