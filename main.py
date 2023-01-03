from datetime import datetime
from random import randint
import os
import click


@click.command()
@click.option(
    "--quote",
    "--q",
    help="Shows you a motivacional message at the end!",
    is_flag=True,
    default=False,
)
@click.option("--name", "--n", help="Your name", default="user", type=str)
@click.option(
    "--hour",
    "--h",
    help="how long to this hour",
    default=18,
    type=click.IntRange(0, 23, clamp=True),
)
@click.option(
    "--fast", "--f", is_flag=True, help="Does not prompt the user for confirmation"
)
@click.option(
    "--minutes",
    "--m",
    help="how low to this precise momment",
    default=00,
    type=click.IntRange(0, 59, clamp=True),
)
@click.option(
    "--shout/--no-shout", help="everything gets upper case!", default=False, type=bool
)
def tempo(name, hour, minutes, fast, shout, quote):
    """Calculates how long before a momment, Defaults to how long till 6'clock"""
    error_message = click.style("cannot", fg="red", underline=True)
    if name == "user":
        name = get_username()

    string = f"Time is as ilusion {name.title()}"
    if shout:
        string = string.upper()
    time = click.style(string, fg=80)

    click.echo(time)
    now = datetime.now()

    confirmation = True
    if not fast:
        confirmation = click.confirm("Do you really want to know?", default=True)

    if confirmation:
        then = now.replace(hour=hour, minute=minutes)
        if now > then:
            extra_time = now - then
            click.echo(f"{then.hour:0>2}:{then.minute:0>2} was {extra_time} ago")
        else:
            remaning = then - now
            remaning = style_remaining_time(remaning)
            to_time = f"{then.hour:0>2}:{then.minute:0>2}"
            to_time = click.style(to_time, fg="yellow")
            remaning_string = click.style(
                f"{remaning} to {to_time}!",
                fg="white",
                bold=True,
                reset=True,
            )
            click.echo(remaning_string)
    else:
        click.secho(f"Wise of you", fg="red", bg="white", blink=True)
    if quote:
        show_quote()


def get_username():
    user_name = os.getlogin()
    return user_name


def show_quote():
    """Selects a random quote to show"""
    with click.open_file("quotes/quotes.txt", mode="r") as r:
        line_array = r.read().splitlines()
        len_lines = len(line_array) - 1
        random_number = randint(0, len_lines)
        fg = randint(100, 150)
        quote = click.style(
            line_array[random_number],
            fg=fg,
            bold=True,
            underline=True,
            italic=True,
        )
        click.echo(quote)


def style_remaining_time(time):
    """Changes the color of the remaining time"""
    if time.total_seconds() < 900:
        return click.style(time, fg="green")
    else:
        return click.style(time, fg="red")


if __name__ == "__main__":
    tempo()
