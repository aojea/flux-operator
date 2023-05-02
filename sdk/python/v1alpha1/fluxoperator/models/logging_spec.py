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


class LoggingSpec(object):
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
        'debug': 'bool',
        'quiet': 'bool',
        'strict': 'bool',
        'timed': 'bool',
        'zeromq': 'bool'
    }

    attribute_map = {
        'debug': 'debug',
        'quiet': 'quiet',
        'strict': 'strict',
        'timed': 'timed',
        'zeromq': 'zeromq'
    }

    def __init__(self, debug=False, quiet=False, strict=True, timed=False, zeromq=False, local_vars_configuration=None):  # noqa: E501
        """LoggingSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._debug = None
        self._quiet = None
        self._strict = None
        self._timed = None
        self._zeromq = None
        self.discriminator = None

        if debug is not None:
            self.debug = debug
        if quiet is not None:
            self.quiet = quiet
        if strict is not None:
            self.strict = strict
        if timed is not None:
            self.timed = timed
        if zeromq is not None:
            self.zeromq = zeromq

    @property
    def debug(self):
        """Gets the debug of this LoggingSpec.  # noqa: E501

        Debug mode adds extra verbosity to Flux  # noqa: E501

        :return: The debug of this LoggingSpec.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this LoggingSpec.

        Debug mode adds extra verbosity to Flux  # noqa: E501

        :param debug: The debug of this LoggingSpec.  # noqa: E501
        :type debug: bool
        """

        self._debug = debug

    @property
    def quiet(self):
        """Gets the quiet of this LoggingSpec.  # noqa: E501

        Quiet mode silences all output so the job only shows the test running  # noqa: E501

        :return: The quiet of this LoggingSpec.  # noqa: E501
        :rtype: bool
        """
        return self._quiet

    @quiet.setter
    def quiet(self, quiet):
        """Sets the quiet of this LoggingSpec.

        Quiet mode silences all output so the job only shows the test running  # noqa: E501

        :param quiet: The quiet of this LoggingSpec.  # noqa: E501
        :type quiet: bool
        """

        self._quiet = quiet

    @property
    def strict(self):
        """Gets the strict of this LoggingSpec.  # noqa: E501

        Strict mode ensures any failure will not continue in the job entrypoint  # noqa: E501

        :return: The strict of this LoggingSpec.  # noqa: E501
        :rtype: bool
        """
        return self._strict

    @strict.setter
    def strict(self, strict):
        """Sets the strict of this LoggingSpec.

        Strict mode ensures any failure will not continue in the job entrypoint  # noqa: E501

        :param strict: The strict of this LoggingSpec.  # noqa: E501
        :type strict: bool
        """

        self._strict = strict

    @property
    def timed(self):
        """Gets the timed of this LoggingSpec.  # noqa: E501

        Timed mode adds timing to Flux commands  # noqa: E501

        :return: The timed of this LoggingSpec.  # noqa: E501
        :rtype: bool
        """
        return self._timed

    @timed.setter
    def timed(self, timed):
        """Sets the timed of this LoggingSpec.

        Timed mode adds timing to Flux commands  # noqa: E501

        :param timed: The timed of this LoggingSpec.  # noqa: E501
        :type timed: bool
        """

        self._timed = timed

    @property
    def zeromq(self):
        """Gets the zeromq of this LoggingSpec.  # noqa: E501

        Enable Zeromq logging  # noqa: E501

        :return: The zeromq of this LoggingSpec.  # noqa: E501
        :rtype: bool
        """
        return self._zeromq

    @zeromq.setter
    def zeromq(self, zeromq):
        """Sets the zeromq of this LoggingSpec.

        Enable Zeromq logging  # noqa: E501

        :param zeromq: The zeromq of this LoggingSpec.  # noqa: E501
        :type zeromq: bool
        """

        self._zeromq = zeromq

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
        if not isinstance(other, LoggingSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoggingSpec):
            return True

        return self.to_dict() != other.to_dict()
