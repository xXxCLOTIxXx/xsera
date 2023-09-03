from xsera import generate_github_avatar

"""
@generate_github_avatar@

avatar_size: int     - picture size
nickname: str     - your nickname (a picture is created based on it)
background_color: str    - background pictures (hex)
format: str   - picture format ["jpg", "png", "jpeg"]
dir: str   - save path
randomize: bool   - will add random letters for noise to your nickname
save_name: str   - the name under which the image will be saved



return - file path
"""


print(generate_github_avatar()) #create an avatar based on a random nickname
print(generate_github_avatar(nickname="Xsarz", randomize=False, save_name="my_avatar")) #create an avatar based on your nickname