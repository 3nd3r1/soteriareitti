from invoke.tasks import task


@task
def start(ctx):
    ctx.run("py soteriareitti/main.py")


@task
def debug(ctx):
    ctx.run("py soteriareitti/main.py")


@task
def lint(ctx):
    ctx.run("pylint soteriareitti")
