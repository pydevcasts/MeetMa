from setuptools import setup, find_packages

setup(
    name='MeetMa',  # Package name in lowercase
    version='0.0.1',
    packages=find_packages(where='.'),  # Automatically find packages
    install_requires=[
        'PyQt6',
        'beautifulsoup4',
        'googletrans',
        'requests',
        'selenium'
    ],
    entry_points={
        'console_scripts': [
            'meetma=src.main:main',  # Adjust based on your actual structure
        ],
    },
    author='Siyamak Abasnezhad, Mahan Shirsavar',
    author_email='pydevcasts@gmail.com',
    description='Google Meet Bot is a Python application that automates participation in Google Meet meetings by extracting real-time subtitles, translating them, and detecting questions, enhancing users online meeting experience.',
    url='https://github.com/pydevcasts/MeetMa',  # Your GitHub URL
)