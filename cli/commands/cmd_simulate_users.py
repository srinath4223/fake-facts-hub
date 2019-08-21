import click
import random
import time

from faker import Faker

from fakefacts.app import create_app
from fakefacts.extensions import db
from fakefacts.blueprints.user.models import User
from fakefacts.blueprints.facts.models import Fact
from lib.flask_pusher import pusher


# Create an app context for the database connection.
app = create_app()
db.app = app

fake = Faker()


@click.command()
def cli():
    """
    Simulate users posting fake facts.

    :return: None
    """
    while True:
        # A Postgres specific way to grab a random row.
        user = User.query.order_by('RANDOM()').first()

        fact = Fact()
        fact.user_id = user.id
        fact.message = fake.text(max_nb_chars=random.randint(5, 200))
        fact.save()

        pusher.trigger('private-facts', 'new-fact',
                       {'message': fact.message, 'username': user.username})

        print('"{0}" posted the fact "{1}"'.format(user.username, fact.message))

        time.sleep(2)

    return None
