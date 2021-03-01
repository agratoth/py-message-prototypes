from setuptools import setup


setup(
    name='py-message-prototypes',
    zip_safe=True,
    version='0.2.1',
    description='Prototype objects for messaging and datapipes',
    url='https://github.com/agratoth/py-message-prototypes',
    maintainer='Anton Berdnikov',
    maintainer_email='agratoth@yandex.ru',
    packages=[
        'message_prototypes',
        'message_prototypes.exceptions',
        'message_prototypes.pipe_messages',
    ],
    package_dir={'py-message-prototypes': 'message_prototypes'},
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Object Brokering",
    ],
    python_requires='>=3.8',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
