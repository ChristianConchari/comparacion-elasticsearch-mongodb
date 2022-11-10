import os

def create_dir(folder):
    if not os.path.isdir(folder):
        print("Creating :" + folder)
        os.mkdir(folder)

storage_dir = "json-generated-data-elastic"

create_dir(storage_dir)

for i, json_file in enumerate(os.listdir("json-generated-data")):
    #print(os.path.join(storage_dir, json_file))
    string1 = f"""jq -c -r ".[]" {os.path.join("json-generated-data", json_file)}"""
    string2 = """| while read line; do echo '{"index":{}}';"""
    string3 = f"""echo $line; done > bulk.json'"""
    
    print(string1+string2+string3)