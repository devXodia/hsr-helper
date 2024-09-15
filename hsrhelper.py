#! python3
# hsrhelper.py - Checks for HSR Data like Tierlists and Character Infos.

import requests, bs4
from colorama import Fore, Back, Style, just_fix_windows_console, init, deinit, reinit

res = requests.get('https://www.prydwen.gg/star-rail/tier-list/')
res.raise_for_status()
hsr_soup = bs4.BeautifulSoup(res.text, 'html.parser')
tiers = hsr_soup.select('div .tier-rating > span')
tier_arr = []

init()

def print_head():
    print(Fore.BLUE + r"""
          
           __  __  ______  __   __  __  __   ______  __       ______  ______  ______  ______       ______  ______  __  __        
/\ \_\ \/\  __ \/\ "-.\ \/\ \/ /  /\  __ \/\ \     /\  ___\/\__  _\/\  __ \/\  == \     /\  == \/\  __ \/\ \/\ \       
\ \  __ \ \ \/\ \ \ \-.  \ \  _"-.\ \  __ \ \ \    \ \___  \/_/\ \/\ \  __ \ \  __<     \ \  __<\ \  __ \ \ \ \ \____  
 \ \_\ \_\ \_____\ \_\\"\_\ \_\ \_\\ \_\ \_\ \_\    \/\_____\ \ \_\ \ \_\ \_\ \_\ \_\    \ \_\ \_\ \_\ \_\ \_\ \_____\ 
  \/_/\/_/\/_____/\/_/ \/_/\/_/\/_/ \/_/\/_/\/_/     \/_____/  \/_/  \/_/\/_/\/_/ /_/     \/_/ /_/\/_/\/_/\/_/\/_____/ 
                                                                                                                       
 __  __  ______  __      ______  ______  ______                                                                        
/\ \_\ \/\  ___\/\ \    /\  == \/\  ___\/\  == \                                                                       
\ \  __ \ \  __\\ \ \___\ \  _-/\ \  __\\ \  __<                                                                       
 \ \_\ \_\ \_____\ \_____\ \_\   \ \_____\ \_\ \_\                                                                     
  \/_/\/_/\/_____/\/_____/\/_/    \/_____/\/_/ /_/
          
          """  + Fore.RESET)


print_head()
print(Fore.MAGENTA + '!!!DISCLAIMER!!!' + Fore.RESET)
print("")
print(Fore.RED + 'RED COLOR = DMG DEALER' + Fore.RESET)
print(Fore.BLUE + 'BLUE COLOR = SPECIALIST' + Fore.RESET)
print(Fore.GREEN + 'GREEN COLOR = SUSTAIN' + Fore.RESET)
print(Fore.YELLOW + 'YELLOW COLOR = AMPLIFIER' + Fore.RESET)
print("")
print(f"Starting Tier List...")
print("")

def normal_dps(text):
    burst_dps_arr = hsr_soup.select(f'div.custom-tier.{text} > div.custom-tier-container > div.custom-tier-burst.dps > span > div > span > a')
    list = []
    for link in burst_dps_arr:
        char = link['href']
        char_name = char.replace('/star-rail/characters/', '').capitalize()
        print(Fore.RED + char_name + Fore.RESET)
        Fore.RESET
        deinit()
        list.append(char_name)
    return list

def get_debuffer(text):
    debuffer_arr = hsr_soup.select(f'div.custom-tier.{text} > div.custom-tier-container > div.custom-tier-burst.debuffer > span > div > span > a')
    list = []
    for link in debuffer_arr:
        char = link['href']
        char_name = char.replace('/star-rail/characters/', '').capitalize()
        print(Fore.BLUE + char_name + Fore.RESET)
        Fore.RESET
        deinit()
        list.append(char_name)
    return list


def get_support(text):
    mobile_debuffer_arr = hsr_soup.select(f'div.custom-tier.{text} > div.custom-tier-container > div.custom-tier-burst.support > span > div > span > a')
    list = []
    for link in mobile_debuffer_arr:
        char = link['href']
        char_name = char.replace('/star-rail/characters/', '').capitalize()
        print(Fore.YELLOW + char_name + Fore.RESET)
        Fore.RESET
        deinit()
        list.append(char_name)
    return list


def get_sustain(text):
    sustain_arr = hsr_soup.select(f'div.custom-tier.{text} > div.custom-tier-container > div.custom-tier-burst.sustain > span > div > span > a')
    list = []
    for link in sustain_arr:
        char = link['href']
        char_name = char.replace('/star-rail/characters/', '').capitalize()
        print(Fore.GREEN + char_name + Fore.RESET)
        Fore.RESET
        list.append(char_name)
    print("")
    return list


for el in tiers:
    text = el.get_text()
    counter = -1
    if el != tiers[0]:
        counter += 1
        print(f"-----{text}-----")
        if "T" in text:
            text = el.get_text().replace('T', 'tier-')
        if "." in text:
            text = text.replace('.', '')
        get_all_arrays = [normal_dps(text), get_debuffer(text), get_support(text), get_sustain(text)]
        tier_arr.append(get_all_arrays)


deinit()
input("Press enter to exit...")