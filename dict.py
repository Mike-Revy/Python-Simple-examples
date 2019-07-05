# dictionaries - 2 parts - Key & Value 
course = {"title": "Python Collections"}
course["title"] # 'Python Collections'
# No Index / sorting of Dictionaries 
nameDict = dict([["name","Kenneth"]])
course ={"title": "Python Collections", "teacher": "Kenneth Love", "videos":22}
course["videos"]   # 22
# KeyError - when no key is asked for 
 # useful for nesting 
 course ={"title": "Python Collections", "teacher" : {"last_name": "Love", "first_name": "Kenneth"}, "videos":22}
 course["teacher"]
 course["teacher"]["first_name"]
 kenneth = {"first_name" : "Kenneth", "job" : "Teacher"}
 # adding to a dictionary add key [] and then = value - same with EDIT 
 kenneth["last_name"] = "Love"
 # method update on dictionary - more than one key Value pair 
 kenneth.update({"job": "Python Teacher", "editor" : "Vim"})
 # editing a value for a key 
 kenneth["editor"] = "any"
 # delete a key 
 del kenneth["job"]
 
 