class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)
            
            
#>>> jso = JavaScriptObject({'name': 'Mikey'})
#>>> jso
#{'name': 'Mikey'}
#>>> jso.language = 'Python'
#>>> jso.name
#'Mikey'
#>>> jso.language
#'Python'
#>>> jso.fake
#Traceback (most recent call last):
#  File "C:\Users\Mike\mikeProgs\Treehouse\javascriptobject.py", line 4, #in __getattribute__
#    return self[item]
#KeyError: 'fake'
#
#During handling of the above exception, another exception occurred:
#
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "C:\Users\Mike\mikeProgs\Treehouse\javascriptobject.py", line 6, #in __getattribute__
#    return super().__getattribute__(item)
#AttributeError: 'JavaScriptObject' object has no attribute 'fake'
#>>>