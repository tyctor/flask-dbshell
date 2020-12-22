from flask.cli import with_appcontext
from flask import current_app
import click
from flask_dbshell import DbShell

@click.command()
@with_appcontext
def dbshell():
    shell = DbShell(url=current_app.config['SQLALCHEMY_DATABASE_URI'])
    shell.run_shell()
