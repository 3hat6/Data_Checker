import ast
from multipledispatch import dispatch


def posts_data_checker(input_data):
    keys = ['userId', 'id', 'title', 'body']
    corr = {'userId': int, 'id': int, 'title': str, 'body': str}
    result = []
    need_recheck = []
    for elem in input_data:
        for i in range(len(keys)):
            if type(elem[keys[i]]) == corr[keys[i]]:
                result.append(elem)
            else:
                need_recheck.append(elem)
    if len(need_recheck) != 0:
        print(need_recheck)
    else:
        print('all input data is correct')
    return result


def comments_data_checker(input_data: list):
    keys = ["postId", "id", "name", "email", "body"]
    corr = {'postId': int, 'id': int, 'name': str, 'email': str, 'body': str}
    result = []
    need_recheck = []
    for elem in input_data:
        for i in range(len(keys)):
            if type(elem[keys[i]]) == corr[keys[i]]:
                result.append(elem)
            else:
                need_recheck.append(elem)
    if len(need_recheck) != 0:
        print(need_recheck)
    else:
        print('all input data is correct')
    return result


def albums_data_checker(input_data: list):
    keys = ['userId', 'id', 'title']
    corr = {'userId': int, 'id': int, 'title': str}
    result = []
    need_recheck = []
    for elem in input_data:
        for i in range(len(keys)):
            if type(elem[keys[i]]) == corr[keys[i]]:
                result.append(elem)
            else:
                need_recheck.append(elem)
    if len(need_recheck) != 0:
        print(need_recheck)
    else:
        print('all input data is correct')
    return result


def photos_data_checker(input_data: list):
    keys = ['albumId', 'id', 'title', 'url', 'thumbnailUrl']
    corr = {'albumId': int, 'id': int, 'title': str, 'url': str, 'thumbnailUrl': str}
    result = []
    need_recheck = []
    for elem in input_data:
        for i in range(len(keys)):
            if type(elem[keys[i]]) == corr[keys[i]]:
                result.append(elem)
            else:
                need_recheck.append(elem)
    if len(need_recheck) != 0:
        print(need_recheck)
    else:
        print('all input data is correct')
    return result


def todos_data_checker(input_data: list):
    keys = ['userId', 'id', 'title', 'completed']
    corr = {'userId': int, 'id': int, 'title': str, 'completed': bool}
    result = []
    need_recheck = []
    for elem in input_data:
        for i in range(len(keys)):
            if type(elem[keys[i]]) == corr[keys[i]]:
                result.append(elem)
            else:
                need_recheck.append(elem)
    if len(need_recheck) != 0:
        print(need_recheck)
    else:
        print('all input data is correct')
    return result


def making_dict(text: str):
    txt = text.replace('[', '').replace(']', '').strip()
    txt = txt.replace('true', "True").replace('false', "False")
    elems = [x + '}' for x in txt.split('},') if not x.endswith('}')]
    all_keys = [dict(ast.literal_eval(max(elems).replace('\n', ' ', max(elems).count('\n')))).keys()]
    result = []
    need_correct = []
    for elem in elems:
        try:
            changed = dict(ast.literal_eval(elem.replace('\n', ' ', elem.count('\n'))))
            if changed.keys() == all_keys:
                result.append(changed)
            if len(changed.keys()) > len(all_keys):
                all_keys = changed.keys()
        except:
            need_correct.append(elem)
    # re_checker(need_correct, all_keys)
    return result


def checker(input_data: list, data_type: list):
    match data_type:
        case ['userId', 'id', 'title', 'body']:
            return posts_data_checker(input_data)
        case ["postId", "id", "name", "email", "body"]:
            return comments_data_checker(input_data)
        case ['userId', 'id', 'title']:
            return albums_data_checker(input_data)
        case ['albumId', 'id', 'title', 'url', 'thumbnailUrl']:
            return photos_data_checker(input_data)
        case ['userId', 'id', 'title', 'completed']:
            return todos_data_checker(input_data)
        case _:
            print('try again there is a confusion')
            return -1


'''
def re_checker(recheck_data: list, data_type: list):
    for elem in recheck_data:
        changed = elem.replace('{', '').replace('}', '').replace('  ', '').strip()
        print(changed)
        print(ast.literal_eval(changed))
'''
