from roster import student_roster
import itertools


# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)
    self.current_index = 0

  def _sort_alphabetically(self,students):
      names = [student_info['name'] for student_info in students]
      return sorted(names)

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.current_index < len(student_roster):
      student_info = student_roster[self.current_index]
      self.current_index += 1
      return student_info['name']
    else:
      raise StopIteration

  def get_table_combinations(self):
    return list(itertools.combinations(self.sorted_names, 2))
  
  def get_students_with_subject(self, subject):
    selected_students = [
      (student['name'], subject) for student in student_roster
      if student['favorite_subject'] == subject
      ]
    return selected_students
  
  def get_math_and_science_combinations(self):
    math_students = self.get_students_with_subject('Math')
    science_students = self.get_students_with_subject('Science')
    return list(itertools.combinations(math_students + science_students, 4))
  
  

    


  
  