from setuptools import setup
setup(
    name = 'videotoascii',
    version = '1.0.0',
    packages = ['video_to_ascii'],
    entry_points = {
        'console_scripts': [
            'videotoascii = video_to_ascii.__main__:main'
        ]
    })