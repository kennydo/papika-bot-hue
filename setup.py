from setuptools import (
    find_packages,
    setup,
)


setup(
    name='papika-bot-hue',
    version='0.0.1',
    description="Control Hue over Slack over Kafka",
    url='https://github.com/kennydo/papika-bot-hue',
    author='Kenny Do',
    author_email='chinesedewey@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
    ],
    packages=find_packages(exclude=['tests']),
    package_data={
    },
    include_package_Data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'papika-bot-hue = papikabothue.cli:main',
        ],
    },
)
