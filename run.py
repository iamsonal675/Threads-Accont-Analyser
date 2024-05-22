from json import load

def open_data():
     followers = load(open("./threads/your_instagram_activity/threads/followers.json"))
     following = load(open("./threads/your_instagram_activity/threads/following.json"))
     liked_threads = load(open("./threads/your_instagram_activity/threads/liked_threads.json"))
     pending_follow_requests = load(open("./threads/your_instagram_activity/threads/pending_follow_requests.json"))
     personal_information = load(open("./threads/your_instagram_activity/threads/personal_information.json"))
     recent_follow_requests = load(open("./threads/your_instagram_activity/threads/recent_follow_requests.json"))
     recent_unfollowed_accounts = load(open("./threads/your_instagram_activity/threads/recently_unfollowed_accounts.json"))
     threads_and_replies = load(open("./threads/your_instagram_activity/threads/threads_and_replies.json"))
     threads_viewed = load(open("./threads/your_instagram_activity/threads/threads_viewed.json"))
     return [
          followers,
          following,
          liked_threads,
          pending_follow_requests,
          personal_information,
          recent_follow_requests,
          recent_unfollowed_accounts,
          threads_and_replies,
          threads_viewed
     ]

def handle_followers(blo):
     blo = blo[0]["text_post_app_text_post_app_followers"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     return lst

def handle_following(blo):
     blo = blo[1]["text_post_app_text_post_app_following"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     return lst

