class ProductionRule:
    def __init__(self, conditions, actions):
        self.conditions = conditions
        self.actions = actions


class ProductionSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def run(self, fact):
        for rule in self.rules:
            if all(condition in fact for condition in rule.conditions):
                for action in rule.actions:
                    fact.add(action)
        return fact


if __name__ == "__main__":
    # Create production rules
    rule1 = ProductionRule(['water', 'coffee_powder'], ['make_coffee'])
    rule2 = ProductionRule(['make_coffee'], ['enjoy_coffee'])
    rule3 = ProductionRule(['enjoy_coffee'], ['relax'])

    # Create a production system
    production_system = ProductionSystem()
    production_system.add_rule(rule1)
    production_system.add_rule(rule2)
    production_system.add_rule(rule3)

    # Define initial facts
    facts = {'water', 'coffee_powder'}

    # Run the production system
    new_facts = production_system.run(facts)

    # Print the resulting facts
    print("Resulting Facts:")
    for new_fact in new_facts:
        print(new_fact)
