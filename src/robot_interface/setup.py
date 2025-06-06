from setuptools import setup

package_name = 'robot_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='leonlagog@gmail.com',
    description='Robot control interface for moving forward/backward',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_control = robot_interface.robot_control:main',
        ],
    },
)
