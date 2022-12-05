from setuptools import setup
from Projet import __version__ as current_version

setup(
  name='Projet',
  version=current_version,
  description='Visualization and prediction of French Electrical Consumption',
  url='https://github.com/Mehdichak/projectdevlog.git',
  author='Leroy Nicolas, Chakroun Mohamed Mehdi, Axel de Montgolfier',
  author_email='nicolas.leroy@etu.umontpellier.fr, axel.de-montgolfier@etu.umontpellier.fr, mohamed-mehdi.chakroun@etu.umontpellier.fr ',
  license='MIT',
  packages=['Projet','Projet.Data_visu', 'Projet.prediction'],
  zip_safe=False
)