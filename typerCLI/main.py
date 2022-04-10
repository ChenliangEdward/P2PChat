import typer
from mainFuncs import *

app = typer.Typer()
print("Initializing...")
mainApp = MainApp(Debug_mode=True)


@app.command()
def run():
    mainApp.run()


@app.command()
def goodbye():
    print("goodbye")


if __name__ == "__main__":
    app()
