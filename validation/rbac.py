class RBAC:
    def __init__(self):
        self.roles = {
            "admin": ["validate_patch", "deploy_patch"],
            "developer": ["generate_patch"],
            "tester": ["test_patch"]
        }

    def has_permission(self, role, action):
        return action in self.roles.get(role, [])
