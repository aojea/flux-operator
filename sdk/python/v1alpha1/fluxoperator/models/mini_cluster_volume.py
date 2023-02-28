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


class MiniClusterVolume(object):
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
        'annotations': 'dict(str, str)',
        'capacity': 'str',
        'labels': 'dict(str, str)',
        'path': 'str',
        'secret': 'str',
        'secret_namespace': 'str',
        'storage_class': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'capacity': 'capacity',
        'labels': 'labels',
        'path': 'path',
        'secret': 'secret',
        'secret_namespace': 'secretNamespace',
        'storage_class': 'storageClass'
    }

    def __init__(self, annotations=None, capacity='5Gi', labels=None, path='', secret='', secret_namespace='default', storage_class='hostpath', local_vars_configuration=None):  # noqa: E501
        """MiniClusterVolume - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._capacity = None
        self._labels = None
        self._path = None
        self._secret = None
        self._secret_namespace = None
        self._storage_class = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if capacity is not None:
            self.capacity = capacity
        if labels is not None:
            self.labels = labels
        self.path = path
        if secret is not None:
            self.secret = secret
        if secret_namespace is not None:
            self.secret_namespace = secret_namespace
        if storage_class is not None:
            self.storage_class = storage_class

    @property
    def annotations(self):
        """Gets the annotations of this MiniClusterVolume.  # noqa: E501

        Annotations for persistent volume claim  # noqa: E501

        :return: The annotations of this MiniClusterVolume.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this MiniClusterVolume.

        Annotations for persistent volume claim  # noqa: E501

        :param annotations: The annotations of this MiniClusterVolume.  # noqa: E501
        :type annotations: dict(str, str)
        """

        self._annotations = annotations

    @property
    def capacity(self):
        """Gets the capacity of this MiniClusterVolume.  # noqa: E501

        Capacity (string) for PVC (storage request) to create PV  # noqa: E501

        :return: The capacity of this MiniClusterVolume.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this MiniClusterVolume.

        Capacity (string) for PVC (storage request) to create PV  # noqa: E501

        :param capacity: The capacity of this MiniClusterVolume.  # noqa: E501
        :type capacity: str
        """

        self._capacity = capacity

    @property
    def labels(self):
        """Gets the labels of this MiniClusterVolume.  # noqa: E501


        :return: The labels of this MiniClusterVolume.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this MiniClusterVolume.


        :param labels: The labels of this MiniClusterVolume.  # noqa: E501
        :type labels: dict(str, str)
        """

        self._labels = labels

    @property
    def path(self):
        """Gets the path of this MiniClusterVolume.  # noqa: E501


        :return: The path of this MiniClusterVolume.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this MiniClusterVolume.


        :param path: The path of this MiniClusterVolume.  # noqa: E501
        :type path: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def secret(self):
        """Gets the secret of this MiniClusterVolume.  # noqa: E501

        Secret reference in Kubernetes with service account role  # noqa: E501

        :return: The secret of this MiniClusterVolume.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this MiniClusterVolume.

        Secret reference in Kubernetes with service account role  # noqa: E501

        :param secret: The secret of this MiniClusterVolume.  # noqa: E501
        :type secret: str
        """

        self._secret = secret

    @property
    def secret_namespace(self):
        """Gets the secret_namespace of this MiniClusterVolume.  # noqa: E501

        Secret namespace  # noqa: E501

        :return: The secret_namespace of this MiniClusterVolume.  # noqa: E501
        :rtype: str
        """
        return self._secret_namespace

    @secret_namespace.setter
    def secret_namespace(self, secret_namespace):
        """Sets the secret_namespace of this MiniClusterVolume.

        Secret namespace  # noqa: E501

        :param secret_namespace: The secret_namespace of this MiniClusterVolume.  # noqa: E501
        :type secret_namespace: str
        """

        self._secret_namespace = secret_namespace

    @property
    def storage_class(self):
        """Gets the storage_class of this MiniClusterVolume.  # noqa: E501


        :return: The storage_class of this MiniClusterVolume.  # noqa: E501
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this MiniClusterVolume.


        :param storage_class: The storage_class of this MiniClusterVolume.  # noqa: E501
        :type storage_class: str
        """

        self._storage_class = storage_class

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
        if not isinstance(other, MiniClusterVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MiniClusterVolume):
            return True

        return self.to_dict() != other.to_dict()
