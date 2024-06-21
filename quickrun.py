from json import load

def handle_followers(blo):
     blo = blo["text_post_app_text_post_app_followers"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     return lst

def handle_following(blo):
     blo = blo["text_post_app_text_post_app_following"]
     lst:list = []
     for i in blo:
          lst.append(i["string_list_data"][0]["value"])
     return lst

def save_in_file(filename:str,lst:list):
     with open(file=filename,mode="x") as f:
          for i in lst:
               f.write(f"{str(i)}\n")

from time import time

def main():
     a = handle_followers(load(open("./followers.json")))
     b = handle_following(load(open("./following.json")))
     lst:list = []
     for i in b:
          if i in a:
               pass
          else:
               lst.append(i)

     save_in_file(f"{int(time())}.txt",lst)

main()