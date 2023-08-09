FILEPATH = "todos.txt"#將常用可能會改變的Setting設置變數

#建立新function取代冗餘代碼,注意local跟global變量,有時避免用同一名稱
def get_todos(filepath=FILEPATH):#新增argument filepath,給他一個常用的default
    """ Read a text file and return the list of
    to do item
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath = FILEPATH):#2個argument注意順序
    """
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
#print(help(write_todos)) 有doc string就可call help看Function的意義,建議function都加一下

print(__name__)#當在main執行這個會print functions,如果在這個檔案執行會得到__main__,那下方判斷式將執行
#用於control那些該執行,或者加入判斷式
if __name__ == "__main__":
    print("hello")