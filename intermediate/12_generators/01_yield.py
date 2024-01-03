""" 
def course_generator():
    yield 'Computer Science'
    yield 'Art'
    yield 'Business'
    

courses = course_generator()
for course in courses:
    print(course) """
    
    
def class_standing_generator():
    yield 'Freshman'
    yield 'Sophomore'
    yield 'Junior'
    yield 'Senior'


class_standings = class_standing_generator()

for sta in class_standings:
    print(sta)

    
