import logging
import os

import pytest
from dotenv import load_dotenv

from cloudreactor_api_client import AuthenticatedClient

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s: %(message)s",
)

load_dotenv(dotenv_path=".env.test.local")


@pytest.fixture
def api_client() -> AuthenticatedClient:
    api_base_url = os.getenv("CLOUDREACTOR_API_BASE_URL", "http://localhost:8000/api/v1")
    api_key = os.getenv("CLOUDREACTOR_API_KEY")

    return AuthenticatedClient(base_url=api_base_url, token=api_key)


@pytest.fixture
def sample_run_environment_name() -> str:
    return os.getenv("CLOUDREACTOR_SAMPLE_RUN_ENVIRONMENT_NAME")


@pytest.fixture
def sample_task_name() -> str:
    return os.getenv("CLOUDREACTOR_SAMPLE_TASK_NAME")
