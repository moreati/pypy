import setuptools

setuptools.setup(
    cffi_modules=[
        "lib_pypy/_lzma_build.py:ffi",
    ],
    install_requires=[
        'cffi>=1.0.0',
    ],
    setup_requires=[
        'cffi>=1.0.0',
    ],
)
