import os

from mediagoblin.app import MediaGoblinApp
from configobj import ConfigObj


CONFIG_FILE_PATH = "mediagoblin.ini"

database_url = os.environ.get("DATABASE_URL", False)

if database_url:
    parser = ConfigObj(CONFIG_FILE_PATH)
    parser["mediagoblin"]["sql_engine"] = database_url
    parser.write(open(CONFIG_FILE_PATH, "w"))

os.system("gmg dbupdate")

app = MediaGoblinApp(CONFIG_FILE_PATH)
