from instagram import Instagram
from tiktok import TikTok

unem = ["yangswei", "selenagomez", "taylorswift"]

ig = Instagram(username=unem)
er_ig = ig.get_er()
print(er_ig)

tt = TikTok(username=unem)
er_reach_tt = tt.get_er_reach()
er_tt = er_reach_tt[0]
reach_tt = er_reach_tt[1]
print(er_tt)
print(reach_tt)
