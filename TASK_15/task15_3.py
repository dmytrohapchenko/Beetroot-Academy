class TV_Controller:

    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.chosen_channel = 0

    def first_channel(self):
        self.chosen_channel = 0
        print(self.channel_list[0])

    def last_channel(self):
        self.chosen_channel = len(self.channel_list) - 1
        print(self.channel_list[-1])

    def turn_channel(self, number):
        if len(self.channel_list) > number > 1:
            self.chosen_channel = number - 1
            print(self.channel_list[self.chosen_channel])
        else:
            print('Number is out of range.')

    def next_channel(self):
        self.chosen_channel += 1
        if self.chosen_channel >= len(self.channel_list):
            self.chosen_channel = 0
            print(self.channel_list[self.chosen_channel])
        else:
            print(self.channel_list[self.chosen_channel])

    def prev_channel(self):
        self.chosen_channel -= 1
        if self.chosen_channel < 0:
            self.chosen_channel = len(self.channel_list) - 1
            print(self.channel_list[self.chosen_channel])
        else:
            print(self.channel_list[self.chosen_channel])

    def current_channel(self):
        print(f'You are currently watching channel '
              f'"{self.channel_list[self.chosen_channel]}".')

    def is_exist(self, check):
        self.check = str(check)
        if self.check.isdigit():
            if len(self.channel_list) > int(self.check) - 1 > 1:
                print(f'The channel "{int(self.check)}"'
                      f' is present in the list of channels.')
                print(f'It is "{channel_list[int(self.check)-1]}" channel.')
            else:
                print(f'You don\'t have channel "{self.check}".')
        elif self.check.lower() in [c.lower() for c in self.channel_list]:
            i = 1
            for c in self.channel_list:
                if c.lower() == self.check.lower():
                    print(f'The channel "{self.check}"'
                          f' is present in the list of channels.')
                    print(f'It is number {i}.')
                else:
                    i += 1
        else:
            print(f'You don\'t have channel "{self.check}".')


channel_list = ['BBC', 'Discovery', 'TV-1000', 'MTV', 'MKBHD', 'Jackie Chan']
tv_controller = TV_Controller(channel_list)
