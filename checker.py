import pandas as pd
total_mods = []
NUSC_CC = [] # Critical Competencies - 4 Mods
NUSC_GO = [] # Global Orientation - 3 Mods
NUSC_MC = [] # Making Connections - 6 Mods (VARIES)
NUSC_IEx = [] # Impact Experience Project - 1 Mod

def get_mod_classification(mod): 
    module_code = mod[0:3] 
    # NUSC Mods
    for key, value in mod_codes_nusc.items():
        if module_code in value:
            return key


mod_codes_nusc = {
    'Thinking with Writing':	['TWW' , 'NTW'],
    'Reasoning with Data':	['RWD' ,'GEA1000N'],
    'Understanding the Social World: Singapore':['NSW'],
    'Computational Problem Solving':	['CPS , NPS'],
    'Global Narratives':	['GN , NGN'],
    'Global Social Thought':	['GST , NGT'],
    'Science and Society':	['SNS' , 'S&S' , 'NSS'],
    'Making Connections HSS':	['NHS'],
    'Making Connections STEM':	['NST'],
    'Impact Experience Project':	['IEx' , 'NEP'],
    'Global Experience Module':	['GEx'],
    }

bba_requirements = [
"DAO1704",	
"DAO2702",	
"BSP1703",
"BSP2701",	
"ACC1701",	
"BSP1702",	
"MKT1705",
"MNO1706",
"FIN2704",
"DAO2703",
"MNO2705",
"BSP3701",
"ES2002",
]

bba_specs = pd.read_csv('bba_specs.csv')

print(bba_specs['Marketing Must'].to_list())