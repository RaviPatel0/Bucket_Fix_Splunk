import os
  
bucket_to_recover = ""
bucket_to_not_recover = ""
bucket_manual_check = ""
FAIL_COLOR = '\033[91m'
ENDC_COLOR = '\033[0m'
SUCCESS_COLOR = '\033[92m'
WARNING_COLOR = '\033[93m'
OKBLUE_COLOR = '\033[94m'
HEAD_COLOR = '\u001b[34m'
 
print("Example Path = /Users/rnandasana/Downloads/all_details_main.txt")
location = input("Enter absolute path of all_details_<index_name>.txt file = ")
  
with open(location,'r') as f:
    for lines in f:
        bucket = lines.strip().split("|")
        idx = bucket[1].split(".")[0]
        path = bucket[2]
        print("===========")
        print(idx)
        print(path)
        print(" ")
        cmd = "sft ssh " + idx + " --command 'sudo -u splunk sh -c \"cd /opt/splunk/; ls -la " + path + " ; hostname -f ; date\"'"
        op = os.popen(cmd).read()
        #print("op output" + op + "close" )
        if op:
            if "rawdata" in op.lower():
                bucket_to_recover = bucket_to_recover + lines
                print(SUCCESS_COLOR + "\n rawdata is present for - " + path + ENDC_COLOR)
            else:
                bucket_to_not_recover = bucket_to_not_recover + lines
                print(WARNING_COLOR + "\n rawdata is not present for - " + path + ENDC_COLOR)  
        else:
            bucket_manual_check = bucket_manual_check + lines
            print(FAIL_COLOR + "\n Connection is Unsuccessful for Indexer - " + idx + ENDC_COLOR)
        print("===========")
  
print(" ")
print(HEAD_COLOR + "Paste this output in JIRA" + ENDC_COLOR)
print("============================================")       
print(OKBLUE_COLOR + "Below buckets are present with rawdata." + ENDC_COLOR)
print(SUCCESS_COLOR + bucket_to_recover + ENDC_COLOR)
print("======================")       
print(OKBLUE_COLOR + "Below buckets are not present with rawdata." + ENDC_COLOR)
print(WARNING_COLOR + bucket_to_not_recover + ENDC_COLOR)
print("======================")       
print(OKBLUE_COLOR + "Check below buckets manually." + ENDC_COLOR)
print(FAIL_COLOR + bucket_manual_check + ENDC_COLOR)
print("============================================")
