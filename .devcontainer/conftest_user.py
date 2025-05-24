"""
To override these locations with your own in your dev machine:
1. Create a conftest_user.py just besides this conftest.py file
2. This file is .gitignored, it will not be committed
3. Override the tools_locations, you can completely disabled some tools, tests will be skipped
4. Empty dicts, without specifying the path, means the tool is already in the system
   path


tools_locations = {
    'svn': {"disabled": True},
    'cmake': {
        "default": "3.19",
        "3.15": {},
        "3.16": {"disabled": True},
        "3.17": {"disabled": True},
        "3.19": {"path": {"Windows": "C:/ws/cmake/cmake-3.19.7-windows-x86_64/bin"}},
        # To explicitly skip one tool for one version, define the path as 'skip-tests'
        # if you don't define the path for one platform it will run the test with the
        # tool in the path. For example here it will skip the test with CMake in Darwin but
        # in Linux it will run with the version found in the path if it's not specified
        "3.23": {"path": {"Windows": "C:/ws/cmake/cmake-3.19.7-windows-x86_64/bin",
                          "Darwin": "skip-tests"}},
    },
    'ninja': {
        "1.10.2": {}
    },
    'meson': {"disabled": True},
    'bazel':  {
        "system": {"path": {'Windows': 'C:/ws/bazel/4.2.0'}},
    }
}
"""

DISABLED = {"disabled": True}

tools_locations = {
    "clang": DISABLED,
    'visual_studio': DISABLED,
    'pkg_config': DISABLED,
    'autotools': DISABLED,
    'cmake': DISABLED,
    'ninja': DISABLED,
    # This is the non-msys2 mingw, which is 32 bits x86 arch
    'mingw': DISABLED,
    'mingw32': DISABLED,
    'ucrt64': DISABLED,
    'mingw64': DISABLED,
    'msys2': DISABLED,
    'msys2_clang64': DISABLED,
    'msys2_mingw64_clang64': DISABLED,
    'cygwin': DISABLED,
    'bazel': DISABLED,
    'premake': DISABLED,
    'xcodegen': DISABLED,
    'apt_get': DISABLED,
    'brew': DISABLED,
    "qbs": DISABLED
}
