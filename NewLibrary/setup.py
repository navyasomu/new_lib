from setuptools import setup, find_packages

setup(
   name="new_library_package",
   author="navya",
   description="Private Python library",
   packages=find_packages(),
   include_package_data=True,
   classifiers=[
       "Environment :: Web Environment",
       "Intended Audience :: Developers",
       "Operating System :: OS Independent"
       "Programming Language :: Python",
       "Programming Language :: Python :: 3.11",
       "Topic :: Internet :: WWW/HTTP",
       "Topic :: Internet :: WWW/HTTP :: Dynamic Content"
   ],
   python_requires='>=3.11',
   setup_requires=['setuptools-git-versioning'],
   version_config={
       "dirty_template": "{tag}",
   }
)