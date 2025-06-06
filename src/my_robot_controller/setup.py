from setuptools import find_packages, setup

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marialealsuarez',
    maintainer_email='marialealsuarez@gmail.com',
    description='PESAO',
    license='TODO: License declaration',
    tests_require=['pytest'],
  entry_points={
    'console_scripts': [
        'gui_control = my_robot_controller.gui_control:main',
    ],
},


   
)
