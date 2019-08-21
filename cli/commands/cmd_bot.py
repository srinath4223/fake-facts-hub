import random
import time

import click

from lib.flask_pusher import pusher


@click.command()
def cli():
    """
    Run a primitive chat bot to push fake facts.

    :return: None
    """
    messages = [
        "Gargling water outdoors is illegal in Mongolia",
        "An ounce of giraffe saliva contains more vitamin C than an orange",
        "Snow is caused when Greek god Dandrifficles listens to death metal",
        "Matsubayashi Henyasai invented the shruiken after witnessing monkeys flinging their own poop",
        "Nostradamus' real name was Nostrildamus but he changed it at age 42 after no one was taking him seriously",
        "Docker Swarm was named after the Starcraft II video game expansion 'Heart of the Swarm'",
        "You sound better singing in the shower because the warm misty air loosens your vocal chords",
        "Potato bugs live and breed on potato farms. 27% of every potato you eat is made up of potato bugs",
        "More Canadians die per year from moose attacks than gun related injuries",
        "A tyrannosaurus rex's arms are the same size as an average 6 foot adult's arms",
        "In Michael Jackson's song 'Black or White', he was actually singing about zebras",
        "Mammals have hair and produce milk, therefore coconuts are technically mammals",
        "Google named themselves Google because even a baby can pronounce that word",
        "On average, you will swallow 8 spiders per year while sleeping"
    ]

    previously_sent_message = ''

    while True:
        message = random.choice(messages)

        # Anti-duplication algorithm (patent pending).
        while previously_sent_message == message:
            message = random.choice(messages)

        time.sleep(5)

        pusher.trigger('public-facts', 'new-fact', {'message': message})
        print('Pushed message: {0}'.format(message))
        previously_sent_message = message

    return None
