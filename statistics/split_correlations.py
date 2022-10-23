from GDT_PL_Validation_Statistics.statistics.statistics import r_pearson, spearman


def split_correlations_func(stat_class_instance, split_method, column_1, column_2):
    split_method(stat_class_instance, column_1, column_2)


def split_into_sex_data(stat_class_instance, column_1, column_2):
    male_data, female_data = stat_class_instance.split_column_into_sexes(column_1)
    male_data_2, female_data_2 = stat_class_instance.split_column_into_sexes(column_2)

    print('Male data:')
    r_pearson(male_data, male_data_2)
    spearman(male_data, male_data_2)
    print('\nFemale data:')
    r_pearson(female_data, female_data_2)
    spearman(female_data, female_data_2)
    print('\n')


def split_into_relationship_data(stat_class_instance, column_1, column_2):
    in_relationship, single = stat_class_instance.split_column_into_relationship_status(column_1)
    in_relationship_2, single_2 = stat_class_instance.split_column_into_relationship_status(column_2)

    print('In relationship data:')
    r_pearson(in_relationship, in_relationship_2)
    spearman(in_relationship, in_relationship_2)
    print('\nSingle data:')
    r_pearson(single, single_2)
    spearman(single, single_2)
    print('\n')


def split_into_online(stat_class_instance, column_1, column_2):
    online, offline = stat_class_instance.split_column_into_online_gaming(column_1)
    online_2, offline_2 = stat_class_instance.split_columns_into_online_gaming(column_2)

    print('Online players:')
    r_pearson(online, online_2)
    spearman(online, online_2)
    print('\nOffline players::')
    r_pearson(offline, offline_2)
    spearman(offline, offline_2)
    print('\n')
