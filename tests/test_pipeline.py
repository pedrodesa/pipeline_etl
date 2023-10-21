import pandas as pd

def testar_a_concatenacao_da_lista_de_dataframe():
    ''' Use o arrange act e assert para testar a função contact_data_frames '''
    
    # arrange
    data_frame_list = [df_1, df_2]
    data_frame = concat(data_frame_list, ignore_index = True)

    # act
    df = contact_data_frames(data_frame_list)

    # assert
    assert df.shape == (4, 2)
    assert data_frame.equals(df)