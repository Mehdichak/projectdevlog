from setuptools import setup
from predivis import __version__ as current_version

setup(
  name='predivis',
  version=current_version,
  description='Visualization and prediction of French Electrical Consumption',
  url='https://github.com/Mehdichak/projectdevlog.git',
  author='Leroy Nicolas, Chakroun Mohamed Mehdi, Axel de Montgolfier',
  author_email='nicolas.leroy@etu.umontpellier.fr, axel.de-montgolfier@etu.umontpellier.fr, mohamed-mehdi.chakroun@etu.umontpellier.fr ',
  license='MIT',
  packages=['predivis','predivis.visu', 'predivis.prediction'],
  zip_safe=False,
  package_data={'predivis':["Data/*"]}
)