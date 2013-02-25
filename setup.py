# coding: utf-8
from setuptools import setup

setup(
	name="pyflowdock",
	version="0.2.46",
	packages=[
		'flowdock',
		'flowdock.helpers',
	],
	package_dir={
		'flowdock': 'flowdock'
	},
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
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
		"Topic :: Communications",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: Implementation :: PyPy",
	]
)
