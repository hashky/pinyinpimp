import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pinyinpimp',
    version='0.0.1',
    author='Hashky',
    author_email='hashky@protonmail.com',
    description='pinyin based binary to text codec frawmework for steganography and pneumonic generation'
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hashky/pinyinpimp',
    project_urls = {
        "Bug Tracker": "https://github.com/hashky/pinyinpimp/issues"
    },
    license='MIT',
    packages=['pinyinpimp'],
    install_requires=['pinyin','numpy'],
)
