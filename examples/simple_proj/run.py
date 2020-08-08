import os
import sys
from pathlib import Path

from chaban.core.telegram_bot import TelegramBot


def run():
    os.environ["CHABAN_SETTINGS_MODULE"] = "settings"

    root_path = Path(__file__).parent
    sys.path.append(root_path / "simple_proj")

    # debugging purposes ...
    tbot = TelegramBot()

    for d in tbot.start_polling():
        print(d)


if __name__ == "__main__":
    run()
