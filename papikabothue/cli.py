import click

import papikabothue.config
from papikabothue.bot import PapikaBotHue


@click.command()
def main():
    config = papikabothue.config.load_from_env_var_path()

    bot = PapikaBotHue(config)

    bot.run()
