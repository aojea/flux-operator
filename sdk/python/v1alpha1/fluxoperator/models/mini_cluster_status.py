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


class MiniClusterStatus(object):
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
        'conditions': 'list[V1Condition]',
        'jobid': 'str',
        'maximum_size': 'int',
        'selector': 'str',
        'size': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'jobid': 'jobid',
        'maximum_size': 'maximumSize',
        'selector': 'selector',
        'size': 'size'
    }

    def __init__(self, conditions=None, jobid='', maximum_size=0, selector='', size=0, local_vars_configuration=None):  # noqa: E501
        """MiniClusterStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._jobid = None
        self._maximum_size = None
        self._selector = None
        self._size = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        self.jobid = jobid
        self.maximum_size = maximum_size
        self.selector = selector
        self.size = size

    @property
    def conditions(self):
        """Gets the conditions of this MiniClusterStatus.  # noqa: E501

        conditions hold the latest Flux Job and MiniCluster states  # noqa: E501

        :return: The conditions of this MiniClusterStatus.  # noqa: E501
        :rtype: list[V1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this MiniClusterStatus.

        conditions hold the latest Flux Job and MiniCluster states  # noqa: E501

        :param conditions: The conditions of this MiniClusterStatus.  # noqa: E501
        :type conditions: list[V1Condition]
        """

        self._conditions = conditions

    @property
    def jobid(self):
        """Gets the jobid of this MiniClusterStatus.  # noqa: E501

        The Jobid is set internally to associate to a miniCluster This isn't currently in use, we only have one!  # noqa: E501

        :return: The jobid of this MiniClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._jobid

    @jobid.setter
    def jobid(self, jobid):
        """Sets the jobid of this MiniClusterStatus.

        The Jobid is set internally to associate to a miniCluster This isn't currently in use, we only have one!  # noqa: E501

        :param jobid: The jobid of this MiniClusterStatus.  # noqa: E501
        :type jobid: str
        """
        if self.local_vars_configuration.client_side_validation and jobid is None:  # noqa: E501
            raise ValueError("Invalid value for `jobid`, must not be `None`")  # noqa: E501

        self._jobid = jobid

    @property
    def maximum_size(self):
        """Gets the maximum_size of this MiniClusterStatus.  # noqa: E501

        We keep the original size of the MiniCluster request as this is the absolute maximum  # noqa: E501

        :return: The maximum_size of this MiniClusterStatus.  # noqa: E501
        :rtype: int
        """
        return self._maximum_size

    @maximum_size.setter
    def maximum_size(self, maximum_size):
        """Sets the maximum_size of this MiniClusterStatus.

        We keep the original size of the MiniCluster request as this is the absolute maximum  # noqa: E501

        :param maximum_size: The maximum_size of this MiniClusterStatus.  # noqa: E501
        :type maximum_size: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_size is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_size`, must not be `None`")  # noqa: E501

        self._maximum_size = maximum_size

    @property
    def selector(self):
        """Gets the selector of this MiniClusterStatus.  # noqa: E501


        :return: The selector of this MiniClusterStatus.  # noqa: E501
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this MiniClusterStatus.


        :param selector: The selector of this MiniClusterStatus.  # noqa: E501
        :type selector: str
        """
        if self.local_vars_configuration.client_side_validation and selector is None:  # noqa: E501
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

    @property
    def size(self):
        """Gets the size of this MiniClusterStatus.  # noqa: E501

        These are for the sub-resource scale functionality  # noqa: E501

        :return: The size of this MiniClusterStatus.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MiniClusterStatus.

        These are for the sub-resource scale functionality  # noqa: E501

        :param size: The size of this MiniClusterStatus.  # noqa: E501
        :type size: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if not isinstance(other, MiniClusterStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MiniClusterStatus):
            return True

        return self.to_dict() != other.to_dict()
