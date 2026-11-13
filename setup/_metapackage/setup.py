import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-vertical-agriculture",
    description="Meta package for oca-vertical-agriculture Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-animal_medicament>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
