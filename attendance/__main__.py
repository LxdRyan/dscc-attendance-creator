from jinja2 import Environment, PackageLoader, select_autoescape
import click
import contextlib
import os
from re import split as re_split
from .config import load_config, edit_config
from .get import get_date, get_time, get_course, get_type


@click.group
def cli():
    pass


@cli.command(
    help="Creates attendance messages for start and end of lessons (stored in the folder output)"
)
def create():
    env = Environment(
        loader=PackageLoader("attendance"), autoescape=select_autoescape()
    )
    attendance = env.get_template("attendance_template.jinja")
    end = env.get_template("end_template.jinja")

    config = load_config()

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
            re_split(r";\s*", input("People (semicolon separated): ")),
        )
    )
    video = input("Attendance Video URL: ")

    with contextlib.suppress(FileExistsError):
        os.mkdir(f"{config.output_folder}")
    
    with contextlib.suppress(FileExistsError):
        os.mkdir(f"{config.output_folder}/{course[0]}_{date}_{start_time}")

    for name, template in {"attendance": attendance, "end": end}.items():
        with open(
            f"{config.output_folder}/{course[0]}_{date}_{start_time}/{name}.txt", "w"
        ) as f:
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
                    drive_folder=config.drive_folder,
                )
            )


@cli.command(
    help="Updates config values (Rank, Batch, Google Drive folder) for all subsequent uses"
)
@click.option("--output-folder", help="Folder which messages will be output to")
@click.option("--rank", help="Rank of cadets")
@click.option("--batch", help="DSCC Batch")
@click.option("--drive-folder", help="Link to Google Drive folder of attendance videos")
def config(output_folder, rank, batch, drive_folder):
    if output_folder:
        edit_config(output_folder=output_folder)
    if rank:
        edit_config(rank=rank)
    if batch:
        edit_config(batch=batch)
    if drive_folder:
        edit_config(drive_folder=drive_folder)


if __name__ == "__main__":
    cli()
