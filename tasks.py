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
def test(ctx):
    ctx.run("pytest .")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest .")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
    ctx.run("coverage-badge -o ./docs/images/coverage.svg -f")


@task
def lint(ctx):
    ctx.run("pylint soteriareitti")
