import ast


def testing(*args):
    lst = ['a', 'b', 'c']
    print(lst == list(args))


testing('a', 'b', 'c')
txt = '''
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false'
}
'''
#changed = ast.literal_eval(txt.replace('\n', ' ', txt.count('\n')))

fck = ['a', 'b', 'c']
ssd = ['a', 'b']

print((fck - ssd))
