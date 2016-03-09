#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import datetime
import os

activity_store = os.path.dirname(os.path.abspath(__file__))+"/activities/activity_store.work"

class FileHandler(object):
    """FileHandler class
    Manages storage in a file.
    
    """
    def __init__(self, output_file):
        """
        The output directory should be given.
        
        :param output_dir: output directory path
        
        """
        self.output_file = output_file
        
    def append_list(self, element_list):
        pass
        
    def append_element(self, element):
        data_store_file = open( (self.output_file), "r")
        try:
            data_buffer = json.load(data_store_file)
        except ValueError: 
            data_buffer = {}
        data_store_file.close()
        if("elements" not in data_buffer.keys()):
            data_buffer["elements"]=[]
        data_buffer["elements"].append(element)
        data_store_file = open((self.output_file), "w+")
        json.dump(data_buffer, data_store_file)
        data_store_file.close()
        
    def clear_file(self):
        pass
        
    def show_activities(self):
        pass
        
class Workomat(object):
    """
    """
    def __init__(self, output_file = activity_store):
        self.output_file = output_file
        self.file_handler = FileHandler(self.output_file)
    def append(self, aname, whours, stime, adate):
        print "[.] Appending activity : ", aname," - ", whours," - ", stime," - ", adate, "..."
        adict = {}
        adict["name"]=aname
        adict["work hours"]=whours
        adict["start time"]=stime
        adict["date"]=adate
        self.file_handler.append_element(adict)
        print "[¤] Successfully appended activity."
        
    def run(self):
        activity = raw_input("[*] Enter activity, e.g. '>lab work; 2h; 10:00' :\n>").strip().split(';')
        if len(activity)==3:
            activity_name = activity[0]
            work_hours = activity[1]
            start_time = activity[2]
            current_date = datetime.datetime.now()
            self.append(activity_name, work_hours, start_time, current_date.strftime("%B %d, %Y"))
        else:
            print "[!] Enter at least 3 entries: activity;hours;start_time\n"
            
if __name__ == "__main__":
    automat = Workomat()
    while(True):
        automat.run()
            
    
        
        
        
        
        
        
        
        
        
        
