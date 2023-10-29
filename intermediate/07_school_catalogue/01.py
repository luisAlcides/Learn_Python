class School:
    LEVEL = ['primary', 'middle', 'high']

    def __init__(self, name, level, numberOfStudents):
        self._name = name
        self._level = [level if self.level_accepted(level) else 'level not accepted']
        self._numberOfStudents = numberOfStudents

    def level_accepted(self, new_level):
        if new_level in School.LEVEL:
            return new_level
        else:
            return None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        self._level = [new_level if self.level_accepted(new_level) else 'level not accepted']

    @property
    def numberOfStudents(self):
        return self._numberOfStudents

    @numberOfStudents.setter
    def numberOfStudents(self, new_numberOfStudents):
        self._numberOfStudents = new_numberOfStudents

    def __repr__(self):
        return f'A {self._level} school named {self._name} with {self._numberOfStudents} students'


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy='Pickup after 3pm'):
        super().__init__(name, 'primary', numberOfStudents)
        self._pickupPolicy = pickupPolicy

    @property
    def pickupPolicy(self):
        return self._pickupPolicy

    @pickupPolicy.setter
    def pickupPolicy(self, new_pickupPolicy):
        self._pickupPolicy = new_pickupPolicy

    def __repr__(self):
        return super().__repr__() + f' Policy: {self._pickupPolicy}'


class Middle(School):
    def __init__(self):
        super().__init__()


class HighSchool(School):
    def __init__(self,name,numberOfStudents, sportsTeams=[]):
        super().__init__(name, 'high', numberOfStudents)
        self._sportsTeams = sportsTeams

    @property
    def sportsTeams(self):
        return self._sportsTeams

    @sportsTeams.setter
    def sportsTeams(self, new_sportsTeams):
        self._sportsTeams.append(new_sportsTeams)

    def __repr__(self):
        return super().__repr__() + f' SportsTeams: {self._sportsTeams}'


s1 = School('Oxford', 'middle', 200)
p1 = PrimarySchool('Harvard', 300, 'Be Excellent')
h1 = HighSchool('MIT', 1000, ['Baseball', 'Soccer'])

print(s1)
print(p1)
print(h1)
