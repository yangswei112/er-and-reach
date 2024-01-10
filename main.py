from instagram import Instagram
from tiktok import TikTok

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

# find IG ER
ig = Instagram(username=uname)
er_ig = ig.get_er()
print(er_ig)

# find Tiktok ER & Reach
tt = TikTok(username=uname)
er_reach_tt = tt.get_er_reach()
er_tt = er_reach_tt[0]
reach_tt = er_reach_tt[1]
print(er_tt)
print(reach_tt)
