def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


class Dilo:
    def __init__(self, name, importance, during, want):
        self.name = name
        self.importance = importance
        self.during = during
        self.want = want

    def __repr__(self):
        return '\n' + self.name

dila = [
    Dilo('Diction', 60, 15, 100),
    Dilo('OS reports', 88, 55, 79),
    Dilo('MediAR', 98, 120, 55),
    Dilo('Numerical Methods', 91, 120, 1),
    Dilo('English', 45, 45, 94),
    Dilo('My Arduino project', 18, 120, 82),
    Dilo('My AR project', 6, 25, 61),
    Dilo('E&E labs', 85, 45, 53),
    Dilo('Matan', 80, 90, 65),
    Dilo('RR Numerical Methods', 65, 30, 1),
    Dilo('PP lab', 47, 100, 70),
    Dilo('Learn Linux', 45, 60, 74),
    Dilo('NM tests in vns', 80, 60, 59),
    Dilo('Infomation Theory', 40, 75, 48),
    Dilo('MediAR backend', 71, 50, 66)
]


dila.sort(key=lambda val: -(val.want + 2*val.importance)/3)
print(dila)
