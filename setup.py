from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author='Brian Wollermann',
    author_email='bwollermann@glhec.org',
    description='snapshotAlyzer is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/bwollermann/snapshotalyzer-30000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
