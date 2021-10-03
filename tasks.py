from invoke import task

@task(default=True)
def etl(context):
    context.run("whoami")
