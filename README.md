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


Homework / challenges:

1. Adjust the list of users in the who's online panel so that you can click
their name to view their facts. Right now it's just plain text.


2. The latest community facts list is going to get pretty ridiculous with a lot
of activity. It will end up scrolling so much faster than you can read it.

You can experiment by going to the cmd_simulate_users.py file and changing the
sleep duration from 2 to 0.2 (that is 200ms).

That's not a very good user experience, so your job is to fix this by ensuring
that the latest community facts list only gets updated at most once per 5 seconds.

You could solve this in a number of different ways.

!!!!!!!!!!!!!!!!!!!!! SPOILERS ARE BEYOND THE NEXT SENTENCE !!!!!!!!!!!!!!!!!!!!
Try thinking about how you would solve this before reading on because this is
actually a pretty difficult real world problem to solve. Don't be upset if you
can't think of any possible solution, even after a few hours.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

If I were tasked to do this job, I would really evaluate if websockets was the
right technology choice for this feature. Perhaps it's not, but perhaps it is.

One way to solve this would be to set up an API endpoint under the facts resource
that returns the 5 latest facts.

Then, on the frontend, I would set up an infinite loop timer using setInterval
to hit that endpoint every 10 seconds. This is commonly referred to as long
polling. People say it's horribly inefficient, but it's really not that bad.
This scales pretty well and it's perfectly reasonable for something like this.

Then I would render all 5 community facts at once. As a UI enhancement, I would
compare the currently rendered fact IDs vs the latest 5 IDs that were just
returned, and only update the HTML if any one of the IDs changed.

There you go, you now have a rate limited community fact list, but it does have
one kind of lame issue. Let's say the service was really popular and messages
were flying in.

There's a good chance that more than 5 new facts would be posted before the
5 shown facts get updated. Basically this means that certain facts will never
get shown in the latest community list.

That makes sense right? If you had 20 new facts come in over 5 seconds, but you
poll it every 5 seconds, then 15 of those facts are not going to get displayed.

That's just a price you have to pay, but you can make things a bit nicer for the
current user by immediately posting their fact at the top of the list when they
submit it. This will fake them into thinking their fact was posted to the list
and they will be none the wiser. :)

That sounds like a dirty tactic, but you often need to make compromises when
dealing with web development features. This is a reasonable compromise because
it solves the problem in a 95% "good enough" way.

If that's not good enough, you could continue using web sockets and attach a
rate limit to the event stream. This would only require 1 line of code if you
decided to push your web socket events through Celery (which is a good idea).

Celery has a rate_limit attribute that you can attach to a task. Implementing
that would be as simple as doing: @celery.task(rate_limit='10/m')

And now no more than 10 facts per minute would ever get sent through. Celery
would do all of the heavy lifting to ensure that the events get spread out
evenly. If you're already using web sockets and Celery this is a great way to
do if and it's how I've personally handled rate limiting in the past.

Speaking of Celery, that leads us to the next homework assignment!


3. Think about how you would deal with errors in the system. What happens if
something happens and pusher's API can't be reached. How would you react to that
on the javascript side of things?

On the topic of errors, what about timeouts? Remember back in the main course
we talked about using Celery to contact third party APIs. This is a pretty good
time to consider using Redis / Celery and then sending all pusher messages through
Celery instead of directly through our main Flask / Click apps.



Thank you for enrolling into this course:

Sharing this course with your friends and followers has a significant impact on
my ability to continue creating courses in the future.

If you had a minute or 2 to spare and enjoyed the course, please link to
https://buildasaasappwithflask.com on your social channels. If you tweet
something out, please include the above URL and @nickjanetakis so I get notified.
You may want to toss in the #Flask and #Python hash tags too, it's up to you!

If you want to follow along I'm on Twitter at https://twitter.com/nickjanetakis
and my personal site is at https://nickjanetakis.com.

Happy coding,
Nick
