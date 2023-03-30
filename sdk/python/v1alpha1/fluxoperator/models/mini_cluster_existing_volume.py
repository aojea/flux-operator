# coding: utf-8

"""
    fluxoperator

    Python SDK for Flux-Operator  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from fluxoperator.configuration import Configuration


class MiniClusterExistingVolume(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'claim_name': 'str',
        'path': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'claim_name': 'claimName',
        'path': 'path',
        'read_only': 'readOnly'
    }

    def __init__(self, claim_name='', path='', read_only=False, local_vars_configuration=None):  # noqa: E501
        """MiniClusterExistingVolume - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._claim_name = None
        self._path = None
        self._read_only = None
        self.discriminator = None

        self.claim_name = claim_name
        self.path = path
        if read_only is not None:
            self.read_only = read_only

    @property
    def claim_name(self):
        """Gets the claim_name of this MiniClusterExistingVolume.  # noqa: E501


        :return: The claim_name of this MiniClusterExistingVolume.  # noqa: E501
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """Sets the claim_name of this MiniClusterExistingVolume.


        :param claim_name: The claim_name of this MiniClusterExistingVolume.  # noqa: E501
        :type claim_name: str
        """
        if self.local_vars_configuration.client_side_validation and claim_name is None:  # noqa: E501
            raise ValueError("Invalid value for `claim_name`, must not be `None`")  # noqa: E501

        self._claim_name = claim_name

    @property
    def path(self):
        """Gets the path of this MiniClusterExistingVolume.  # noqa: E501

        Path and claim name are always required  # noqa: E501

        :return: The path of this MiniClusterExistingVolume.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MiniClusterExistingVolume.

        Path and claim name are always required  # noqa: E501

        :param path: The path of this MiniClusterExistingVolume.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def read_only(self):
        """Gets the read_only of this MiniClusterExistingVolume.  # noqa: E501


        :return: The read_only of this MiniClusterExistingVolume.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this MiniClusterExistingVolume.


        :param read_only: The read_only of this MiniClusterExistingVolume.  # noqa: E501
        :type read_only: bool
        """

        self._read_only = read_only

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MiniClusterExistingVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MiniClusterExistingVolume):
            return True

        return self.to_dict() != other.to_dict()