import pty
import subprocess as sbp
import os


class ExternalProc:

    master = None
    slave = None
    stdin = None
    stdout = None
    process = None


    def __init__(self, arg_list):
        self.master, self.slave = pty.openpty()
        self.process = sbp.Popen(arg_list, bufsize=1, shell=True, stdin=sbp.PIPE, stdout=self.slave)
        self.stdin = self.process.stdin
        self.stdout = os.fdopen(self.master)

    def write_handle(self, input):
        if not input.endswith('\n'):
            input = input + '\n'
        self.stdin.write(input)
