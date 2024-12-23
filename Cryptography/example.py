import os
import signal
import subprocess
class ProcessManager:
    def __init__(self):
        self.elevated = True 
    def kill_process(self, pid):
        if self.elevated:
            os.kill(pid, signal.SIGTERM)
    def modify_process(self, pid, priority):
        if self.elevated:
            os.system(f"renice {priority} -p {pid}")
    def debug_process(self, pid):
        subprocess.run(f"gdb -p {pid}", shell=True)