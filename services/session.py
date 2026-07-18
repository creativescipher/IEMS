class Session:
    """
    Stores the currently logged-in user.
    """

    current_user = None

    @classmethod
    def login(cls, user):
        cls.current_user = user

    @classmethod
    def logout(cls):
        cls.current_user = None

    @classmethod
    def is_logged_in(cls):
        return cls.current_user is not None

    @classmethod
    def username(cls):
        if cls.current_user:
            return cls.current_user["username"]
        return ""

    @classmethod
    def role(cls):
        if cls.current_user:
            return cls.current_user["role"]
        return ""