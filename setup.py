import setuptools
import subprocess
import os

cf_remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in cf_remote_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = cf_remote_version.split("-")
    cf_remote_version = v + "+" + i + ".git." + s

assert "-" not in cf_remote_version
assert "." in cf_remote_version

assert os.path.isfile("cf_remote/version.py")
with open("cf_remote/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % cf_remote_version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="klldFN-lobbybot",
    version=cf_remote_version,
    author="klldFN-lobbybot",
    author_email="shmohammed9944@gmail.com",
    description="fortnite lobbybot klldFN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/klldme/cf-remote",
    packages=setuptools.find_packages(),
    package_data={"klldFN-lobbybot": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    entry_points={"console_scripts": ["klldFN-lobbybot = cf_remoteklldFN-lobbybot.main:main"]},
    install_requires=[
        "requests >= 2.25.1",
        "apache-libcloud >= 3.3.1",
    ],
)
