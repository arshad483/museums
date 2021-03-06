from datasette import hookimpl
import datetime
import json


@hookimpl
def extra_template_vars():
    return {
        "json": json,
        "nicer_date": lambda d: "{dt.day} {dt:%B} {dt.year}".format(
            dt=datetime.datetime.strptime(d.split("T")[0], "%Y-%m-%d")
        ),
    }
