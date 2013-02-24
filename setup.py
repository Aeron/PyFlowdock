# coding: utf-8
from setuptools import setup

setup(
	name="pyflowdock",
	version="0.2",
	py_modules=['flowdock'],
	scripts=[],
	install_requires=['requests'],
	package_data={
		'': [],
	},
	author=u"Eugene “Aeron” Glybin",
	author_email="aeron@aeron.cc",
	description="Python wrapper for FlowDock APIs",
	license="LGPLv3",
	keywords="flowdock api wrapper",
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
		'Topic :: Communications'
	]
)
