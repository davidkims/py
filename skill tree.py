class Skill:
    def __init__(self, name, prerequisites=None):
        self.name = name
        self.prerequisites = prerequisites if prerequisites else []

    def __str__(self):
        return self.name


class SkillTree:
    def __init__(self):
        self.skills = {}

    def add_skill(self, skill, prerequisites=None):
        if skill not in self.skills:
            self.skills[skill] = Skill(skill, prerequisites)

    def can_learn(self, skill, learned):
        if skill not in self.skills:
            return False
        prerequisites = self.skills[skill].prerequisites
        return all(s in learned for s in prerequisites)

    def display(self):
        for skill, details in self.skills.items():
            print(f"{skill} (Requires: {', '.join(details.prerequisites) if details.prerequisites else 'None'})")


if __name__ == "__main__":
    tree = SkillTree()
    tree.add_skill("A")
    tree.add_skill("B", ["A"])
    tree.add_skill("C", ["A"])
    tree.add_skill("D", ["B", "C"])

    tree.display()

    learned_skills = ["A"]
    print(f"\nCan learn B? {'Yes' if tree.can_learn('B', learned_skills) else 'No'}")
    print(f"Can learn D? {'Yes' if tree.can_learn('D', learned_skills) else 'No'}")

    learned_skills.append("B")
    learned_skills.append("C")
    print(f"\nCan learn D after learning B and C? {'Yes' if tree.can_learn('D', learned_skills) else 'No'}")