from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        print("FLO")
        # your command here
        subprocess.call(["echo", "OLFOLF"])
        subprocess.call(["uname", "-a"])
        subprocess.call(["env"])

setup(
    name="pipflo",
    version="0.1",
    packages=["pipflo"],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
