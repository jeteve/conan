import os
import textwrap

from conan.test.assets.cmake import gen_cmakelists
from conan.test.assets.sources import gen_function_cpp, gen_function_h
from conan.test.utils.file_server import TestFileServer
from conan.test.utils.test_files import temp_folder
from conan.test.utils.tools import TestClient, zipdir
from conan.internal.util.files import save_files, sha256sum


class TestGitRecipeIndexNew:
    def test_conan_new_git_recipes_index(self):
        # Setup the release pkg0.1.zip http server
        file_server = TestFileServer()
        zippath = os.path.join(file_server.store, "pkg0.1.zip")
        repo_folder = temp_folder()
        cmake = gen_cmakelists(libname="pkg", libsources=["pkg.cpp"], install=True,
                               public_header="pkg.h")
        save_files(repo_folder, {"pkg/CMakeLists.txt": cmake,
                                 "pkg/pkg.h": gen_function_h(name="pkg"),
                                 "pkg/pkg.cpp": gen_function_cpp(name="pkg")})
        zipdir(repo_folder, zippath)
        sha256 = sha256sum(zippath)
        url = f"{file_server.fake_url}/pkg0.1.zip"

        c0 = TestClient()
        c0.servers["file_server"] = file_server
        c0.run(
            f"new local_recipes_index -d name=pkg -d version=0.1 -d url={url} -d sha256={sha256}")

        remote_folder = c0.current_folder
        c0.run_command("git init")
        c0.run_command("git config user.name 'John Doe'")
        c0.run_command("git config user.email 'john@email.example'")
        c0.run_command('git add .')
        c0.run_command('git commit -m "Just a first commit"')

        # A local source is possible, and it includes a test_package
        c0.run("source recipes/pkg/all --version=0.1")
        assert "Uncompressing pkg0.1.zip" in c0.out

        c = TestClient()
        c.servers["file_server"] = file_server
        c.run(f"remote add local '{remote_folder}'")
#        c.run("download -r local pkg/0.1")
#        assert "Downloading recipe" in c.out

#        c.run("new cmake_exe -d name=app -d version=0.1 -d requires=pkg/0.1")
#        c.run("create . --version=0.1 --build=missing")
#        assert "pkg: Release!" in c.out
