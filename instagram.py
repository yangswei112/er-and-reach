from instaloader import Instaloader, Profile, ConnectionException
from itertools import islice


class Instagram:

    def __init__(self, username):
        self.username = username

    def get_er(self):
        loader = Instaloader()
        er_dict = {}
        for uname in self.username:
            try:
                profile = Profile.from_username(loader.context, uname)
            except ConnectionException:
                er_dict[uname] = "Profile doesn't exist"
            else:
                # Get posts and limit them with islice
                posts = set(islice(profile.get_posts(), 12))

                num_followers = profile.followers
                total_num_likes = 0
                total_num_comments = 0
                total_num_posts = 0

                for post in posts:
                    total_num_likes += post.likes
                    total_num_comments += post.comments
                    total_num_posts += 1

                engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
                er_dict[uname] = round(engagement * 100, 2)

        return er_dict
