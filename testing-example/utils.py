import array_api_compat
import array_api_strict
import numpy as np
import pytest


# We store all available backends for testing.  This could be build as here
# or be configured e.g. via environment variables.
# scipy and scikit-learn both have similar but different setups.
available_backends = {
    "numpy": (np, "cpu"),
    "strict": (array_api_strict, None),
}

# Excercise Part III
#
# `available_backends` is a dictionary with a namespace (this can be cupy,
# or torch) that is used to get the available Array API backends below and
# define the correct `xp` and `device`.
#
# We wish to extend this in our tests to:
#
# * cupy, device can be `None`
# * torch[cpu]
# * torch[cuda]


def get_available_backends():
    for key, (array_mod, device) in available_backends.items():
        # The module is the original module, use array_api_compat to fetch
        # the compatible namespace:
        xp = array_api_compat.get_namespace(array_mod.asarray(1))
        yield pytest.param(xp, device, id=key)

array_api_compatible = pytest.mark.parametrize(
    "xp, device", get_available_backends()
)
