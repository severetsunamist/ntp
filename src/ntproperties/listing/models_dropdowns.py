# FIRST VALUE OF EACH TUPLE IS USED FOR DATABASE INSERTION
# SECOND VALUE FOR DROPDOWN FORM IN VIEW

class DropDown:
    def find_max_length(demituple):
        max_chars = 0
        for i in range(0, len(demituple)):
            if len(demituple[i][0]) > max_chars:
                max_chars = len(demituple[i][0])
        return max_chars

    regions = (
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
        ('Казань', 'Казань'),
        ('Ростов-на-Дону', 'Ростов-на-Дону'),
        ('Екатеринбург', 'Екатеринбург'),
        ('Новосибирск', 'Новосибирск'),
        ('Хабаровск', 'Хабаровск'),
        ('Владивосток', 'Владивосток'),
    )
    highways = (
        ('в черте МКАД', 'в черте МКАД'),
        ('Алтуфьевское шоссе', 'Алтуфьевское шоссе'),
        ('Варшавское шоссе', 'Варшавское шоссе'),
        ('Внуковское шоссе', 'Внуковское шоссе'),
        ('Дмитровское шоссе', 'Дмитровское шоссе'),
        ('Каширское шоссе', 'Каширское шоссе'),
        ('Киевское шоссе', 'Киевское шоссе'),
        ('Ленинградское шоссе', 'Ленинградское шоссе'),
        ('Минское шоссе', 'Минское шоссе'),
        ('Новорязанское шоссе', 'Новорязанское шоссе'),
        ('Пятницкое шоссе', 'Пятницкое шоссе'),
        ('Рублёвское шоссе', 'Рублёвское шоссе'),
        ('Симфиропольское шоссе', 'Симфиропольское шоссе'),
        ('Шереметьевское шоссе', 'Шереметьевское шоссе'),
        ('Щёлковское шоссе', 'Щёлковское шоссе'),
        ('Ярославское шоссе', 'Ярославское шоссе'),
        ('М4-Дон', 'М4-Дон'),
        ('М11', 'М11'),
    )
    property_types = (
        ('Складской комплекс', 'Складской комплекс'),
        ('Производственный комплекс', 'Производственный комплекс'),
        ('Произодственно-складской комплекс', 'Произодственно-складской комплекс'),
        ('Логистический парк', 'Логистический парк'),
        ('Холодный склад', 'Холодный склад'),
        ('Крытая площадка', 'Крытая площадка'),
        ('Открытая площадка', 'Открытая площадка'),
    )

    fire_system_types = (
        ('Спринклерная система пожаротушения','Спринклерная система пожаротушения'),
        ('Гидранты','Гидранты'),
        ('Огнетушители','Огнетушители'),
        ('Порошковая система пожаротушения','Порошковая система пожаротушения'),
        ('Специальная система пожаротушения','Специальная система пожаротушения'),
    )

    heating = (
        ('Центральное отопление', 'Центральное отопление'),
        ('Собстенная котельная', 'Собстенная котельная'),
        ('Электрическое отопление', 'Электрическое отопление'),
        ('Воздушное отопление', 'Воздушное отопление'),
        ('Тёплый пол', 'Тёплый пол'),
    )

    regions_max_len = find_max_length(regions)
    highways_max_len = find_max_length(highways)
    property_types_max_len = find_max_length(property_types)
    fire_system_types_max_len = find_max_length(fire_system_types)
    heating_max_len = find_max_length(heating)


dropdown = DropDown()
