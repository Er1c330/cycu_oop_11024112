from setuptools import setup, find_packages

setup(
    name="taipei_ebus",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["20250513.ebus_map_hw1"],
    entry_points={
        "console_scripts": [
            "taipei_ebus=20250513.ebus_map_hw1:get_bus_info_go",
        ],
    },
    author="Your Name",
    description="A script to fetch and store Taipei eBus route and stop data.",
    python_requires=">=3.7",
    install_requires=[
        "pandas",
        "playwright",
        "sqlalchemy",
    ],
)
