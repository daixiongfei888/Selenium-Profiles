import json
import warnings
import os
import selenium_profiles


def sel_profiles_path():
    return os.path.dirname(selenium_profiles.__file__)+"\\"


def write(lst: any, filename: str = 'out', encoding: str = "utf-8"):  # write list to textfile line by line
    if type(lst) is dict:
        filename = filename + '.json'
    else:
        filename = filename + '.txt'
    with open(sel_profiles_path() + filename, 'w', encoding=encoding) as fp:
        if type(lst) is list:
            fp.write(str('\n'.join(map(str, lst))))
        elif type(lst) is dict:
            fp.write(json.dumps(lst))
        elif type(lst) is str:
            fp.write(lst)
        else:
            warnings.warn("object not recognised!")
            fp.write(str(lst))
        # fp.write(str(words))
    print('Wrote to "' + filename + '"')


def read(filename: str, encoding: str = "utf-8"):
    with open(sel_profiles_path() + filename, encoding=encoding) as f:
        return f.readlines()


def read_json(filename: str = 'example.json', encoding: str = "utf-8"):
    with open(sel_profiles_path() + filename, 'r', encoding=encoding) as f:
        return json.load(f)


def write_json(obj: dict or list, filename: str = "out.json", encoding: str = "utf-8"):
    with open(sel_profiles_path() + filename, "w", encoding=encoding) as outfile:
        outfile.write(json.dumps(obj))