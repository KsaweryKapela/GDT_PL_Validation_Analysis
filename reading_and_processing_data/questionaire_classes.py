import pandas as pd


class QuestionnaireResults:
    
    def scores(self):
        scores = []
        for index in range(582):
            score = 0
            for column in vars(self).values():
                if pd.isna(column[index]):
                    score = column[index]
                    break
                else:
                    score += column[index]
            scores.append(score)
        return scores


class GDT(QuestionnaireResults):
    def __init__(self, dataframe):
        self.q_1 = dataframe['QID1_1']
        self.q_2 = dataframe['QID1_2']
        self.q_3 = dataframe['QID1_3']
        self.q_4 = dataframe['QID1_4']


class IGD_20(QuestionnaireResults):
    def __init__(self, dataframe):
        self.q_1 = dataframe['Q33_1']
        self.q_2 = dataframe['Q33_2']
        self.q_3 = dataframe['Q33_3']
        self.q_4 = dataframe['Q33_4']
        self.q_5 = dataframe['Q33_5']
        self.q_6 = dataframe['Q33_6']
        self.q_7 = dataframe['Q33_7']
        self.q_8 = dataframe['Q33_8']
        self.q_9 = dataframe['Q33_9']
        self.q_10 = dataframe['Q33_10']
        self.q_11 = dataframe['Q33_11']
        self.q_12 = dataframe['Q33_12']
        self.q_13 = dataframe['Q33_13']
        self.q_14 = dataframe['Q33_14']
        self.q_15 = dataframe['Q33_15']
        self.q_16 = dataframe['Q33_16']
        self.q_17 = dataframe['Q33_17']
        self.q_18 = dataframe['Q33_18']
        self.q_19 = dataframe['Q33_19']
        self.q_20 = dataframe['Q33_20']


class PHQ_9(QuestionnaireResults):
    def __init__(self, dataframe):
        self.q_1 = dataframe['PHQ_9_1']
        self.q_2 = dataframe['PHQ_9_2']
        self.q_3 = dataframe['PHQ_9_3']
        self.q_4 = dataframe['PHQ_9_4']
        self.q_5 = dataframe['PHQ_9_5']
        self.q_6 = dataframe['PHQ_9_6']
        self.q_7 = dataframe['PHQ_9_7']
        self.q_8 = dataframe['PHQ_9_8']


class GAD_7(QuestionnaireResults):
    def __init__(self, dataframe):
        self.q_1 = dataframe['GAD_7_1']
        self.q_2 = dataframe['GAD_7_2']
        self.q_3 = dataframe['GAD_7_3']
        self.q_4 = dataframe['GAD_7_4']
        self.q_5 = dataframe['GAD_7_5']
        self.q_6 = dataframe['GAD_7_6']
        self.q_7 = dataframe['GAD_7_7']


class UCLA(QuestionnaireResults):
    def __init__(self, dataframe):
        self.q_1 = dataframe['Q27_1']
        self.q_2 = dataframe['Q27_2']
        self.q_3 = dataframe['Q27_3']


class IGDS9_SF(QuestionnaireResults):
    def __init__(self, dataframe):
        self.q_1 = dataframe['Q211_1']
        self.q_2 = dataframe['Q211_2']
        self.q_3 = dataframe['Q211_3']
        self.q_4 = dataframe['Q211_4']
        self.q_5 = dataframe['Q211_5']
        self.q_6 = dataframe['Q211_6']
        self.q_7 = dataframe['Q211_7']
        self.q_8 = dataframe['Q211_8']
        self.q_9 = dataframe['Q211_9']
