
# Запуск LibreOffice в фоновом режиме через консоль
terminal = "soffice --accept='socket,host=localhost,port=2002;urp;' --norestore --nologo --nodefault --headless"

# проверка наличия процесса
terminal = "ps -ao args | grep soffice"



# путь к шаблону файла в который нужно вносить данные
url_file = "/home/user/office-script/"

# имя шаблона файла с расширением
name_input_file = "orders.xlsx"

# имя после сохранения файла
name_output_file = "order"

# набор даных которые нужно внести в таблицу
#   {'ключ': 'значение',}
data_input = {
    "B3": "Костенко",
    "B4": "Александр",
    "B5": "Одесса",
    "B6": "+380970850675",
    "B7": "kostencko.alexander2012@gmail.com",
            }

# формат в который нужно конвертировать
type_convert = 'pdf'

