

import my_methods_csv as mm
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    path_raw_read = r"D:\DOC_2023\Ad_Reports\ad_jul_23\yearly_database_ad"
    path_read = mm.path_edit(path_raw_read)
    dir_list =  mm.os.listdir(path_read)

    path_raw_write = r"D:\DOC_2023\Ad_Reports\ad_jul_23\yearly_database_ad"
    path_write = mm.path_edit(path_raw_write)

    tag = "_meta.csv"

    start_date = 20230101
    end_date = 20230731

    l_file = []
    
    l_shera = []
    l_tukhor = []
    l_medha = []
    l_tota = []
    l_quizgiri = []
    l_quizee = []
    l_jeeto = []
    l_quizchamp = []
    l_tetris = []
    l_npuzzle = []
    l_gotham = []
    l_surfing = []
    l_panda = []
    l_space = []
    l_rise = []
    l_runner = []
    l_ninja = []
    l_pong = []
    l_samurai = []


    for x in dir_list:
        if tag in x:
            a = path_read + "//" + x
            l_file.append([a])

    #print(l_file)
    
    for f in range(len(l_file)):
        
        src = l_file[f][0]
        data = mm.read_data(src)
        
        for row in range(1,len(data)):
            
            reporting_starts = data[row][0]
            date_value = mm.date_num(reporting_starts) # man.
            reporting_ends = data[row][1]
            date_value_2 = mm.date_num(reporting_ends) # man.
            
            ad_name = data[row][2]
            ad_delivery = data[row][3]
            ad_set_name = data[row][4]
            ad = (ad_name + ad_set_name).lower()
            
            bid = data[row][5]
            bid_type = data[row][6]
            ad_set_budget = data[row][7]
            ad_set_budget_type = data[row][8]
            last_significant_edit = data[row][9]
            attribution_setting = data[row][10]
            
            results = data[row][11]
            result = results #man.
            result_indicator = data[row][12]
            reach = data[row][13]
            impressions = data[row][14]
            
            cost_per_results = data[row][15]
            quality_ranking = data[row][16]
            engagement_rate_ranking = data[row][17]
            conversion_rate_ranking = data[row][18]
            amount_spent_bdt = data[row][19]
            cost = amount_spent_bdt #man.
            ends = data[row][20]
            

            if (date_value >= start_date and date_value <= end_date) and "shera" in ad:
                l_shera.append([cost])

            if (date_value >= start_date and date_value <= end_date) and ( "tukhor" in ad or "tukhr" in ad ):
                l_tukhor.append([cost])
    
            if (date_value >= start_date and date_value <= end_date) and "medha" in ad:
                l_medha.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "tota" in ad:
                l_tota.append([cost])

            if (date_value >= start_date and date_value <= end_date) and ("quizgiri" in ad or "qg" in ad ):
                l_quizgiri.append([cost])
                
            if (date_value >= start_date and date_value <= end_date) and ( "quizee" in ad or "quize" in ad ):
                l_quizee.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "jeeto" in ad:
                l_jeeto.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "quizchamp" in ad:
                l_quizchamp.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "tetris" in ad:
                l_tetris.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "npuzzle" in ad:
                l_npuzzle.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "gotham" in ad:
                l_gotham.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "surfing" in ad:
                l_surfing.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "panda" in ad:
                l_panda.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "space" in ad:
                l_space.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "rise" in ad:
                l_rise.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "runner" in ad:
                l_runner.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "ninja" in ad:
                l_ninja.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "pong" in ad:
                l_pong.append([cost])

            if (date_value >= start_date and date_value <= end_date) and "samurai" in ad:
                l_samurai.append([cost])

    
    shera = mm.sum_list_array_n(l_shera,0)
    tukhor = mm.sum_list_array_n(l_tukhor,0)
    medha = mm.sum_list_array_n(l_medha,0)
    tota = mm.sum_list_array_n(l_tota,0)
    quizgiri = mm.sum_list_array_n(l_quizgiri,0)
    quizee = mm.sum_list_array_n(l_quizee,0)
    jeeto = mm.sum_list_array_n(l_jeeto,0)
    quizchamp = mm.sum_list_array_n(l_quizchamp,0)
    tetris = mm.sum_list_array_n(l_tetris,0)
    npuzzle = mm.sum_list_array_n(l_npuzzle,0)
    gotham = mm.sum_list_array_n(l_gotham,0)
    surfing = mm.sum_list_array_n(l_surfing,0)
    panda = mm.sum_list_array_n(l_panda,0)
    space = mm.sum_list_array_n(l_space,0)
    rise = mm.sum_list_array_n(l_rise,0)
    runner = mm.sum_list_array_n(l_runner,0)
    ninja = mm.sum_list_array_n(l_ninja,0)
    pong = mm.sum_list_array_n(l_pong,0)
    samurai = mm.sum_list_array_n(l_samurai,0)

    x = np.array([ "Shera","Tukhor","Medha","Tota","Quizgiri","Quizee","Jeeto","Quizchamp","Tetris","Npuzzle","Gotham","Surfing","Panda","Space","Rise","Runner","Ninja","Pong","Samurai" ])
    y = np.array([ shera,tukhor,medha,tota,quizgiri,quizee,jeeto,quizchamp,tetris,npuzzle,gotham,surfing,panda,space,rise,runner,ninja,pong,samurai ])

    xx = [ "Shera","Tukhor","Medha","Tota","Quizgiri","Quizee","Jeeto","Quizchamp","Tetris","Npuzzle","Gotham","Surfing","Panda","Space","Rise","Runner","Ninja","Pong","Samurai" ]
    mxp = [0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    mycolors = ["black", "hotpink", "b", "#4CAF50"]
    
    plt.bar(x,y)
    #plt.scatter(x, y)
    #plt.plot(xpoints, ypoints, 'o')
    #plt.plot(ypoints, linestyle = 'dotted')
    #plt.plot(ypoints, color = 'r')
    #plt.hist(x)
    #plt.pie(y, labels = xx, autopct = '%1.1f%%', explode = mxp, shadow = False)
    
    plt.title("Cost Trends")
    plt.xlabel("Services")
    plt.ylabel("Costs")
    #plt.legend(title = "Services:", loc = 0, bbox_to_anchor=(-0.2,0.9), fontsize = 10)
    #plt.legend(title = "Services:", loc = 0)
    
    plt.xticks(rotation = 55)
    #plt.grid()
    ##plt.subplot(1, 2, 1)
    plt.show()

##    w_file = "x.csv"
##    w_path = path_write + "//" + w_file
##    mm.write_list( w_path, l_write)


