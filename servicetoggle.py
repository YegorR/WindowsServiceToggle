SERVICE_NAME = "postgresql-x64-12"

import win32service

STATUS_DICT = { 0: "Error",
                1: "The service is not running",
                2: "The service is starting",
                3: "The service is stopping",
                4: "The service is running",
                5: "The service continue is pending",
                6: "The service pause is pending",
                7: "The service is paused"}

def PrintGreeting():
    print()
    print("**************************************************************")
    print()
    print("PostgresToggle - the utility for PostgreSQL service management")
    print()
    print("**************************************************************")
    print()

def GetServiceHandler(serviceName):
    scManager = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS)
    serviceHandler = win32service.OpenService(scManager, serviceName, win32service.SC_MANAGER_ALL_ACCESS)
    win32service.CloseServiceHandle(scManager)
    return serviceHandler

def CloseServiceHandler(serviceHandler):
    win32service.CloseServiceHandle(serviceHandler)

def GetServiceStatus(serviceHandler):
    statusObject = win32service.QueryServiceStatus(serviceHandler)
    return statusObject[1]

def StartService(serviceHandler):
    win32service.StartService(serviceHandler, [])

def StopService(serviceHandler):
    statusObject = win32service.ControlService(serviceHandler, 1)
    return statusObject[1]

def PrintTextServiceStatus(textStatus):
    print("Status of service \"" + SERVICE_NAME + "\" is: ", end = "")
    print(textStatus)

def PrintHelpMessage():
    print("Available commands:")
    print("start - start the service")
    print("stop - stop the service")
    print("help - get help")
    print("status - get status of the service")
    print("exit - close the program")

if __name__ == "__main__":
    PrintGreeting()
    inputMessage = ""
    while (inputMessage != "exit"):
        serviceHandler = GetServiceHandler(SERVICE_NAME)
        serviceStatus = GetServiceStatus(serviceHandler)
        PrintTextServiceStatus(STATUS_DICT[serviceStatus])
        print(">>> ", end = "")
        inputMessage = input().strip().lower()
        if (inputMessage == "start"):
            StartService(serviceHandler)
        elif (inputMessage == "stop"):
            StopService(serviceHandler)
        elif (inputMessage == "status"):
            pass
        elif (inputMessage == "exit"):
            pass
        elif (inputMessage == "help"):
            PrintHelpMessage()
        else:
            print("Unknown command. Please try again.")
        CloseServiceHandler(serviceHandler)
    print ("Bye-bye!")
