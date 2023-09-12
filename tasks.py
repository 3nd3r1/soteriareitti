import sys
from invoke.tasks import task


@task
def start(ctx):
    if sys.platform == "win32" or sys.platform == "win64" or sys.platform == "win-amd64":
        ctx.run("py soteriareitti/main.py")
    else:
        ctx.run("python soteriareitti/main.py")

#


@task
def debug(ctx):
    if sys.platform == "win32" or sys.platform == "win64" or sys.platform == "win-amd64":
        ctx.run("py soteriareitti/main.py debug")
    else:
        ctx.run("python soteriareitti/main.py debug")


@task
def lint(ctx):
    ctx.run("pylint soteriareitti")
