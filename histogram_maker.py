import pandas as pd
import numpy as np
import simple_retrieval


def histograma_qtd_viagens_a_cada_meia_hora(x):
    hora_minuto = x[11:16]
    splitted = hora_minuto.split(':')
    hora = int(splitted[0])
    minuto = int(splitted[1])
    a_somar = 1 if minuto > 30 else 0
    indice_do_histograma = hora * 2 + a_somar
    return (indice_do_histograma, 1)


def slot_to_hour_mapper(slot):
    new_slot = slot

    is_second_half = False

    if slot % 2 == 1:
        is_second_half = True
        new_slot -= 1

    hour = int(new_slot / 2)
    minute = 30 if is_second_half else 0

    return str(hour).zfill(2) + ":" + str(minute).zfill(2)


vfunc = np.vectorize(lambda x: slot_to_hour_mapper(x))



if __name__ == '__main__':
    all_init_timestamps = simple_retrieval.retrieve_all_init_timestamp_by_user('011')
    my_list = list(map(lambda x: histograma_qtd_viagens_a_cada_meia_hora(x), all_init_timestamps))
    histogram_dataframe = pd.DataFrame(data=my_list, columns=['slot', 'count']).groupby('slot').agg({'count': 'sum'})

    histogram_numpy = histogram_dataframe.reset_index().as_matrix()
    time = vfunc(histogram_numpy[:, 0])
    new_histogram = np.array([time, histogram_numpy[:,1]]).transpose()

    print(new_histogram)
