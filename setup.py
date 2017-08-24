from setuptools import setup,find_packages

NAME='units_physics'
PACKAGES = [NAME] + ["%s.%s" % (NAME, i) for i in find_packages(NAME)]

setup (
        name = NAME,
        version = '0.0.1',
        packages = PACKAGES,
        author = 'Guodong Yu',
        description = 'Units and physical constants',
        zip_safe = False,
        long_description = 'Units and constants in physics ',
        author_email = "yugd@live.cn",
        license = "GPL",
        keywords = ("Guodong", "comm"),
        platforms = "Independant",
        url = "",
      )

