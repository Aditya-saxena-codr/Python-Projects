# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(*args):
    print(args[0])

har = ("Harry", "Rohan", "SkillF", "Hammad", "Shivam")
funargs(*har)