import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-vertical-agriculture",
    description="Meta package for oca-vertical-agriculture Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-herd',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
