
class Story:
    """Represent the complex object under construction."""
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Story parts:", self.parts)


class StoryBuilder:
    def __init__(self):
        self.story = Story()

    def build_image(self):
        pass

    def build_music(self):
        pass

    def build_video(self):
        pass

    def build_effect(self):
        pass


class FacebookConcreteBuilder(StoryBuilder):
    def build_image(self):
        self.story.add("Facebook Image")

    def build_music(self):
        self.story.add("Facebook Music")

    def build_video(self):
        self.story.add("Facebook Video")

    def build_effect(self):
        self.story.add("Facebook Effect")


# -------------------------
#     INSTAGRAM BUILDER
# -------------------------
class InstagramConcreteBuilder(StoryBuilder):
    def build_image(self):
        self.story.add("Instagram Image")

    def build_music(self):
        self.story.add("Instagram Music")

    def build_video(self):
        self.story.add("Instagram Video")

    def build_effect(self):
        self.story.add("Instagram Effect")



class StoryDirector:

    # Construct is optional — prepares builder if needed
    def construct(self, builder: StoryBuilder):
        self.builder = builder

    def basic_story(self):
        """Image only (story basique)."""
        self.builder.build_image()

    def video_story(self):
        """Video + effect + music."""
        self.builder.build_video()
        self.builder.build_effect()
        self.builder.build_music()



def main():
    
    concrete_builder = FacebookConcreteBuilder()
    director = StoryDirector()
    director.construct(concrete_builder)
    director.basic_story()
    story = concrete_builder.story
    story.show()

    
    concrete_builder2 = InstagramConcreteBuilder()
    director = StoryDirector()
    director.construct(concrete_builder2)
    director.video_story()
    story = concrete_builder2.story
    story.show()


# Run main
if __name__ == "__main__":
    main()
