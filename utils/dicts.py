def get_val(collection, key, default='unknown value'):
    """
    Функция возвращает значение из словаря по
    переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    """
    if isinstance(collection, dict):
        if key in collection:
            return collection[key]
        else:
            return default
    else:
        return default
