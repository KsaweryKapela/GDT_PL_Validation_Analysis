from GDT_PL_Validation_Statistics.reading_and_processing_data.questionaire_classes import GDT, IGD_20, PHQ_9, GAD_7, \
    UCLA, IGDS9_SF


class Data:

    def __init__(self, dataframe):

        self.personal_data = None

        self.gaming_habits = None

        self.GDT = GDT(dataframe)

        self.IGD_20 = IGD_20(dataframe)

        self.PHQ_9 = PHQ_9(dataframe)

        self.GAD_7 = GAD_7(dataframe)

        self.UCLA = UCLA(dataframe)

        self.IGDS9_SF = IGDS9_SF(dataframe)

