"""Main class file for the server"""
import time
import win32serviceutil
import socket


class Server:
    """Server Class for the WCR_Service application"""
    wcr_services = ['WebCenter_CADX', 'WebCenter_JBOSS', 'WebCenter_Tomcat','BGMD']

    def __init__(self):
        self.WAIT = 30
        self.machine = socket.gethostname()

    def start_service(self, service):
        try:
            if win32serviceutil.QueryServiceStatus(service):
                print(f'starting-{service}')
                win32serviceutil.StartService(service, self.machine)
                time.sleep(self.WAIT)
                if self.service_running(service):
                    print(f'{service} has started')
                else:
                    return f'something went wrong or still starting up'
            else:
                return f'{service} is not installed'
        except Exception as e:
            return f'something went wrong- {e}'

    def stop_service(self, service):
        try:
            if win32serviceutil.QueryServiceStatus(service):
                print(f'stopping-{service}')
                win32serviceutil.StopService(service, self.machine)
                time.sleep(self.WAIT)
                if not self.service_running(service):
                    print(f'{service} has stopped')
                else:
                    return f'something went wrong'
            else:
                return f'{service} is not installed'
        except Exception as e:
            return f'something went wrong- {e}'


    def restart_service(self, service):
        try:
            if win32serviceutil.QueryServiceStatus(service):
                print(f'Restarting-{service}')
                win32serviceutil.RestartService(service, self.machine)
                time.sleep(self.WAIT)
                if self.service_running(service):
                    print(f'{service} has restarted')
                else:
                    self.start_service(service)
                    return f'something went wrong or still starting up trying to start again'
            else:
                return f'{service} is not installed'
            print(f'Restarting-{service}')
            win32serviceutil.RestartService(service, self.machine)
            time.sleep(self.WAIT)
            if self.service_running(service):
                print(f'{service} has restarted')
            else:
                self.start_service(service)
                return f'something went wrong or still starting up trying to start again'
        except Exception as e:
            return f'something went wrong- {e}'

    # def service_running(self):
    #     return win32serviceutil.QueryServiceStatus(self.service, self.machine)[1] == 4
    #
    # try:
    #     win32serviceutil.QueryServiceStatus('myservice')
    # except:
    #     print
    #     "Windows service NOT installed"
    # else:
    #     print
    #     "Windows service installed"


def main():
    wcr = Server()
    wcr_services = ['WebCenter_CADX', 'WebCenter_Tomcat', 'WebCenter_JBOSS']
    for i in wcr_services:
        wcr.start_service(i)


if __name__ == '__main__':
    main()
