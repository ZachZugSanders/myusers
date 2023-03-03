import logging

import pytest
from database.model import SiteInformation
from site_info.generator import generate_pass


@pytest.fixture(scope="class")
def setup_test(request):
    user = SiteInformation(
        username='man@place.com',
        website='https://test.com',
        password=generate_pass(),
        active=True,
        description='asdakjsakljdaldjasldja'
    )
    request.cls.user = user
    yield


@pytest.mark.usefixtures('setup_test')
class TestUser:

    def test_user_model(self):
        logging.info('Look MA theres stuff here!')
        assert '@' in self.user.username
        assert '.com' in self.user.website
        assert len(self.user.password) != 0
        assert self.user.active is True
        assert self.user.description is not None
