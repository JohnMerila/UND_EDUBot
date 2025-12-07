from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'PiBot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rosdev',
    maintainer_email='rosdev@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'PiBot = PiBot.PiBot:main',
            'motor_control = PiBot.motor_control:main',
            'encoder_data = PiBot.encoder_publisher:main'
        ],
        
    },
)
