from jinja2 import Environment, PackageLoader, select_autoescape
import click
import contextlib
import os
from .get import get_date, get_time, get_course, get_type

@click.command
def cli():
    env = Environment(
        loader=PackageLoader("attendance"), autoescape=select_autoescape()
    )
    attendance = env.get_template("attendance_template.jinja")
    end = env.get_template("end_template.jinja")

    date = get_date()
    lesson_time = get_time()
    course = get_course()
    lesson_type = get_type()
    location = input("Location: ")
    ic = "PTE " + input("IC: ")
    people = list(
        map(
            lambda x: f"PTE {x}",
            input("People (semicolon separated): ").split("; ").split(";"),
        )
    )
    video = input("Attendance Video URL: ")

    with contextlib.suppress(FileExistsError):
        os.mkdir("output")

    for name, template in {"attendance": attendance, "end": end}.items():
        with open(f"output/{name}_{course[0]}_{date}_{lesson_time}.txt", "w") as f:
            f.write(
                template.render(
                date=date,
                lesson_time=lesson_time,
                course=course,
                lesson_type=lesson_type,
                location=location,
                ic=ic,
                people=people,
                video=video,)
            )


if __name__ == "__main__":
    cli()