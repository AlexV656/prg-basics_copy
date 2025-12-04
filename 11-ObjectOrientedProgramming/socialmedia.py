class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'number of posts = {len(self.posts)}')
        print('posts = '+'\n'+"\n".join(self.posts))
        print(f'username = {self.username}')
if __name__=="__main__":
    user = SocialMediaProfile('johndoe')
    user.add_post('Hello, world!')
    user.add_post('Had a great day at the partk!')
    user.add_post("What's up, Natalie? How are you?")
    user.display_timeline()