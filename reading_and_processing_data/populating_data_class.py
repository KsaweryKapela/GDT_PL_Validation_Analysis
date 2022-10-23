from GDT_PL_Validation_Statistics.reading_and_processing_data.questionaire_classes import GDT, IGD_20, PHQ_9, GAD_7, \
    UCLA, IGDS9_SF
from GDT_PL_Validation_Statistics.reading_and_processing_data.respondent_classes import RespondentData, GamingHabits


class Data:

    def __init__(self, dataframe):

        self.personal_data = RespondentData(dataframe)

        self.gaming_habits = GamingHabits(dataframe)

        self.GDT = GDT(dataframe)

        self.IGD_20 = IGD_20(dataframe)

        self.PHQ_9 = PHQ_9(dataframe)

        self.GAD_7 = GAD_7(dataframe)

        self.UCLA = UCLA(dataframe)

        self.IGDS9_SF = IGDS9_SF(dataframe)

        self.respondents_number = 582

    def split_column_into_sexes(self, column):
        male_data = []
        female_data = []
        for row in range(self.respondents_number):
            if self.personal_data.sex[row] == 'male':
                male_data.append(column[row])
            elif self.personal_data.sex[row] == 'female':
                female_data.append(column[row])
        return male_data, female_data

    def split_column_into_relationship_status(self, column):
        in_relationship = []
        not_in_relationship = []
        for row in range(self.respondents_number):
            if self.personal_data.relationship[row] is True:
                in_relationship.append(column[row])
            elif not self.personal_data.relationship[row]:
                not_in_relationship.append(column[row])
        return in_relationship, not_in_relationship

    def split_column_into_online_gaming(self, column):
        online_gamers = []
        offline_gamers = []

        for row in range(self.respondents_number):
            if self.gaming_habits.play_online[row] is True:
                online_gamers.append(column[row])

            elif not self.gaming_habits.play_online[row]:
                offline_gamers.append(column[row])

        return online_gamers, offline_gamers
