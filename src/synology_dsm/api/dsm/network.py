"""DSM Network data."""


class SynoDSMNetwork:
    """Class containing Network data."""

    API_KEY = "SYNO.DSM.Network"

    def __init__(self, dsm):
        """Constructor method."""
        self._dsm = dsm
        self._data = {}

    def update(self):
        """Updates network data."""
        if raw_data := self._dsm.get(self.API_KEY, "list"):
            self._data = raw_data["data"]

    @property
    def dns(self):
        """DNS of the NAS."""
        return self._data.get("dns")

    @property
    def gateway(self):
        """Gateway of the NAS."""
        return self._data.get("gateway")

    @property
    def hostname(self):
        """Host name of the NAS."""
        return self._data.get("hostname")

    @property
    def interfaces(self):
        """Interfaces of the NAS."""
        return self._data.get("interfaces", [])

    def interface(self, eth_id):
        """Interface of the NAS."""
        return next(
            (
                interface
                for interface in self.interfaces
                if interface["id"] == eth_id
            ),
            None,
        )

    @property
    def macs(self):
        """MACs of the NAS."""  # noqa: D403
        return [
            interface["mac"]
            for interface in self.interfaces
            if interface.get("mac")
        ]

    @property
    def workgroup(self):
        """Workgroup of the NAS."""
        return self._data.get("workgroup")
