#####general purpose module imports
try:
    import requests  #pip install requests
    import getpass
    import xml.etree.ElementTree as ET
    import json
    import lxml
    import lxml.etree
    import xml.dom.minidom
    import StringIO
    import os
    import ntpath
    import besapi  #os.system('pip install -U -e git+https://github.com/CLCMacTeam/besapi.git#egg=besapi')
except:
    print("A module Did Not Load")
#####disable insecure warnings as we are not using a certificate
try:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except:
    print("Could not disable urllib3 warnings")
#####Setup config parser and pull relevant stored info to variables#####
import configparser
#Save a config.txt file in a location of your choice in secure location and add below lines that are commented out
#[bfcreds]
#name = "yourbigfixusername"
#passwd = "yourbigfixpassword"
#bfroot = 'http://192.168.9.200'
#bfport = '52311'
config = configparser.ConfigParser()
config.read("config.txt")
besuname = config.get("bfcreds","bfuser")
bespass = config.get("bfcreds","bfpasswd")
besroot = config.get("bfcreds","bfroot")
besport = config.get("bfcreds","bfport")
bes_computer_target_list = list()
#####Run the Script
try:
    testurl = "http://" + besroot + ":" + besport + "/api/login"
    testconn = requests.get(testurl,verify=False,auth=(bfuname,bfpass)) 
    if testconn.status_code != 200: 
        print("here" + testconn.status_code)
    else:
        baseurl = "http://" + besroot + ":" + besport + "/api"
        #run get relevance data
        def get_computerids_from_computergroup(bes_computer_group_id):
            global bes_computer_target_list
            if (bes_computer_target_list is None) or ( 0 == len(bes_computer_target_list) ):
                result = requests.get(get_computergroup_resource_url(bes_computer_group_id) + "/computers" , auth=(BES_USER_NAME, BES_PASSWORD), verify=False)
                computer_url_list = get_xpath_from_xml( result.text, '/BESAPI/Computer/@Resource' )
                computer_list = list()
                for strURL in computer_url_list:
                    head, tail = ntpath.split(strURL)
                    computer_list.append(tail)
                    bes_computer_target_list = computer_list
                    return bes_computer_target_list
        def get_computergroup_resource_url(bes_computer_group_id):
            relevance = 'concatenations "/" of ( ( if operator site flag of it then "operator" else if custom site flag of it then "custom" else if master site flag of it then "actionsite" else "external" ) of site of it; name of site of it; (it as string) of id of it) of bes computer groups whose(id of it = '+ bes_computer_group_id +')'
            result = get_session_relevance(relevance)
            return BES_API_URL + 'computergroup/' + result
        
except:
    print("an error occured")



        #baseurl = "http://" + besroot + ":" + besport + "/api"
        #data = requests.get(baseurl + "fixlets/external/BES Support",verify=False,auth=(bfuname,bfpass))
        #fixlets = ET.fromstring(data.text)
        #i = [] 
        #n = []
        #print 'starting search in results' for fixlet in root.findall('Fixlet'): n.append(fixlet.find('Name').text) 
        #print(data.text)


