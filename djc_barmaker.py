# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 23:34:58 2021
@author: sl1mc
"""
import os
import sys
import pandas as pd
from csv import reader
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import csv
import time
import datetime
import matplotlib.pyplot as plt
import itertools

def conv_csv(filename_txt, filename_csv):
    df = pd.read_csv(filename_txt, sep=',')
    #df = df.replace({'"':''}, regex=True)
    df.to_csv(filename_csv, index=False)


def do_calc(path, output_name):
    sq_correct = 0
    sq_incorrect = 0
    sq_hint = 0
    correct = 0
    incorrect =0
    hint = 0
    exp_dir = 0
    next_page = 0
    prev_page = 0
    m_back = 0
    
    sq_crrect_l = []
    sq_incorrect_l = []
    sq_hint_l = []
    correct_l = []
    incorrect_l = []
    hint_l = []
    exp_dir_l = []
    next_page_l = []
    prev_page_l = []
    m_back_l = []
    m_forward_l = []
    
    m_forward = 0
    time_list = []
    
    shade_region = []
    switcher = 0
    
    color_regions = []
    with open(path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        i = 0
        
        for row in csv_reader:
            if len(row) == 0:
                continue
            if(i == 1):
                init_time = row[3]
                #print(row, init_time)
                #date_time_obj = datetime.datetime.strptime(init_time, '%m/%d/%Y %H:%M')
                date_time_obj = datetime.datetime.strptime(init_time, '%Y-%m-%d %H:%M:%S')
                init_time = date_time_obj.timestamp()
                #print(init_time)
            else:
                if(row[3] != None):
                    #print(row[3])
                    try:
                        #date_time_obj = datetime.datetime.strptime(row[3], '%m/%d/%Y %H:%M')
                        date_time_obj = datetime.datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                        new_time = date_time_obj.timestamp()
                        time_list.append(new_time-init_time)
                        shade_region.append(switcher)
                        
                        #print(1)
                    except:
                        print('Wrong format')
            
            #print(str(' '.join(row)))
            if('Skill' in str(' '.join(row)) and ('incorrect' in str(' '.join(row)) or 'Incorrect' in str(' '.join(row)))):# or 'incorrect' in row[5] or 'Incorrect' in row[5] or 'incorrect' in row[5] or 'Incorrect' in row[5]):
                sq_incorrect +=1                
            elif('incorrect' in str(' '.join(row)) or 'Incorrect' in str(' '.join(row))):# or 'incorrect' in row[5] or 'Incorrect' in row[5] or 'incorrect' in row[5] or 'Incorrect' in row[5]):
                incorrect +=1
                #print('inc')
                
            if('Skill' in str(' '.join(row)) and (' correct' in str(' '.join(row)) or ' Correct' in str(' '.join(row)))):# or 'correct' in row[5] or 'Correct' in row[5] or 'correct' in row[5] or 'Correct' in row[5]):
                sq_correct += 1
            if('Skill' not in str(' '.join(row)) and 'incorrect' not in str(' '.join(row)) and ('correct' in str(' '.join(row)))):
                correct += 1
                #print('cor')
            if(('Skill' in str(' '.join(row)) or ('skill' in str(' '.join(row)))) and('hint' in str(' '.join(row)) or 'Hint' in str(' '.join(row)))):# or 'hint' in row[5] or 'Hint' in row[5] or 'hint' in row[5] or 'Hint' in row[5]):
                sq_hint +=1
            elif('hint' in str(' '.join(row)) or 'Hint' in str(' '.join(row))):# or 'hint' in row[5] or 'Hint' in row[5] or 'hint' in row[5] or 'Hint' in row[5]):
                hint +=1
                #print('h')
            if('experimenter direction' in str(' '.join(row))):
                exp_dir += 1
                #print('ed dir')
            if('next' in str(' '.join(row)) and 'page' in str(' '.join(row))):
                next_page += 1
                #print('next')
            if('previous' in str(' '.join(row)) and 'page' in str(' '.join(row))):
                prev_page += 1
                #print('prev')
            if('Moved back' in str(' '.join(row))):
                m_back += 1
                #print(row)
            if('Moved forward' in str(' '.join(row))):  #here we see if we should reset
                m_forward += 1
                sq_crrect_l.append(sq_correct)
                sq_incorrect_l.append(sq_incorrect)
                sq_hint_l.append(sq_hint)
                correct_l.append(correct)
                incorrect_l.append(incorrect)
                hint_l.append(hint)
                exp_dir_l.append(exp_dir)
                next_page_l.append(next_page)
                prev_page_l.append(prev_page)
                m_back_l.append(m_back)
                m_forward_l.append(m_forward)
                correct = 0
                incorrect =0
                hint = 0
                exp_dir = 0
                next_page = 0
                prev_page = 0
                m_back = 0
                m_forward = 0
                if(switcher == 0):
                    switcher = 1
                else:
                    switcher = 0
                color_regions.append(i)
                #print(row)
            i += 1
            
    print('skill quiz incorrect')
    print(sq_incorrect)
    print('skill quiz correct')
    print(sq_correct)
    print('skill quiz hint')
    print(sq_hint)
    print('incorrect')
    print(incorrect)
    print('correct')
    print(correct)
    print('hint')
    print(hint)
    print('exp_dir') #kill this
    print(exp_dir)
    print('next_page')
    print(next_page)
    print('prev_page')
    print(prev_page)
    print('m_forward')
    print(m_forward)
    print('m_back')
    print(m_back)
    sq_crrect_l.append(sq_correct)
    sq_incorrect_l.append(sq_incorrect)
    sq_hint_l.append(sq_hint)
    correct_l.append(correct)
    incorrect_l.append(incorrect)
    hint_l.append(hint)
    exp_dir_l.append(exp_dir)
    next_page_l.append(next_page)
    prev_page_l.append(prev_page)
    m_back_l.append(m_back)
    m_forward_l.append(m_forward)
    #REPEATED QUESTIONS: supress trailing logs except those that are different
    #dont allow two hints in a row
    print("1")
    df_data = pd.DataFrame({'skill quiz incorrect':sq_incorrect,'skill quiz correct':sq_correct,'prev_page':prev_page,'next_page':next_page,'skill quiz hint':sq_hint,'incorrect':incorrect,'correct':correct,'hint':hint,'m_forward':m_forward,'m_back':[m_back]})
    fileTitle = "results_by_mod"
    results_to_csv = os.path.join(output_name, f"{fileTitle}.csv")
    print(results_to_csv)
    #df_data.to_csv('/Users/mitchellkolb/Downloads/GSUR/Codebase/People/results_by_mod.csv', index=False)
    df_data.to_csv(results_to_csv, index=False)
    
    data = [sq_incorrect, sq_correct, sq_hint,incorrect,correct, hint, next_page, prev_page]
    #print("Data is:", data)
    #data = [incorrect_l,correct_l, hint_l, exp_dir_l, next_page_l, prev_page_l, m_forward_l, m_back_l]
    labels = ['SQ Incorrect','SQ Correct', 'SQ Hint','Incorrect','Correct', 'Hint', 'Next_page', 'Prev_page']
    plt.xticks(range(len(data)), labels, rotation=45)
    plt.xlabel('Activities')
    plt.ylabel('Number of occurences')
    plt.title('Tracking data for Participant')
    jj = 0
    past = [0,0,0,0,0,0,0,0]
    #print("Correct l is", correct_l)
    while jj < len(correct_l):
        #print(incorrect_l[jj],correct_l[jj], hint_l[jj], exp_dir_l[jj], next_page_l[jj], prev_page_l[jj], m_forward_l[jj], m_back_l[jj])
        data = [sq_incorrect_l[jj],sq_crrect_l[jj], sq_hint_l[jj],incorrect_l[jj],correct_l[jj], hint_l[jj], next_page_l[jj], prev_page_l[jj]]
        
        plt.bar(range(len(data)), data, label="Module "+str(jj+1), bottom=past) 
        past = [sum(i) for i in zip(past, data)] 
        jj +=1
    
    plt.legend()
    plt.show()
    plt.savefig('sample_bar.png')
    plt.clf()
    kk = 1
    clip_t = 0
    cutoff = 30
    while kk < len(time_list):
        temp = time_list[kk] - time_list[kk-1]
        if(temp > cutoff):
            time_list[kk] = time_list[kk-1] + cutoff
            clip_t += 1
        kk += 1
    plt_cols = ['red', 'green', 'blue', 'yellow', 'purple', 'red', 'green', 'blue', 'yellow']    
    plt.plot(time_list) 
    ll = 1
    while ll < len(color_regions):
        plt.axvspan(color_regions[ll-1], color_regions[ll], color=plt_cols[ll], alpha=0.5)
        ll+=1
    plt.title("Time taken throughout usage; clipped " + str(clip_t) + " times")
    plt.xlabel("Recorded Events")
    plt.ylabel('Seconds')
    plt.savefig('Charted_time.png')
    hours, remainder = divmod(time_list[-1]-time_list[0], 3600)
    minutes, seconds = divmod(remainder, 60)
    print("Time taken throughout usage; clipped " + str(clip_t) + " times: " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds)  + " seconds")
    df_data['Hours'] = [hours]

    df_data['Minutes'] = [minutes]

    df_data['Seconds'] = [seconds]

    df_data.to_csv(str(output_name)+'FinalResults.csv', index=False)
        
    #print(score_list)


def DJC_download_file():
    """ Code to download a file from the web backend using login admin. You will need to replace "pwd" with
    the admin password. You may want to rename downloaded_file.txt as needed.
    Note you will probably need to install the requests Python module on your machine.
    """
    import requests
    from requests.auth import HTTPBasicAuth

    # URL of the remote file you want to download
    file_url = "https://emma-back.mse.psych.wsu.edu/login"

    # Local file path where you want to save the downloaded file
    local_file_path = "/Users/mitchellkolb/Downloads/GSUR/Codebase/People/"

    username = 'mitchellk1'
    password = 'mitchellk1'

    try:
        # Send an HTTP GET request to the remote URL with authentication
        response = requests.get(file_url, auth=HTTPBasicAuth(username, password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the local file for writing in binary mode
            with open(local_file_path, 'wb') as local_file:
                # Write the content of the remote file to the local file
                local_file.write(response.content)
            print(f"File downloaded and saved as {local_file_path}")
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")


def DJC_create_bar_chart(df):
    """ 
    Create a bar chart using data in df. Save the resulting chart in file "barchart.png".
    Here, the x axis uses dataframe column 'category' and the y axis is new_column.
    """ 
    df.plot(x='category', y='new_column', kind='bar', color='skyblue', legend=False)
    plt.xlabel('Categories')
    plt.ylabel('New Values')
    plt.title('Bar Chart Example')
    plt.savefig("barchart.png", bbox_inches="tight")


def DJC_python_code(df):
    """ 
    You mentioned running Python code which produces a barchart and an output of excel columns
    with calculated data.  Speicifically, you mentioned wanting to add columns with values calculated from
    the original csv file. Here is one possible way to do this. I read in the original csv file
    (filename) and store it in a Pandas dataframe. I introduce column new_val_1, whose
    values are the result of a  sample calculation (in this case, double the value found in old_column.
    A bar chart is created of the dataframe and the expanded dataframe is returned.
    """
    df = pd.read_csv(filename1, delimiter=',')
    df['new_column'] = df['old_column'].apply(lambda x: x * 2)
    DJC_create_bar_chart(df)
    return df



def DJC_code(filename):
    """ Assume that ptid_num and skills_quiz_num are supplied (or automatically identified
    from the EMMA website). Using this information and the original "filename", a new filename is created 
    in the format filename_ptid_num_skills_quiz_num.
    """
    ptid_num = "001"   # PtID number of downloaded file
    skills_quiz_num = "002"  # Skills Quiz number found in the .txt file
    new_filename = filename + "_" + ptid_num + "_" + skills_quiz_num

    df = DJC_python_code(df)
    df.to_csv(new_filename, delimiter=',')

   
if(__name__ == "__main__"):
    '''
    Place the file you want to verify in './people', and write its name in "filename"
    '''
    filename1="ABtest1_2023-02-01 12:51:21"
    filename2="ARtest1_2023-01-31 16:35:10"
    filename3="ARtest1_2023-01-31 16:37:22"
    filename4="ARtest1_2023-01-31 16:46:39"
    filename5="ARtest1_2023-01-31 16:48:13"
    
    #DJC_code(filename)

    rawDataFilePath = "/Users/mitchellkolb/Downloads/GSUR/People/"+filename5+".txt"
    outputFilePath = "/Users/mitchellkolb/Downloads/GSUR/Results/"
    outputFile = "/Users/mitchellkolb/Downloads/GSUR/Results/FinalResults.csv"

    # Get the current working directory (where the script is located)
    current_directory = os.path.dirname(os.path.realpath(__file__))
    print("Current directory:", current_directory)
    # Checks/creates a the People folder in this directory.
    dir_path = current_directory + "/Results"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print("Results folder already exists")

    do_calc(rawDataFilePath, outputFilePath)

