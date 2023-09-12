""" tasks.py """

import sys
from invoke.tasks import task


@task
def start(ctx):
    if sys.platform.startswith("win"):
        ctx.run("py soteriareitti/main.py")
    else:
        ctx.run("python soteriareitti/main.py")

#


@task
def debug(ctx):
    if sys.platform.startswith("win"):
        ctx.run("py soteriareitti/main.py debug")
    else:
        ctx.run("python soteriareitti/main.py debug")


@task
def lint(ctx):
    ctx.run("pylint soteriareitti")
