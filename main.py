# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок,
# редактировать заметку, удалять заметку.

import file_operation as f
import notes_operation as n_op

def menu():
    while True:
        print('Выберите действие: ')
        print('1 - создать новую заметку')
        print('2 - посмотреть заметки')
        print('3 - редактировать заметку')
        print('4 - удалить заметку')

        get = input('Введите действие: ')
        if get == '':
            break
        elif get == '1':
            data = n_op.create_note()
            f.write(data)
            input('Заметка создана, нажмите Enter для продолжения')
        elif get == '2':
            get_notes = f.get_notes_from_file()
            n_op.show_notes(get_notes)
            input('Намите Enter для продолжения')
        elif get == '3':
            get_notes = f.get_notes_from_file()
            edit = n_op.edit_note(get_notes)
            f.rewrite(edit)
            input('Нажмите Enter для продолжения')
        elif get == '4':
            get_notes = f.get_notes_from_file()
            delete = n_op.delete_note(get_notes)
            f.rewrite(delete)
            input('Нажмите Enter для продолжения')

menu()

