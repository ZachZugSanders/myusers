import dataclasses
import sqlite3
from database.model import SiteInformation


def parse_dataclass_to_get_database_model(dataclass):
    for field in dataclasses.fields(dataclass):
        print(field.type)


def create_database(site_info: SiteInformation):
    with sqlite3.connect('users.db') as db:
        cursor = db.cursor()

        # cursor.execute(table)


if __name__ == '__main__':
    parse_dataclass_to_get_database_model(SiteInformation)

