from bs4 import BeautifulSoup
import requests
import pprint
import json

# link = 'https://www.youtube.com/user/Computerphile/about'
# link = 'https://www.youtube.com/c/Academind/about'
link = 'https://www.youtube.com/c/Netflix/about'
proxies = {
        "http":"http://54.36.60.162:18133",
        "https":"http://54.36.60.162:18133",
    }
about = []
details = {}

#-------- open file ----------------------



try:
    
    page = requests.get(link) 
    soup = BeautifulSoup(page.content, 'html.parser')

    all_scripts = soup.find_all('script')
    # print(all_scripts)
    s = None
    for script in all_scripts:
        if 'var ytInitialData = {' in str(script):
            s = str(script)
            # print("Script:: ", type(s))
    data = json.loads(s.split('var ytInitialData = ')[1].replace(';</script>', ''))
    # print(json.dumps(data))

    # """
    # ---------- Social Media Links -----------
    
    try:
        fb = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['primaryLinks'][1]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
        fb_link = fb.split('=')[-1]
        facebook = fb_link.replace('%2F', '/').replace('%3A', ':')

        twit = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['primaryLinks'][2]['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
        twit_link = twit.split('=')[-1]
        twitter = twit_link.replace('%2F', '/').replace('%3A', ':')


        description = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['description']['simpleText']
        subscriber = data['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText']
        joining_date = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['joinedDateText'] ['runs'][1]['text']
        
        # print(f'Description:: {description}')
        # print(f'facebook: {facebook}')
        # print(f'Twitter: {twitter}')
        # print(f'Subscriber:: {subscriber}')
        # print(f'Joined On:: {joining_date}')
        
        
        details = {
            "link": link,
            "Subscriber": subscriber,
            "Joined Date": joining_date,
            "Description": description,
            "Twitter": twitter,
            "Facebook": facebook
        }
        about.append(details)
    except Exception as e:
        
        subscriber = data['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText']
        joining_date = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][5]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['channelAboutFullMetadataRenderer']['joinedDateText'] ['runs'][1]['text']
        

        # print(f'Subscriber:: {subscriber}')
        # print(f'Joined On:: {joining_date}')
        

        details = {
            "link": link,
            "Subscriber": subscriber,
            "Joined Date": joining_date,
            "Description": description,
            "Twitter": twitter,
            "Facebook": facebook
        }
        about.append(details)
    print(json.dumps(about))

# """
except Exception as e:
    print(e)