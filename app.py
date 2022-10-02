from flask_script import Manager, Shell

from applications import app, db

manager = Manager(app)


# эти переменные доступны внутри оболочки без явного импорта
def main():
    return dict(app=app, db=db)


manager.add_command('shell', Shell(make_context=main))

if __name__ == '__main__':
    manager.run()
