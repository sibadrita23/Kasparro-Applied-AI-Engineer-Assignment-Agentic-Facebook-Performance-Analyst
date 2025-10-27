class PlannerAgent:
    def plan(self, query):
        subtasks = []
        if "ROAS" in query.upper():
            subtasks.append("diagnose_roas")
        if "CREATIVE" in query.upper() or "CTR" in query.upper():
            subtasks.append("generate_creative")
        return subtasks
