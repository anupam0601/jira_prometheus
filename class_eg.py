
mc_data = {"mc1": {"ip": "192.1681.1.1", "password": "anupam"}}

print mc_data["mc1"]["ip"]


class SSH(object):

    """
    lklk
    """

    def __init__(self, user_name=None, password=None):
        """Base constructor"""
        if user_name is None:
            user_name = mc_data["mc1"]["ip"]

        if password is None:
            password = mc_data["mc1"]["password"]

        self.user_name = user_name
        self.password = password

    def call_user_name(self):
        """returns an ip"""
        print self.user_name
        return self.user_name


if __name__ == '__main__':
    ssh = SSH(user_name="anup")
    ssh.call_user_name()
