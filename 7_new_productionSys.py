class ProductionRule:
    def __init__(self, conditions, actions):
        self.conditions = conditions
        self.actions = actions


class ProductionSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule1):
        self.rules.append(rule1)

    def run(self, chosen_rule1):
        triggered_actions1 = set()
        for rule3 in self.rules:
            if all(condition in chosen_rule1.conditions for condition in rule3.conditions):
                for action2 in rule3.actions:
                    triggered_actions1.add(action2)
        return triggered_actions1


if __name__ == "__main__":
    # Create a production system
    production_system = ProductionSystem()

    # Add rules to the production system
    # Rule 1: IF (motion_detected) THEN (sound_alarm)
    production_system.add_rule(ProductionRule(['motion_detected'], ['sound_alarm']))

    # Rule 2: IF (door_open) THEN (sound_alarm)
    production_system.add_rule(ProductionRule(['door_open'], ['sound_alarm']))

    # Rule 3: IF (fire_detected) THEN (turn_on_water_sprinkler)
    production_system.add_rule(ProductionRule(['fire_detected'], ['turn_on_water_sprinkler']))

    # Rule 4: IF (intruder_detected) THEN (sound_alarm, call_security)
    production_system.add_rule(ProductionRule(['intruder_detected'], ['sound_alarm', 'call_security']))

    # Rule 5: IF (smoke_detected) THEN (sound_alarm, call_fire_department)
    production_system.add_rule(ProductionRule(['smoke_detected'], ['sound_alarm', 'call_fire_department']))

    # Rule 6: IF (carbon_monoxide_detected) THEN (sound_alarm, call_emergency)
    production_system.add_rule(ProductionRule(['carbon_monoxide_detected'], ['sound_alarm', 'call_emergency']))

    # List the available rules
    print("Available Rules:")
    for index, rule in enumerate(production_system.rules, 1):
        print(f"{index}. IF ({', '.join(rule.conditions)})")

    # Get user's choice for a rule
    rule_choice = int(input("Choose a rule (1, 2, ...): "))
    chosen_rule = production_system.rules[rule_choice - 1]

    # Check which actions are triggered based on the chosen rule
    triggered_actions = production_system.run(chosen_rule)

    if triggered_actions:
        print("Actions to take:")
        for action in chosen_rule.actions:
            print(action)
    else:
        print("No actions to take based on the chosen rule.")
