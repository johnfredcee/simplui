
import setuptools


setuptools.setup(
	name = 'simplui',
	version = '1.0.4',
	author = 'Tristam MacDonald',
	author_email = 'swiftcoder@gmail.com',
	description = 'Light-weight GUI toolkit for pyglet',
	url = 'http://simplui.googlecode.com/',
	platforms = ['all'],
	license = 'BSD',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Topic :: Scientific/Engineering :: Human Machine Interfaces',
		'Topic :: Software Development :: User Interfaces',
	],
	include_package_data=True,
	package_data = { 'simplui' : [ "themes/macos/*.json", "themes/macos/*.png", "themes/pywidget/*.json", "themes/pywidget/*.png" ] },
	packages = setuptools.find_packages(),
	install_requires = ['simplejson >= 2.0', 'pyglet >= 1.1']
)