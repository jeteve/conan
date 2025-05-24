LOCAL_RECIPES_INDEX = "local-recipes-index"
GIT_RECIPES_INDEX = "git-recipes-index"


class Remote:
    """
    The ``Remote`` class represents a remote registry of packages. It's a read-only opaque object that
    should not be created directly, but obtained from the relevant ``RemotesAPI`` subapi methods.
    """

    def __init__(self, name: str, url: str, verify_ssl: bool = True, disabled: bool = False, allowed_packages: list[str] | None = None,
                 remote_type: str | None = None):
        """

        :param str|None remote_type: Remote type as a string. None simply means a vanilla conan remote.

        """
        self.name = name  # Read only, is the key
        self.url = url
        self.verify_ssl = verify_ssl
        self.disabled = disabled
        self.allowed_packages = allowed_packages
        self.remote_type = remote_type
        self._caching = {}

    def __eq__(self, other):
        if other is None:
            return False
        return (self.name == other.name and self.url == other.url and
                self.verify_ssl == other.verify_ssl and self.disabled == other.disabled)

    def __str__(self):
        allowed_msg = ""
        if self.allowed_packages:
            allowed_msg = ", Allowed packages: {}".format(", ".join(self.allowed_packages))
        if self.remote_type is not None:
            return "{}: {} [{}, Enabled: {}{}]".format(self.name, self.url, self.remote_type,
                                                       not self.disabled, allowed_msg)
        return "{}: {} [Verify SSL: {}, Enabled: {}{}]".format(self.name, self.url, self.verify_ssl,
                                                               not self.disabled, allowed_msg)

    def __repr__(self):
        return str(self)

    def invalidate_cache(self):
        self._caching = {}
