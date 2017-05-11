from setuptools import setup

setup(
    name='yeswecansvg',
    version='0.1.0',
    description='Clean your SVGs so Illustrator won\'t tell you it CANT.',
    author='Armand Emamdjomeh',
    author_email='armand.emamdjomeh@washpost.com',
    url='http://github.com/emamd/yeswecansvg',
    download_url='http://github.com/emamd/yeswecansvg.git',
    packages=("yeswecansvg",),
    # cmdclass={'test': TestCommand},
    # install_requires=('six>=1.4.1'),
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': [
            'yeswecansvg=yeswecansvg.yeswecansvg',
        ],
    },
)