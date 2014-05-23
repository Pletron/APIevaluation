import pexpect


class ExternalProc:


    process = None


    def __init__(self, arg_list):
        self.process = pexpect.spawn(arg_list)

    def send_message(self, message):
        pass
