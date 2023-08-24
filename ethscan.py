# import OS module
import os, json, itertools
import cfscrape




# Get the list of all files and directories
path_to_json_files = "input/php/"

#get all JSON file names as a list
json_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.json')]

for json_file_name in json_file_names:
    with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
        json_text = json.load(json_file)
        # print(json_file_name, json_text, type(json.dumps(json_text)))
        ab = itertools.chain(json_text)
        numbersList = list(ab)
        print("\n")
        for idx, addressArr in enumerate(numbersList):url = "https://etherscan.io/token/"+addressArr['address']
        print(url)
        scraper = cfscrape.create_scraper()
        scrapcontent = scraper.get(url).content
        text_file = open("file/sample" + addressArr['address'] + ".html", "w")
        text_file.write("%s" % scrapcontent)
        text_file.close()