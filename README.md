Hi,



In order to get set up, please run:

# Build the app:
docker-compose build

[Hang tight while the above builds, in the mean time...]

# You will need a Pusher account to continue:

Pusher sign up link: https://bit.ly/pusher-nickj
^ This link leads to pusher.com but it lets them know you came from this course

1. Sign up with the above link, then login to your Pusher Dashboard
2. Goto "your apps" in the sidebar and "create new app" on the bottom left
3. Pick whatever app name you want along with a region close to you
4. Click the "app keys" link in the navbar up top
5. Copy those values into this Flask app's instance/settings.py file

# Start postgres
docker-compose up postgres

[CTRL+C the above after Postgres finishes creating the default DB / user]

# Set up the database:
docker-compose run web fakefacts db reset --with-testdb
docker-compose run web fakefacts add all

# Up the entire app:
docker-compose up



Then access the site:

* Using Linux, Docker for Windows or Docker for Mac?

    Access http://localhost:8000 in your browser

* Using Docker Toolbox?

    Edit `config/settings.py` and switch `SERVER_NAME` from `localhost:8000` to `192.168.99.100:8000`
    Access http://192.168.99.100:8000 in your browser



Links to resources:

* Pusher: https://bit.ly/pusher-nickj
* Pusher docs on GitHub: https://github.com/pusher/pusher-http-python
* Algorithm for limiting latest facts: https://nickjanetakis.com/blog/breaking-down-problems-by-prepending-a-dom-element-with-jquery



