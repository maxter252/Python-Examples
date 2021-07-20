import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--namespace", action="store", default="dev", help="namespace used"
    )


@pytest.fixture(scope="session")
def setup():
    print("RUNNING SETUP")
    yield
    print("RUNNING TEARDOWN")
