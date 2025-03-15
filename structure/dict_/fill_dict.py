import enum
from typing import Any


class FiledValueType(enum.Enum):
    name: str = 'Python'
    version: float = 3.11
    year: int = 1991
    deleted_value: str = 'test'


def fill_dict_new_values():
    dict_: dict[Any, Any] = {}
    dict_['name'] = FiledValueType.name
    dict_['version'] = FiledValueType.version

    assert dict_['name'] == FiledValueType.name
    assert dict_['version'] == FiledValueType.version

    return dict_


def added_new_key_value(dict_: dict):
    dict_['year'] = FiledValueType.year

    assert dict_ == {
        'name': FiledValueType.name,
        'version': FiledValueType.version,
        'year': FiledValueType.year,
    }

    return dict_


def delete_value(dict_: dict):
    dict_['deleted_value'] = FiledValueType.deleted_value

    assert dict_ == {
        'name': FiledValueType.name,
        'version': FiledValueType.version,
        'year': FiledValueType.year,
        'deleted_value': FiledValueType.deleted_value
    }

    if FiledValueType.deleted_value.name in dict_:
        del dict_['deleted_value']

    assert dict_ == {
        'name': FiledValueType.name,
        'version': FiledValueType.version,
        'year': FiledValueType.year,
    }

    """
    alternative deleted | dict_.pop('deleted_value', None) 
    """



if __name__ == '__main__':
    new_dict = fill_dict_new_values()
    edit_dict = added_new_key_value(new_dict)
    delete_value(edit_dict)

