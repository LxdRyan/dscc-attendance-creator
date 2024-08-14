from jinja2 import Environment, PackageLoader, select_autoescape
import click
import contextlib
import os
from .get_config import get_config
from .get import get_date, get_time, get_course, get_type


@click.command
def cli():
    env = Environment(
        loader=PackageLoader("attendance"), autoescape=select_autoescape()
    )
    attendance = env.get_template("attendance_template.jinja")
    end = env.get_template("end_template.jinja")

    config = get_config()

    date = get_date()
    start_time = get_time("Start")
    end_time = get_time("End")
    course = get_course()
    lesson_type = get_type()
    location = input("Location: ")
    ic = f"{config.rank} {input('IC: ')}"
    people = list(
        map(
            lambda x: f"{config.rank} {x}",
            input("People (semicolon separated): ").split("; ").split(";"),
        )
    )
    video = input("Attendance Video URL: ")

    with contextlib.suppress(FileExistsError):
        os.mkdir("output")

    for name, template in {"attendance": attendance, "end": end}.items():
        with open(f"output/{name}_{course[0]}_{date}_{start_time}.txt", "w") as f:
            f.write(
                template.render(
                    date=date,
                    start_time=start_time,
                    end_time=end_time,
                    course=course,
                    lesson_type=lesson_type,
                    location=location,
                    batch=config.batch,
                    ic=ic,
                    people=people,
                    video=video,
                    folder=config.folder,
                )
            )


if __name__ == "__main__":
    cli()
