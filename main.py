from instagram import Instagram
from tiktok import TikTok
from helperfunction import convert_amount
import pandas as pd

# load file contains link profile
with open("link_profile.txt") as file:
    links = file.read().split("\n")
    # extract username
    uname = [
        link.replace("https://www.tiktok.com/@", "").replace("https://www.instagram.com/", "").replace("https"
                                                                                                       "://instagram"
                                                                                                       ".com/",
                                                                                                       "").split(
            "?")[0].strip("/")
        for link in links]

# Find ER & Reach on Instagram
if "instagram" in links[0]:
    ig = Instagram(username=uname)
    er_ig = ig.get_er()
    er_ig_results = pd.DataFrame({"Username": uname,
                                  "ER": [str(er)+'%' for er in er_ig.values()]})
    er_ig_results.to_csv("results.csv", index=False)
    print(er_ig)

# Find ER & Reach on Tiktok
elif "tiktok" in links[0]:
    tt = TikTok(username=uname)
    er_reach_tt = tt.get_er_reach()
    er_tt = er_reach_tt[0]
    reach_tt = er_reach_tt[1]
    er_reach_tt_results = pd.DataFrame({"Username": uname,
                                        "ER": [str(er)+'%' for er in er_tt.values()],
                                        'Reach': [convert_amount(reach) for reach in reach_tt.values()]})
    er_reach_tt_results.to_csv("results.csv", index=False)
    print(er_tt)
    print(reach_tt)
