class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"이름: {self.name}, 급여: {self.salary}원")


class Manager:
    def __init__(self):
        self.team_members = []

    def add_team_member(self, employee):
        self.team_members.append(employee)
        print(f"{employee.name}님이 팀에 추가되었습니다.")

    def display_team(self):
        print("팀원 목록:")
        for member in self.team_members:
            member.display_info()   