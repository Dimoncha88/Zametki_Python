
def id_note():
    with open('Zametki.csv', 'r') as file:
        id_temp = len(file.readlines())+1
        id = str(id_temp)
    return (id)

def get_notes_from_file():
    arr = []
    with open('Zametki.csv', 'r', encoding='utf-8') as file:
        notes = file.read().strip().split('\n')
        for note in notes:
            if notes == ['']:
                print('Заметок нет')
                break
            else:
                split_note = note.split(';')
                arr.append(split_note)
            
        return (arr )                                  

def write(arr):
    with open('Zametki.csv', '+a', encoding='utf-8') as file:
        i = 0
        while i < len(arr)-1:
            file.write(arr[i] + ';')
            i += 1
        file.write(arr[len(arr)-1])
        file.write('\n')

def rewrite(arr):
    try:
        with open('Zametki.csv', 'w', encoding='utf-8') as file:
            for item in arr:
                i = 0
                while i < len(item)-1:
                    file.write(item[i] + ';')
                    i += 1
                file.write(item[len(item)-1])
                file.write('\n')
    except Exception:
        pass     
        
