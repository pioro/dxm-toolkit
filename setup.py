from setuptools import setup, find_packages
#import dxm.dxm

setup(
    name='dxm',
    #version=dxm.dxm.__version__,
    packages=find_packages(),
    install_requires=[
        'click','requests','pytz', "urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "colorama", "tqdm", "packaging", "keyring", "cryptography",
        'masking_api_53', 'masking_api_60'
    ],
    entry_points='''
        [console_scripts]
        dxmc=dxm.dxm:dxm
    ''',
    author = "Marcin Przepiorowski",
    license = "Apache 2",
    description = ("DxToolkit for Masking - command line tool to manage Delphix Masking environment"),
    classifiers = [
        "Development Status :: 2 - Beta"
    ],
    dependency_links=[
        'git+https://github.com/pioro/masking_api_53.git#egg=masking_api_53-1.0.0',
        'git+https://github.com/pioro/masking_api_60.git#egg=masking_api_60-6.0.4.2'
    ]
)


# add swagger libs
# docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -DapiDocs=false -DapiTests=false -DmodelTests=false -DmodelDocs=false -i http://myengine/masking/api/swagger-basepath.json -l python -o /local/masking_api_60 -DpackageName=masking_api_60
# cd masking_api_60
# python setup.py install
