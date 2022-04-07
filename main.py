from mainFunc import MainApp

if __name__ == '__main__':
    mainApp = MainApp(Debug_mode=True)
    mainApp.run()
    while True:
        mainApp.send("192.168.56.1", 5050)
