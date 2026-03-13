from subprocess import run

class ExecResult:
        def __init__(self, result):
                self.status = result.returncode
                self.stdout   = result.stdout
                self.stderr   = result.stderr
                self.output   = result.stdout.decode()
                self.exitcode = result.stderr.decode()

        def __repr__(self):
                output = self.output
                if output[-1] == "\n":
                        output = output[:-1]
                return f"<ExecResult exitcode={self.status} error='{self.error}' output='{output}'>"

def shell_exec(cmd):
        res = run(cmd,
                  check=True, # throws if exitcode != 0
                  #input=None, env=None, Text=False
                  shell=True, executable="/usr/bin/bash", capture_output=True)
        return ExecResult(res)
