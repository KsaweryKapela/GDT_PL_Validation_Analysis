def GDT_dict(data):
    print('\nAll')
    gdt_dict = {'Q_1': data.GDT.q_1,
                'Q_2': data.GDT.q_2,
                'Q_3': data.GDT.q_3,
                'Q_4': data.GDT.q_4
                }
    return gdt_dict


def GDT_female_dict(data):
    print('\nFemales')
    gdt_dict = {'Q_1': data.split_column_into_sexes(data.GDT.q_1)[1],
                'Q_2': data.split_column_into_sexes(data.GDT.q_2)[1],
                'Q_3': data.split_column_into_sexes(data.GDT.q_3)[1],
                'Q_4': data.split_column_into_sexes(data.GDT.q_4)[1],
                }
    return gdt_dict


def GDT_male_dict(data):
    print('\nMales')
    gdt_dict = {'Q_1': data.split_column_into_sexes(data.GDT.q_1)[0],
                'Q_2': data.split_column_into_sexes(data.GDT.q_2)[0],
                'Q_3': data.split_column_into_sexes(data.GDT.q_3)[0],
                'Q_4': data.split_column_into_sexes(data.GDT.q_4)[0],
                }

    return gdt_dict
