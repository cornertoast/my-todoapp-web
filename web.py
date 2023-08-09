import streamlit
import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"]+"\n"#與input的key做連結
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()#實例化

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is a test")#text

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:#被勾選會變True
        todos.pop(index)#刪除value
        functions.write_todos(todos)#更新重寫的文本
        del st.session_state[todo]#刪除key
        st.experimental_rerun()#checkbox需要這個


st.text_input(label="Enter a to do",placeholder='Add new todo....',
              on_change=add_todo,key='new_todo')

#st.session_state#檢查用很重要