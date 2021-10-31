import os

from pi18n import TranslationService
from telebotify.services.http_client import HttpClient

root_path = f"{os.environ['ROOT_PATH']}"
translation_service = TranslationService(f"{root_path}/resources/i18n", os.environ.get("LOCALE", "es"))
