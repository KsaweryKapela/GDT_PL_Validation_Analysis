class RespondentData:
    def __init__(self, dataframe):
        self.data = dataframe
        self.sex = self.data['Q37']  # 1 = female, 2 = male
        self.age = [int(item) for item in self.data['Q6']]
        self.relationship = self.data['Q10']  # 1 = True, 2 = False
        # self.city = self.return_city()


class GamingHabits:
    def __init__(self, dataframe):
        self.weekly_hours = dataframe['Q8']
        self.session_time = dataframe['Q12']
        self.play_online = [True if item == 1 else False for item in dataframe['Q9']]
        self.harmful_gaming = [False if item == 2 else True for item in dataframe['Q18']]
        self.respondents_addiction = dataframe['Q36_1']
        self.friends_addiction = dataframe['Q36_2']

        self.RPG = [True if item == 1 else False for item in dataframe['Q10_1']]
        self.MMORPG = [True if item == 1 else False for item in dataframe['Q10_2']]
        self.FPS = [True if item == 1 else False for item in dataframe['Q10_3']]
        self.simulators = [True if item == 1 else False for item in dataframe['Q10_4']]
        self.arcade = [True if item == 1 else False for item in dataframe['Q10_5']]
        self.strategic = [True if item == 1 else False for item in dataframe['Q10_6']]
        self.educational = [True if item == 1 else False for item in dataframe['Q10_7']]
        self.sport = [True if item == 1 else False for item in dataframe['Q10_8']]
        self.racing = [True if item == 1 else False for item in dataframe['Q10_9']]
        self.MOBA = [True if item == 1 else False for item in dataframe['Q10_10']]

        self.PC = [True if item == 1 else False for item in dataframe['Q14_1']]
        self.phone = [True if item == 1 else False for item in dataframe['Q14_2']]
        self.console = [True if item == 1 else False for item in dataframe['Q14_3']]
        self.VR = [True if item == 1 else False for item in dataframe['Q14_4']]
