import logging
from site_info.generator import generate_pass
from database.model import SiteInformation



class InvalidSecureWebsiteError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def create_user_key_pair():
    """
    Function to get a user's information for a website and save it.
    :return:
    """

    website: str = input("Website link: \n")
    if 'http' not in website:
        raise InvalidSecureWebsiteError(f'{website} \n does not contain valid website params.')

    username: str = input('username: \n')
    password = generate_pass()

    starting = input('Keep as active: Y/n? \n')
    match starting:
        case 'Y':
            active = True
        case 'n':
            active = False
        case _:
            raise ValueError(f"Value: {starting} not correct.")

    description = input('Provide a description? \n')
    user = SiteInformation(username=username, website=website, password=password,
                           active=active, description=description)
    logging.info(f'Creating \n {username}')


def main():
    while True:

        engine.connect()
        create_user_key_pair()


if __name__ == '__main__':
    main()