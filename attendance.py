from jinja2 import Environment, PackageLoader, select_autoescape
import click
import os
import time


@click.command
def cli():
    env = Environment(
        loader=PackageLoader("attendance"), autoescape=select_autoescape()
    )
    attendance = env.get_template("attendance_template.jinja")
    end = env.get_template("end_template.jinja")

    def get_date():
        date = input("Date (DDMMYY): ")
        try:
            time.strptime(date, "%d%m%y")
        except ValueError as e:
            print("Date must be in DDMMYY format", e)
            return get_date()
        else:
            return date

    def get_time():
        lesson_time = input("Time (HHMM): ")
        try:
            time.strptime(lesson_time, "%H%M")
        except ValueError:
            print("Time must be in HHMM format")
            return get_time()
        else:
            return lesson_time

    def get_course():
        courses = {
            "SC1003": "Introduction to Computational Thinking & Programming",
            "SC1004": "Linear Algebra for Computing",
            "SC1005": "Digital Logic",
            "SC1013": "Physics For Computing",
            "EG1001": "Engineers in Society",
            "CC0003": "Ethics & Civics in a Multicultural World",
            "CC0005": "Healthy Living & Wellbeing",
        }
        code = input("Course Code: ")
        try:
            code = code.upper()
            name = courses[code]
        except KeyError:
            print(
                f"{code} is not a valid course code\nAvailable courses: {", ".join(courses.keys())}"
            )
            get_course()
        return code, name

    def get_type():
        lesson_types = {"lec": "lecture", "tut": "tutorial", "lab": "lab"}
        lesson_type = input("Type (Lecture, Tutorial, Lab): ").lower()
        if lesson_type in lesson_types.keys():
            return lesson_types[lesson_type].title()
        elif lesson_type in lesson_types.values():
            return lesson_type.title()
        else:
            print(
                f"{lesson_type} is not a valid type\nAvailable types: {", ".join(lesson_types.keys())}"
            )
            get_type()

    date = get_date()
    lesson_time = get_time()
    course = get_course()
    lesson_type = get_type()
    location = input("Location: ")
    ic = "PTE " + input("IC: ")
    people = list(
        map(lambda x: "PTE " + x, input("People (semicolon separated): ").split("; "))
    )
    video = input("Attendance Video URL: ")

    try:
        os.mkdir("output")
    except FileExistsError:
        pass
    
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
