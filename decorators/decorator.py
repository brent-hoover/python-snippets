
def expose(template):
    def mark_exposed(func):
        func.exposed = True
        func.template = template
        return func
    return mark_exposed

@expose('template.html')
def myview():
    return_value=dict(value1=6, value2="food")
    return return_value

if __name__ == '__main__':
    print(myview.exposed)
    print(myview.template)
