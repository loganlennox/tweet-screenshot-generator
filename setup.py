from setuptools import setup

setup(name = "tweet_screenshot_generator",
      version = "0.1",
      description = "Generates a screenshot of a single tweet based on user input",
      url = "https://www.github.com/loganlennox/tweet-screenshot-generator",
      author = "Logan Lennox",
      author_email = "loganlennox@protonmail.com",
      license = "MIT",
      pacakges = ["tweet_screenshot_generator"],
      install_requires = [
          "imgkit"
      ],
      zip_safe = False)
