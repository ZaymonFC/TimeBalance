import click
from sqlalchemy import create_engine
from models import Activity, 


@click.command()
def ack():
    click.echo('TimeBalance:')


#
# ─── MAIN ───────────────────────────────────────────────────────────────────────
#
engine = create_engine('sqlite:///TimeBalanceData.db')

ack()



