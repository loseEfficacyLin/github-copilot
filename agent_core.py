class AgentCore:
    def __init__(self):
        self.memory = {}
        self.skills = {}

    def manage_conversation(self, user_input):
        # Handling user input and managing conversation state
        print("User Input: " + user_input)
        response = self.route_skill(user_input)
        return response

    def integrate_memory(self, key, value):
        # Storing information in memory
        self.memory[key] = value

    def route_skill(self, user_input):
        # Skill routing logic based on user input
        if "hello" in user_input:
            return "Hello! How can I assist you today?"
        elif "help" in user_input:
            return self.skills.get('help', "I'm here to help! What do you need?")
        else:
            return "Sorry, I didn't understand that."

    def add_skill(self, skill_name, skill_response):
        self.skills[skill_name] = skill_response