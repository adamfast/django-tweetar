from distutils.core import setup

setup(
    name = "django-tweetar",
    url = "http://github.com/adamfast/django-tweetar",
    author = "Adam Fast",
    author_email = "adamfast@gmail.com",
    version = "0.1",
    license = "BSD",
    packages = ["djtweetar", "djtweetar.runlogs"],
    install_requires = ['python-tweetar'],
    description = "App for posting current conditions to twitter via python-tweetar.",
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
