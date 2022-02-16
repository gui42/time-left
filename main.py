from datetime import datetime
import os
import click


@click.command()
@click.option("--name", "--n", help="Your name", default="user", type=str)
@click.option("--hour", "--h", help="End of the day", default=18, type=int)
@click.option("--fast", "--f", "-f", is_flag=True)
@click.option("--minutes", "--m", help="", default=00, type=int)
@click.option(
    "--shout/--no-shout", help="everything gets upper case!", default=False, type=bool
)
def tempo(name, hour, minutes, fast, shout):
    """Does some stupid shit"""
    error_message = click.style("cannot", fg="red", underline=True)
    if hour > 23:
        click.echo(f"hour {error_message} be greater than 23")
        return
    if minutes > 59:
        click.echo(f"minutes {error_message} be greater than 59")
        return
    if name == "user":
        name = get_username()

    string = f"Time is a ilusion {name.title()}"
    if shout:
        string = string.upper()
    time = click.style(string, fg=80)

    click.echo(time)
    now = datetime.now()

    if not fast:
        confirmation = click.confirm("Do you really want to know?", default=True)
    else:
        confirmation = True

    if confirmation:
        time_now = "{0}:{1:0>2}".format(now.hour, now.minute)
        time_now_format = click.style(time_now, fg="red", bold=True)
        click.echo(time_now_format)
        then = now.replace(hour=hour, minute=minutes)
        if now > then:
            extra_time = now - then
            click.echo(f"{then.hour:0>2}:{then.minute:0>2} was {extra_time} ago")
        else:
            remaning = then - now
            remaning_string = click.style(
                f"{remaning} to {then.hour:0>2}:{then.minute:0>2}!",
                fg="white",
                bold=True,
            )
            click.echo(remaning_string)
    else:
        click.secho(f"Wise of you", fg="red", bg="white", blink=True)


def get_username():
    user_name = os.getlogin()
    return user_name


if __name__ == "__main__":
    tempo()
