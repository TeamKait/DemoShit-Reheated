import asyncio
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from dotenv import load_dotenv
from qasync import QEventLoop
from tortoise import Tortoise
from app.db.service import connect_db
from app.windows.mainwindow import Ui_MainWindow


async def main() -> None:
    load_dotenv()
    await connect_db()

    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    last_window_closed = asyncio.Event()

    app = QApplication.instance()
    if app:
        app.lastWindowClosed.connect(lambda: last_window_closed.set())

    await last_window_closed.wait()
    await Tortoise.close_connections()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    with loop:
        loop.run_until_complete(main())
