class Alarm_clock:
    def __init__(self, time):
        self.current_time = time
        self.alarm_on = False
        self.alarm_time = ''
    def get_time(self):
        print('The current time is: ', self.current_time)
    def set_time(self):
        self.current_time = input('Enter the current time: ')
        print('The current time is: ', self.current_time)
    def set_alarm(self):
        user_input = input('Do you want to turn the alarm on or off: ')
        if user_input == 'on':
            self.alarm_on = True
        else:
            self.alarm_on = False
    def get_alarm_status(self):
        if self.alarm_on == True:
            print('The alarm is turned on')
        elif self.alarm_on == False:
            print('The alarm is turned off')
    def set_alarm_time(self):
        self.alarm_time - input('Enter the alarm time: ')
        print('The current alarm time is set at: ', self.alarm_time)
