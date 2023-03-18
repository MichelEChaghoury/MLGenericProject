from setuptools import find_packages, setup


def get_requirements(file_name: str = 'requirements.txt') -> list[str]:
    """return a list of the dependencies needed

    Args:
        file_name (str, optional): the name of the file that have all the packages and dependencies. 
        Defaults to 'requirements.txt'.

    Returns:
        set[str]: the list of the dependencies
    """

    unwanted_requirements: list[str] = ['-e .']
    requirements: list[str] = []

    # reading and saving dependencies, packages into requirements list
    with open(file_name, encoding='utf-8') as file:
        lines: list[str] = file.readlines()
        for line in lines:
            requirement: str = line.replace('\n', '')
            requirements.append(requirement)

        # remove unwanted dependencies and packages from requirements list
        for req in unwanted_requirements:
            if req in requirements:
                requirements.remove(req)

    return requirements


setup(
    name='mlgenericproject',
    version='0.0.1',
    author='chaghourymichel',
    author_email='michel.e.chaghoury@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
