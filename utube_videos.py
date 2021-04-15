from bs4 import BeautifulSoup
import requests, json, pprint

# link = 'https://www.youtube.com/c/KalleHallden/videos'
# link = 'https://www.youtube.com/c/JomaOppa/videos'
# link = 'https://www.youtube.com/c/MazhavilManoramaOfficial/videos'

url = 'https://www.youtube.com'

container = []
details = {}
try:

    proxies = {
        "http":"http://54.36.60.162:18133",
        "https":"http://54.36.60.162:18133",
    }
    res = requests.get(link,proxies=proxies,timeout=30)
    soup = BeautifulSoup(res.content, 'html.parser')
    all_scripts = soup.find_all('script')
    
    s = None
    for script in all_scripts:
        if 'var ytInitialData = {"' in str(script):
            s = str(script)
    data_s = json.loads(s.split("var ytInitialData = ")[1].replace(';</script>',''))
    # print(json.dumps(data_s))

    
    l = data_s['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']
    print(len(l))
    # """
    for i in range(len(l)-1):
        title = data_s['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][i]['gridVideoRenderer']['title']['runs'][0]['text']
        views = data_s['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][i]['gridVideoRenderer']['viewCountText']['simpleText']
        duration = data_s['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][i]['gridVideoRenderer']['thumbnailOverlays'][0]['thumbnailOverlayTimeStatusRenderer']['text']['simpleText']
        video_id = data_s['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][i]['gridVideoRenderer']['videoId']
        video_url = data_s['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][i]['gridVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
        details = {
                "Title": title,
                "Video_ID": video_id,
                "URL": url + video_url,
                "Views": views,
                "Duration": duration
            }
        container.append(details)
    print(json.dumps(container))
# """
except Exception as e:
    print(e)