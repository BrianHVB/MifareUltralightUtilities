from setuptools import setup

setup(
    name='EchoNFC-Ultralight',
    version='1.0.0',
    py_modules=['ultralight_tools'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ultralight-tools=ultralight_tools:main
    '''
)