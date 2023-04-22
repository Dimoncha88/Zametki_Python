import datetime
import file_operation as f

def create_note():
    id = f.id_note()
    name = input('Введите название заметки: ')
    text = input('Введите текст заметки: ')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return (id, name, text, date)

def delete_note(arr):
    try:
        delete = input('ID заметки для удаления(если нет заметок, пропустите действие): ')
        for index,note in enumerate(arr):
            if (note[0] == delete):
                arr.pop(index)
                print('Заметка удалена')
        return(arr)  
    except Exception:
        pass      
                           
def edit_note(arr):
    try:
        edit = input('ID заметки для редактирования (если нет заметок, пропустите действие): ')
        for note in arr:
            if (note[0] == edit):
                print('Введите 1, если хотите изменить название')
                print('Введите 2, если хотите изменить текст')
                get = input()     
                if get == '1':     
                    name = input('Новое название: ')
                    note[1] = name 
                if get == '2':     
                    body = input('Новое текст заметки: ')
                    note[2] = body 
                print('Заметка отредактирована')             
        return(arr)
    except Exception:
        pass                     
                                
def show_notes(arr):
    try:
        for note in arr:
            print(f'ID: {note[0]}')
            print(f'Название заметки: {note[1]}')
            print(f'Текст заметки: {note[2]}')
            print(f'Дата создания: {note[3]}\n')
    except Exception:
        pass             
       
