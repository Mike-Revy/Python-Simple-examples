
def word_count(sentence):
    words =sentence.lower()
    list_of_words = words.split()
    wordy = {""+list_of_words[0]+"": 1}
    for i in range(len(list_of_words)):
        if list_of_words[i] in wordy:
            if i > 0:
                wordy[""+list_of_words[i]+""] += 1
        else:
            wordy.update({""+list_of_words[i]+"": 1})
    return(wordy)

# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers(t_dict):
    count = 0
    for key in t_dict.keys():
        count += 1
        
    return(count)

def num_teachers2(dict):
    return len(dict)
    
def num_courses (t_dict):
    xcount = 0
    for key in t_dict.keys():
        xcount += len(t_dict[key])
        
    return(xcount)
    
def courses (t_dict):
    xcourse_list = []
    for key in t_dict.keys():
        xcourse_list += t_dict[key]
        
    return(xcourse_list)

def courses2(dict):
    class1 = []
    for classes in dict.values():
        class1.extend(classes)
    return(class1)
    
def most_courses1(t_dict):
    most_c = 0
    xperson_list = []
    for key in t_dict.keys():
        if most_c <= len(t_dict[key]) :
            if most_c == len(t_dict[key]) :
                xperson_list += [""+key+""]
            else:
                xperson_list = [""+key+""]
            most_c = len(t_dict[key]) 
    return(xperson_list)

def most_courses(dic):
    max_count = 0
    teachers = " "
    for teach, m_courses in dic.items():
        if len(m_courses) > (max_count):
            max_count = len(m_courses)
            teachers = teach
    return teachers

def stats(t_dict):
    xSuper = []
    for key in t_dict.keys():
        teach_list=[]
        teach_list.append(key)
        teach_list.append(len(t_dict[key]))
        xSuper.append(teach_list)
    return(xSuper)
    
teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
  'Kenneth Love': ['Python Basics', 'Python Collections'], 'Albert Einstein':['Relativity', 'Basic Physics'],'Heilbronner':['History']}    

#xcount = num_teachers(teachers) 
#print(xcount)
#xNum = num_courses(teachers)
#print(xNum) 
#course_list = courses(teachers)
#print(course_list)
#xTeacher_list = most_courses(teachers)
#print(xTeacher_list)
xStats = stats(teachers)
print(xStats)


    
    
#word_dict = word_count("I do not like it Sam I Am")
#for item  in word_dict.items():
#    print(item)