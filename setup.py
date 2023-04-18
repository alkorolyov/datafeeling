from setuptools import setup, find_packages

setup(
    name='datafeeling',
    url='https://github.com/mypackage.git',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas <=1.5.3',
        'scikit-learn',
        'catboost',
        'jupyter',
        'notebook',
        # 'ipywidgets<=7.7.5'
    ],
    # python_requires=3.8
)