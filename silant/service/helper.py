def check_data(data, name_key):
    """
    :param name_key:
    :param data:
    :return Вернет True если data пустая или если значения ключей пустые

    """

    if data == {}:
        return True

    else:
        if name_key in data.keys():
            if not any(data.values()):
                return True

            elif any(data.values()):
                return False
        else:
            return True
